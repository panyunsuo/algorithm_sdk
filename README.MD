** 算法模块 **

* `algorithm_error` 异常模块  
* * `algorithm_error.AbnormalAlgorithmPlatform` API网关相关异常  
* `auth.AuthInfo` 账号信息,需要初始化后作为参数给其他需要验证的模块调用  
* `base` 基础类库模块
* * `base.Base` 主要是对图片算法的处理,可以上传/下载图片, 获取算法结果等,详细使用见模块说明
* * `base.AlgoBase` 对`Base`模块的封装,主要是有同步/异步发布算法的功能
* `BgCutPhoto` 换背景算法
* `CheckPhoto` 合规检测
* `CutPhoto` 证件照制作(不带缓存)
* `CutoutAndBeauty` 证件照制作(带缓存)
* `ExtractFaceFeatureV2` 人脸特征值提取
* `FacialBeauty` 精修美颜
* `HumanPlus` 全身照/形象照
* `ImageResize` 图片缩放
* `MatchFaceFeatureV2` 人脸特征匹配
* `ImageResize` 结婚照算法

** 使用示例: **
> 结婚照

```python
from algorithm_sdk import AuthInfo, WeddingPhoto

auth_info = AuthInfo(host='http://ialgo.leqi.us', username='your name', password='your password', intranet=True)
filename = 'src/1.jpg' # 本地图片路径

wedding_photo = WeddingPhoto(auth_info=auth_info, file=open(filename, 'rb').read())
resp = wedding_photo.synchronous_request()
print(resp.json)
```