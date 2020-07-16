"""
@File    :   check_photo.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/20 14:52
"""
from .base import AlgoBase


class Card(AlgoBase):
    __algo_name__ = 'card'

    def __init__(self, auth_info, file, process=None, need_goal_graph=False, **kwargs):
        """
        身份证识别
        :param auth_info: 验证参数
        :param file: 图片文件 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        :param process:缩放参数
        :param need_goal_graph:是否需要目标图
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['file'] = self.file_auto_process(file, has_none=False)
        self.request['process'] = process
        self.request['need_goal_graph'] = need_goal_graph
        self.request.update(kwargs)
