"""
@File    :   cut_photo.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/20 17:42
"""
import logging

from .base import AlgoBase


class CutPhoto(AlgoBase):
    __algo_name__ = 'cut_photo'

    def __init__(self, auth_info, file, specRule, ratios, img_size, background_color, process=None, ppi=300,
                 fair_level=None, img_format='PNG', is_check=False, file_size_section=None, need_mask_image=False,
                 need_fair=True, background_image_keys=None, beauty_level=None, **kwargs):
        """
        证件照制作(旧)
        :param auth_info: 验证信息
        :param file: 图片文件 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        :param specRule: 检测参数
        :param ratios: 裁剪参数
        :param img_size: 结果图缩放参数
        :param background_color:背景颜色
        :param process: 原图缩放参数
        :param ppi: ppi
        :param fair_level:美颜级别
        :param img_format: 结果图文件格式
        :param is_check: 是否需要检测
        :param file_size_section: 文件大小控制
        :param need_mask_image:是否需要遮罩图片
        :param need_fair: 是否只需要美颜图片
        :param background_image_keys: 背景图片
        :param beauty_level: 新的美颜级别参数
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['specRule'] = specRule
        self.request['process'] = process
        self.request['ratios'] = ratios
        self.request['file'] = self.file_auto_process(file)
        self.request['width_px'], self.request['height_px'] = img_size
        self.request['background_color'] = background_color
        self.request['ppi'] = ppi
        self.request['fair_level'] = fair_level
        self.request['img_format'] = img_format
        self.request['is_check'] = is_check
        self.request['file_size_section'] = file_size_section
        self.request['need_mask_image'] = need_mask_image
        self.request['need_fair'] = need_fair
        self.request['background_image_keys'] = background_image_keys
        self.request['beauty_level'] = beauty_level
        if not beauty_level and fair_level:
            logging.warning('fair_level 参数建议使用 beauty_level参数替换')
        self.request.update(kwargs)
