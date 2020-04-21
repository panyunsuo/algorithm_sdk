"""
@File    :   check_photo.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/20 14:52
"""
from .base import AlgoBase


class CheckPhoto(AlgoBase):
    __algo_name__ = 'check_photo'

    def __init__(self, auth_info, file, process=None, specRule=None):
        """
        合规检测算法
        :param auth_info: 验证参数
        :param file: 图片文件 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象
        :param process:缩放参数
        :param specRule:检测参数
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['file'] = self.file_auto_process(file, has_none=False)
        self.request['process'] = process
        self.request['specRule'] = specRule
