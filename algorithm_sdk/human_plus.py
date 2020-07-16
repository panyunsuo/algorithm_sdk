"""
@File    :   human_plus.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/21 9:27
"""

from .base import AlgoBase


class HumanPlus(AlgoBase):
    __algo_name__ = 'human_plus'

    def __init__(self, auth_info, file, process=None, cut_params=None, need_to_use_cache=True, just_one_face=False,
                 **kwargs):
        """
        全身照/形象照算法
        :param auth_info:验证参数
        :param file: 图片文件 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        :param process: 原图缩放参数
        :param cut_params: 裁剪参数
        :param need_to_use_cache: 是否使用缓存
        :param just_one_face:是否只处理一张人脸的情况
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['file'] = self.file_auto_process(file, has_none=False)
        self.request['process'] = process
        self.request['cut_params'] = cut_params
        self.request['need_to_use_cache'] = need_to_use_cache
        self.request['just_one_face'] = just_one_face
        self.request.update(kwargs)
