
"""
@File    :   auth_info.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/21 10:47
"""
class AuthInfo(object):

    def __init__(self, host, username, password, intranet=True, need_cache=True):
        """
        账号验证
        :param host:服务器地址 例如:http://algo.leqi.us
        :param username: 算法账号名
        :param password: 算法密码
        :param intranet: 是否使用内网传输图片文件
        :param need_cache: 是否需要网关平台使用缓存
        """
        self.host = host
        self.username = username
        self.intranet = intranet
        self.password = password
        self.need_cache = need_cache