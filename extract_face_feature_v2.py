"""
@File    :   extract_face_feature_v2.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/21 9:29
"""

from .base import AlgoBase


class ExtractFaceFeatureV2(AlgoBase):
    __algo_name__ = 'extract_face_feature_v2'

    def __init__(self, auth_info, file, process=None, liveness_threshold=None, **kwargs):
        """
        提取人脸特征参数
        :param auth_info:验证参数
        :param file: 图片文件 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象
        :param process: 原图缩放参数
        :param liveness_threshold: 活体检测阈值
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['file'] = self.file_auto_process(file, has_none=False)
        self.request['process'] = process
        self.request['liveness_threshold'] = liveness_threshold
        self.request.update(kwargs)
