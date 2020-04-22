"""
@File    :   base.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/20 13:11
"""
import hashlib
import io
import time
from urllib.parse import urljoin

from PIL import Image

from .algorithm_error import TaskTimeoutNotCompleted, UnknownType
from .auth import AuthInfo
from .request import request


# 获取MD5的函数
def get_md5(data):
    md5_obj = hashlib.md5()
    md5_obj.update(data)
    hash_code = md5_obj.hexdigest()
    return hash_code


class Base(object):
    """
    基础库,封装了一些基础的函数,例如图片上传 下载 生成预览url 根据任务ID获取结果等,可以单独初始化此库来使用上述功能
    """

    def __init__(self, auth_info: AuthInfo):
        self._host = auth_info.host
        self._username = auth_info.username
        self._intranet = auth_info.intranet
        self._password = auth_info.password

    def _get_put_url(self, oss_name, intranet):
        allot_data = {
            'user': self._username,
            'pwd': self._password,
            'filename': oss_name,
            'intranet': intranet
            }
        resp = request.post(self.api_send_oss_url, data=allot_data)
        resp.verify()
        return resp.json['put_url'], resp.json.get('exist_file'), resp.json['oss_name']

    def _get_file_url(self, oss_name, intranet, watermark):
        params = {
            'filename': oss_name,
            'intranet': intranet,
            'watermark': watermark
            }
        resp = request.get(self.api_get_oss_url, params=params)
        resp.verify()
        return resp.json['preview_url']

    def send_file(self, file_bytes, oss_name=None, cover=False, intranet=None):
        """
        上传文件到算法的oss中
        :param file_bytes:文件二进制数据
        :param oss_name: 指定的oss文件名称,若为None则会使用文件md5来命名(此处的文件名不是最终的文件名)
        :param cover: 当该文件名在oss上存在时,是否需要重新上传,覆盖该文件
        :param intranet: 是否使用内网传输, 为None时将使用auth_info中的参数
        :return: 文件在oss上面的文件名
        """
        if intranet is None:
            intranet = self._intranet

        if not oss_name:
            oss_name = get_md5(file_bytes)

        put_url, exist_file, oss_name = self._get_put_url(oss_name, intranet)

        if not exist_file or cover:
            resp = request.put(put_url, data=file_bytes, timeout=10)
            resp.verify()

        return oss_name

    def get_file(self, oss_name=None, intranet=None):
        """
        下载文件数据
        :param oss_name:文件在阿里云oss上的名称
        :param intranet: 是否使用内网传输, 为None时将使用auth_info中的参数
        :return: 图片二进制数据
        """
        if intranet is None:
            intranet = self._intranet
        get_url = self._get_file_url(oss_name, intranet, watermark=None)
        resp = request.get(get_url, timeout=10)
        resp.verify()
        return resp.content

    def get_file_url(self, oss_name, intranet=False, watermark=None):
        """
        生成文件的预览地址
        :param oss_name: 文件在阿里云oss上的名称
        :param intranet: 是否使用内网传输, 为None时将使用auth_info中的参数
        :param watermark: 图片水印
        :return: url
        """
        if intranet is None:
            intranet = self._intranet
        get_url = self._get_file_url(oss_name, intranet, watermark)
        return get_url

    def get_results(self, task_id):
        """
        根据任务ID获取处理结果,未处理完成时resp.allot_code=501
        :param task_id: 任务ID
        :return: algorithm.response.Response
        """
        url = self.api_task_id.format(task_id=task_id)
        resp = request.get(url, params={})
        return resp

    @property
    def api_send_oss_url(self):
        """
        网关平台上传文件的url
        :return:url
        """
        api = 'api/oss_url'
        return urljoin(self._host, api)

    @property
    def api_get_oss_url(self):
        """
        网关平台获取文件的url
        :return:url
        """
        api = 'api/oss_url'
        return urljoin(self._host, api)

    @property
    def api_sync_url(self):
        """
        网关平台同步请求算法的url
        :return:url
        """
        api = 'api/algorithm'
        return urljoin(self._host, api)

    @property
    def api_async_url(self):
        """
        网关平台异步请求算法的url
        :return:url
        """
        api = 'api/algorithm/async'
        return urljoin(self._host, api)

    @property
    def api_task_id(self):
        """
        网关平台获取任务结果的url
        :return:url
        """
        api = 'api/algorithm/{task_id}'
        return urljoin(self._host, api)


class AlgoBase(Base):
    """
    各个算法的基类,通过继承此模块,拥有生成算法参数,请求算法等功能
    """

    def __init__(self, auth_info: AuthInfo, algo_name):
        super().__init__(auth_info)
        self.algo_name = algo_name
        self.need_cache = auth_info.need_cache
        self.request = {}

    @property
    def json(self):
        """
        生成算法请求的json参数
        :return: dict
        """
        return {
            'user': self._username,
            'pwd': self._password,
            'target': self.algo_name,
            'need_cache': self.need_cache,
            'request': self.request
            }

    def synchronous_request(self, timeout=30, interval=0.5):
        """
        同步请求算法(实质上是多次异步请求)
        :param timeout:请求超时时间
        :param interval: 每次轮询的间隔
        :return:algorithm.response.Response
        """
        stop_time = time.time() + timeout
        # 发布任务
        task_id = self.asynchronous_request().task_id
        while time.time() < stop_time:
            response = self.get_results(task_id)
            if response:
                if response.allot_code == 200:
                    return response
                elif response.allot_code != 501:
                    response.verify()
            time.sleep(interval)

        raise TaskTimeoutNotCompleted(task_id, timeout, interval)

    def asynchronous_request(self):
        """
        异步发布算法
        :return:algorithm.response.Response
        """
        response = request.post(self.api_async_url, data=self.json)
        response.verify()
        return response

    def file_auto_process(self, file, has_none=None):
        """
        文件自动处理,若传入的
        :param file:文件,可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象
        :param has_none:是否可以为None
        :return:str:oss文件名
        """
        if not file and has_none:
            raise TypeError('参数不得为空')
        if isinstance(file, str):
            return file
        elif isinstance(file, bytes):
            return self.send_file(file)
        elif isinstance(file, Image.Image):
            buffer = io.BytesIO()
            file.save(buffer, format='PNG')
            return self.send_file(buffer.getvalue())
        else:
            raise UnknownType(file, type(file))
