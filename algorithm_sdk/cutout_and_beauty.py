"""
@File    :   cutout_and_beauty.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/21 9:15
"""
import logging

from .base import AlgoBase


class CutoutAndBeauty(AlgoBase):
    __algo_name__ = 'cutout_and_beauty'

    def __init__(self, auth_info, file, facial_data, process=None, fair_level=None, img_size=None, clothes_keys=None,
                 need_resize=True, save_pack_data=False, has_full_body_dress_up=False, collar_coordinates=None,
                 hat_img=None, beauty_level=None, **kwargs):
        """
        带换装功能的抠图美颜算法
        :param auth_info:验证参数
        :param file:图片文件 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        :param facial_data:裁剪参数
        :param process:原图缩放参数
        :param fair_level:美颜级别
        :param img_size:结果图缩放参数
        :param clothes_keys:衣服模板 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        :param need_resize:是否需要照着img_size缩放
        :param save_pack_data:是否需要打包中间结果(算法人员调试使用)
        :param collar_coordinates:左右衣领坐标
        :param hat_img:帽子模板 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        :param beauty_level: 新的美颜级别参数
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['file'] = self.file_auto_process(file, has_none=False)
        self.request['process'] = process
        self.request['facial_data'] = facial_data
        self.request['fair_level'] = fair_level
        self.request['img_size'] = img_size
        self.request['clothes_keys'] = [self.file_auto_process(file, has_none=True) for file in clothes_keys]
        self.request['need_resize'] = need_resize
        self.request['save_pack_data'] = save_pack_data
        self.request['beauty_level'] = beauty_level
        self.request['has_full_body_dress_up'] = has_full_body_dress_up
        self.request['collar_coordinates'] = collar_coordinates
        self.request['hat_img'] = self.file_auto_process(hat_img, has_none=True)
        if not beauty_level and fair_level:
            logging.warning('fair_level 参数建议使用 beauty_level参数替换')
        self.request.update(kwargs)
