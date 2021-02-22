from .base import AlgoBase


class OriginalBackgroundCrop(AlgoBase):
    __algo_name__ = 'original_background_crop'

    def __init__(self, auth_info, file, facial_data, process=None, img_size=None, need_resize=True, **kwargs):
        """
        证件照带原背景的裁剪算法
        :param auth_info:验证参数
        :param file:图片文件 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        :param facial_data:裁剪参数
        :param process:原图缩放参数
        :param img_size:结果图缩放参数
        :param need_resize:是否需要照着img_size缩放
        @param kwargs:
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['file'] = self.file_auto_process(file, has_none=False)
        self.request['process'] = process
        self.request['facial_data'] = facial_data
        self.request['img_size'] = img_size
        self.request['need_resize'] = need_resize
        self.request.update(kwargs)
