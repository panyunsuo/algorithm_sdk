"""
@File    :   image_handle.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/7/30 15:26
------------
@Model Name:   审核工具处理
"""
from .base import AlgoBase


class AccountingExaminationReview(AlgoBase):
    __algo_name__ = 'accounting_examination_review'

    def __init__(self, auth_info, url, client_type, cache, **kwargs):
        """
        :param auth_info:验证参数
        :param url:图片的下载地址,建议为OSS内网下载地址
        :param client_type:客户端类型
        :param cache:是否使用缓存
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['url'] = url
        self.request['client_type'] = client_type
        self.request['cache'] = cache
        self.request.update(kwargs)
