"""
@File    :   __init__.py.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/20 13:08

算法模块:
    algorithm_error 异常模块
        - algorithm_error.AbnormalAlgorithmPlatform API网关相关异常
    auth.AuthInfo 账号信息,需要初始化后作为参数给其他需要验证的模块调用
    base 基础类库模块
        -base.Base 主要是对图片算法的处理,可以上传/下载图片, 获取算法结果等,详细使用见模块说明
        -base.AlgoBase 对Base模块的封装,主要是有同步/异步发布算法的功能
        -bass.ExecutableFunction 使用函数作为图片的参数,当图片不存在时再执行该函数获取图片数据
    bg_cut_photo 换背景算法
    check_photo 合规检测
    cut_photo 证件照制作(不带缓存)
    cutout_and_beauty 证件照制作(带缓存)
    extract_face_feature_v2 人脸特征值提取
    facial_beauty 精修美颜
    human_plus 全身照/形象照
    image_resize 图片缩放
    match_face_feature_v2 人脸特征匹配
    wedding_photo 结婚照算法

使用示例:
结婚照

from algorithm_sdk import AuthInfo, WeddingPhoto

auth_info = AuthInfo(host='http://algo.leqi.us', username='your name', password='your password', intranet=True)
filename = 'src/1.jpg' # 本地图片路径

wedding_photo = WeddingPhoto(auth_info=auth_info, file=open(filename, 'rb').read())
resp = wedding_photo.synchronous_request()
print(resp.json)

"""
from . import algorithm_error
from .auth import AuthInfo
from .base import AlgoBase, Base, ExecutableFunction
from .bg_cut_photo import BgCutPhoto
from .card import Card
from .check_photo import CheckPhoto
from .cut_photo import CutPhoto
from .cutout_and_beauty import CutoutAndBeauty
from .extract_face_feature_v2 import ExtractFaceFeatureV2
from .facial_beauty import FacialBeauty
from .human_plus import HumanPlus
from .image_resize import ImageResize
from .match_face_feature_v2 import MatchFaceFeatureV2
from .wedding_photo import WeddingPhoto
from .facial_beauty_v2 import FacialBeautyV2

__version__ = '1.0.7'

__all__ = (
    algorithm_error, AlgoBase, AuthInfo, Base, BgCutPhoto, CheckPhoto, CutPhoto, CutoutAndBeauty, ExtractFaceFeatureV2,
    FacialBeauty, HumanPlus, ImageResize, MatchFaceFeatureV2, ImageResize, WeddingPhoto, ExecutableFunction, Card,
    FacialBeautyV2)
