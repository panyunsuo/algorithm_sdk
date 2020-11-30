# 安装  
`python3 setup.py install`

# 算法模块

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

# 使用示例: 
> 结婚照

```python
from algorithm_sdk import algorithm_error, AuthInfo, Base, WeddingPhoto

auth_info = AuthInfo(host='http://algo.leqi.us', username='your name', password='your password', intranet=True)
# 本地图片路径
filename = 'src/1.jpg'

# 缩放参数(含义为将图片等比缩放为最大边小于2000且为JPG格式的图片)
process = 'image/resize,m_lfit,w_2000,h_2000,limit_1/auto-orient,1/format,jpg'
# 美颜参数
fair_level_left = {'skinsoft': 0, 'reyelarge': 2, 'skinwhite': 2, 'mouthlarge': 2, 'facelift': 2, 'leyelarge': 2, 'coseye': 2}

# 创建算法对象,各个算法的各个参数具体含义可见文档
wedding_photo = WeddingPhoto(auth_info=auth_info, file=open(filename, 'rb').read(), img_size=(750, 500), process=process, fair_level_left=fair_level_left)

# 同步请求算法
resp = wedding_photo.synchronous_request()
print('同步请求算法完成', resp.json, '\n')

# 异步发布任务
resp = wedding_photo.asynchronous_request()
print('异步发布任务得到任务ID为', resp.task_id, '\n')

# 根据任务ID获取处理结果(顺带演示异常的使用,异常可以在各类请求时进行捕获并做处理)
try:
    # 使用Base类来操作任务结果
    base = Base(auth_info=auth_info)
    resp = base.get_results(resp.task_id)

    # verify()方法主要是用来检测算法平台返回的状态码是否正常,为非200的将会抛出异常
    resp.verify()
    # 判断算法服务器状态码,若该图片无法制作该规格之类的提示可在此判断
    if resp.code != 200:
        print('算法制作异常 code:', resp.code, 'message', resp.message)
        exit()
    
    # 从返回值中拿到结果图,各个算法的返回参数可见文档
    beauty_file = resp.json['beauty_file']

    # 生成图片预览的url(可以视情况加水印,此处的url由于是给外网访问的,所以intranet参数要为False)
    url = base.get_file_url(beauty_file, intranet=False)
    print('url', url)

    # 下载文件到本地
    img_bytes = base.get_file(oss_name=beauty_file)
    with open('beauty_file.png', 'wb') as f:
        f.write(img_bytes)
    print('文件下载成功 ./beauty_file.png')

except algorithm_error.ProductionNotCompleted:
    # 实际情况下,当出现此异常,要么是服务器休眠0.5s后再次轮询,要么是客户端休眠0.5s后再拿此task_id来轮询服务器
    print('算法制作未完成,请循环请求')
    exit()
except algorithm_error.AbnormalAlgorithmPlatform as e:
    # 算法平台对除未制作完成的异常外进行全异常捕捉
    print('算法平台异常 状态码:', e.code, '状态提示', e.message)
    exit()
except Exception as e:
    print('未知异常 ', e)
    exit()
```