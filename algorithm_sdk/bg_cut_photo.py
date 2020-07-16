"""
@File    :   bg_cut_photo.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/21 8:44
"""
import logging

from .base import AlgoBase


class BgCutPhoto(AlgoBase):
    __algo_name__ = 'bg_cut_photo'

    def __init__(self, auth_info, file, background_color, process=None, ppi=300, fair_level=None,
                 need_not_beaut_img=True, need_mask_image=False, need_original_background_color=False,
                 beauty_level=None, **kwargs):
        """
        原图换背景(建议用全身照算法)
        :param auth_info: 验证参数
        :param file: 图片文件 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        :param background_color: 背景颜色
        :param process: 原图缩放参数
        :param ppi: ppi
        :param fair_level:美颜级别
        :param need_not_beaut_img:是否需要未美颜图片
        :param need_mask_image: 是否需要遮罩图片
        :param need_original_background_color:是否需要原图背景的图片
        :param torso_ratio: 身体裁剪比例
        :param beauty_level: 新的美颜级别参数
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['file'] = self.file_auto_process(file, has_none=False)
        self.request['process'] = process
        self.request['background_color'] = background_color
        self.request['ppi'] = ppi
        self.request['fair_level'] = fair_level
        self.request['need_not_beaut_img'] = need_not_beaut_img
        self.request['need_mask_image'] = need_mask_image
        self.request['need_original_background_color'] = need_original_background_color
        self.request['beauty_level'] = beauty_level
        if not beauty_level and fair_level:
            logging.warning('fair_level 参数建议使用 beauty_level参数替换')
        self.request.update(kwargs)
