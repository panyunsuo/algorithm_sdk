"""
@File    :   cutout_and_beauty.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/21 9:15
"""

from .base import AlgoBase


class CutoutAndBeauty(AlgoBase):
    __algo_name__ = 'cutout_and_beauty'

    def __init__(self, auth_info, file, facial_data, process=None, fair_level=None, img_size=None, clothes_keys=None,
                 need_resize=True, save_pack_data=False, use_thumbnail_cutout=True, torso_ratio=1,
                 has_full_body_dress_up=False, collar_coordinates=None, **kwargs):
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
        :param use_thumbnail_cutout:是否使用缩图抠图
        :param torso_ratio:身体比例
        :param collar_coordinates:左右衣领坐标
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['file'] = self.file_auto_process(file, has_none=False)
        self.request['process'] = process
        self.request['facial_data'] = facial_data
        self.request['fair_level'] = fair_level
        self.request['img_size'] = img_size
        self.request['clothes_keys'] = [self.file_auto_process(file) for file in clothes_keys]
        self.request['need_resize'] = need_resize
        self.request['save_pack_data'] = save_pack_data
        self.request['use_thumbnail_cutout'] = use_thumbnail_cutout
        self.request['torso_ratio'] = torso_ratio
        self.request['has_full_body_dress_up'] = has_full_body_dress_up
        self.request['collar_coordinates'] = collar_coordinates
        self.request.update(kwargs)
