"""
@File    :   resopnse.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/20 13:43
"""
from . import algorithm_error


class Response(object):
    """
    请求接口后的响应对象
    """
    _dict = None

    def __init__(self, resp):
        """
        :param resp: requests响应对象
        """
        self.resp = resp

    @property
    def json(self):
        """
        响应数据的dict类型数据
        :return: dict
        """
        if not self._dict:
            try:
                self._dict = self.resp.json()
            except Exception:
                raise algorithm_error.CannotBeConvertedToJSON(self.resp.text)

        return self._dict

    @property
    def ok(self):
        """
        是否请求成功(http code==200)
        :return: bool
        """
        return self.resp.ok

    @property
    def text(self):
        """
        响应数据的文本数据
        :return: str
        """
        return self.resp.text

    @property
    def content(self):
        """
        响应数据的二进制数据
        :return: bytes
        """
        return self.resp.content

    @property
    def allot_code(self):
        """
        网关平台响应码
        :return: int
        """
        return self.resp.status_code

    @property
    def use_cache(self):
        """
        网关平台是否使用了缓存
        :return: bool
        """
        return self.json.get('algo_cache', False)

    @property
    def task_id(self):
        """
        获取task id ,只有算法同步/异步发布成功后才有此数据
        :return: str
        """
        return self.json.get('task_id')

    @property
    def algo_server_timing(self):
        """
        算法平台响应时间(s)
        :return: float
        """
        return self.json.get('algo_server_timing')

    @property
    def allot_version(self):
        """
        算法平台版本
        :return: str
        """
        return self.json.get('allot_version')

    @property
    def first_acquisition(self):
        """
        当为异步任务根据task_id获取结果时,此字段为是否第一次获取结果
        :return:bool
        """
        return self.json.get('first_acquisition')

    @property
    def error(self):
        """
        算法平台错误信息,可能为None
        :return: str
        """
        return self.json.get('error')

    @property
    def code(self):
        """
        算法本身的异常信息
        :return: str
        """
        return self.json.get('code')

    @property
    def message(self):
        """
        算法本身的异常信息,可能为None
        :return: str
        """
        return self.json.get('message')

    def verify(self):
        """
        校验http code是否为200,若不是,则抛出对应的异常
        :return:
        """
        e = algorithm_error.AbnormalAlgorithmPlatform.code_filter(self.allot_code)
        if e:
            raise e(self.resp.text)

        if self.allot_code != 200:
            raise algorithm_error.UnknownFailure(self.resp.text)
