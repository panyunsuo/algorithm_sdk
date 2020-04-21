"""
@File    :   image_resize.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/21 9:39
"""
from .base import AlgoBase


class ImageResize(AlgoBase):
    __algo_name__ = 'image_resize'

    def __init__(self, auth_info, file, process=None, sharp=True, mode=0, img_format='JPEG'):
        """
        图片缩放
        :param auth_info:验证参数
        :param file: 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象
        :param process: 算法处理前的原图缩放参数
        :param sharp: 是否需要锐化
        :param mode: 缩放模式
        :param img_format: 结果图格式
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['file'] = self.file_auto_process(file, has_none=False)
        self.request['process'] = process
        self.request['sharp'] = sharp
        self.request['mode'] = mode
        self.request['img_format'] = img_format
