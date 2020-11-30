"""
@File    :   image_handle.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/7/30 15:26
------------
@Model Name:   图片处理
"""
from .base import AlgoBase


class ImageHandle(AlgoBase):
    __algo_name__ = 'image_handle'

    def __init__(self, auth_info, file, process=None, img_format='JPEG', scaling_parameters=None, crop_params=None,
                 person_info=None, **kwargs):
        """
        图片处理
        :param auth_info:验证参数
        :param file: 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        :param process: 算法处理前的原图缩放参数
        :param img_format: 结果图格式
        :param scaling_parameters: 缩放参数
        :param crop_params: 裁剪参数
        :param person_info: 是否需要人的信息(年龄/性别)
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['file'] = self.file_auto_process(file, has_none=False)
        self.request['process'] = process
        self.request['img_format'] = img_format
        self.request['scaling_parameters'] = scaling_parameters
        self.request['crop_params'] = crop_params
        self.request['person_info'] = person_info
        self.request.update(kwargs)
