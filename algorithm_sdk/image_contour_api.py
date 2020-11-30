"""
@File    :   image_merge_api.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/9/4 8:43
------------
@Model Name:   图片加轮廓算法

@Notes:
"""
from .base import AlgoBase


class ImageContourApi(AlgoBase):
    __algo_name__ = 'image_contour_api'

    def __init__(self, auth_info, fore_file, mask_file, style, process=None, **kwargs):
        """
        图片融合
        :param auth_info:验证参数
        :param fore_file: 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        :param mask_file: 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        :param back_file: 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        :param process: 算法处理前的原图缩放参数
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['fore_file'] = self.file_auto_process(fore_file, has_none=False)
        self.request['mask_file'] = self.file_auto_process(mask_file, has_none=True)
        self.request['style'] = style
        self.request['process'] = process
        self.request.update(kwargs)
