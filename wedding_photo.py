"""
@File    :   wedding_photo.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/21 9:03
"""
from .base import AlgoBase


class WeddingPhoto(AlgoBase):
    __algo_name__ = 'wedding_photo'

    def __init__(self, auth_info, file, img_size=None, process=None, fair_level_right=None, fair_level_left=None,
                 need_beauty_buffer=False, use_cache=True, **kwargs):
        """
        结婚照算法
        :param auth_info:验证参数
        :param file: 图片文件 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象
        :param img_size: 结果图缩放参数
        :param process: 原图缩放参数
        :param fair_level_right: 右脸美颜参数
        :param fair_level_left:左脸美颜参数
        :param need_beauty_buffer: 是否需要美颜buffer(用于本地美颜)
        :param use_cache: 是否需要使用缓存
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['file'] = self.file_auto_process(file)
        self.request['img_size'] = img_size
        self.request['process'] = process
        self.request['fair_level_right'] = fair_level_right
        self.request['fair_level_left'] = fair_level_left
        self.request['need_beauty_buffer'] = need_beauty_buffer
        self.request['use_cache'] = use_cache
        self.request.update(kwargs)
