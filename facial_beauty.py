"""
@File    :   facial_beauty.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/21 8:51
"""
from .base import AlgoBase


class FacialBeauty(AlgoBase):
    __algo_name__ = 'facial_beauty'

    def __init__(self, auth_info, file, beauty_level, process=None, refer_images=None, ppi=300, need_cache=True,
                 img_format='PNG', use_mask=False):
        """
        精修美颜
        :param auth_info:验证参数
        :param file: 图片文件 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象
        :param beauty_level:美颜级别
        :param process:原图缩放参数
        :param refer_images:美颜模板 [file1, file2]
        :param ppi:ppi
        :param need_cache:是否需要缓存
        :param img_format:结果图格式
        :param use_mask:是否需要使用原图的第4通道为遮罩
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['file'] = self.file_auto_process(file, has_none=False)
        self.request['process'] = process
        self.request['beauty_level'] = beauty_level
        self.request['refer_images'] = [self.file_auto_process(file) for file in refer_images]
        self.request['ppi'] = ppi
        self.request['need_cache'] = need_cache
        self.request['img_format'] = img_format
        self.request['use_mask'] = use_mask
