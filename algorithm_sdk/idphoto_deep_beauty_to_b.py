from .base import AlgoBase


class IDPhotoDeepBeautyToB(AlgoBase):
    __algo_name__ = 'idphoto_deep_beauty_to_b'

    def __init__(self, auth_info, oss_name, process=None, spec_info=None, deep_beauty_template=None, need_resize=True,
                 **kwargs):
        """
        证件照B端精修美颜
        @param auth_info:
        @param file:图片文件 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        @param process:原图缩放参数
        @param spec_info: 规格参数
        @param deep_beauty_template: 模板名称
        @param need_resize:是否需要缩放
        @param kwargs:
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['oss_name'] = self.file_auto_process(oss_name, has_none=False)
        self.request['process'] = process
        self.request['spec_info'] = spec_info
        self.request['deep_beauty_template'] = deep_beauty_template
        self.request['need_resize'] = need_resize
        self.request.update(kwargs)
