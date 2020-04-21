"""
@File    :   match_face_feature_v2.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/21 9:31
"""
from .base import AlgoBase


class MatchFaceFeatureV2(AlgoBase):
    __algo_name__ = 'match_face_feature_v2'

    def __init__(self, auth_info, target_features, filter_features_file=None, filter_features_list=None,
                 reference_similarity=None):
        """
        人脸特征匹配
        :param auth_info:验证参数
        :param target_features: 目标特征值
        :param filter_features_file: 匹配特征值文件 适合数据量大的场景 可以是str:oss文件名 bytes:原图字节文件
        :param filter_features_list: 匹配特征值列表,适合数据量小的场景(与filter_features_file参数二选一传)
        :param reference_similarity:参照的相似度
        """
        super().__init__(auth_info, self.__algo_name__)
        self.request['target_features'] = target_features
        self.request['filter_features_file'] = self.file_auto_process(filter_features_file, has_none=True)
        self.request['filter_features_list'] = filter_features_list
        self.request['reference_similarity'] = reference_similarity
