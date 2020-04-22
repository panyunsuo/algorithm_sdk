"""
@File    :   error.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/20 13:17
"""


def log(key, args):
    return (key + (' {} ' * len(args))).format(*args)


class UnknownType(Exception):
    def __init__(self, *args):
        """
        未知参数类型
        :param args:异常信息
        """
        error = log('未知参数类型', args=args)
        super().__init__(error)


class CannotBeConvertedToJSON(Exception):
    def __init__(self, *args):
        """
        无法转换数据为JOSN
        :param args:异常信息
        """
        error = log('无法转换数据为JOSN', args=args)
        super().__init__(error)


class TaskTimeoutNotCompleted(Exception):
    def __init__(self, *args):
        """
        任务超时未完成
        :param args:异常信息
        """
        error = log('任务超时未完成', args=args)
        super().__init__(error)


class AbnormalAlgorithmPlatform(Exception):
    """
    算法平台异常 一般为401 402 403的code只会在开发阶段出现,一旦开发阶段调通后就不会出现该异常
    """
    code = 400
    message = '算法平台异常'
    _code_abnormal = {}

    def __init__(self, *args):
        error = log(self.message, args=args)
        super().__init__(error)

    @classmethod
    def code_abnormal(cls):
        if not cls._code_abnormal:
            for sc in cls.__subclasses__():
                cls._code_abnormal[sc.code] = sc

        return cls._code_abnormal

    @classmethod
    def code_filter(cls, code):
        return cls.code_abnormal().get(code)


class IncorrectAccountPassword(AbnormalAlgorithmPlatform):
    code = 401
    message = '账号或密码错误'

    def __init__(self, *args):
        """
        账号密码错误
        :param args:异常信息
        """
        super().__init__(*args)


class InsufficientAccountPermissions(AbnormalAlgorithmPlatform):
    code = 402
    message = '账号权限不足'

    def __init__(self, *args):
        """
        账号权限不足
        :param args:异常信息
        """
        super().__init__(*args)


class MissingParameters(AbnormalAlgorithmPlatform):
    code = 403
    message = '缺少参数'

    def __init__(self, *args):
        """
        缺少参数
        :param args:异常信息
        """
        super().__init__(*args)


class AbnormalProduction(AbnormalAlgorithmPlatform):
    code = 502
    message = '制作异常'

    def __init__(self, *args):
        """
        制作异常
        :param args:异常信息
        """
        super().__init__(*args)


class ProductionNotCompleted(AbnormalAlgorithmPlatform):
    code = 501
    message = '制作未完成'

    def __init__(self, *args):
        """
        制作未完成
        :param args:异常信息
        """
        super().__init__(*args)


class UnknownFailure(AbnormalAlgorithmPlatform):
    code = 0
    message = '未知异常'

    def __init__(self, *args):
        """
        未知异常
        :param args:异常信息
        """
        super().__init__(*args)


class ServerCrash(AbnormalAlgorithmPlatform):
    code = 500
    message = '服务器崩溃'

    def __init__(self, *args):
        """
        服务器崩溃
        :param args:异常信息
        """
        super().__init__(*args)
#
# class AbnormalProduction(Exception):
#     def __init__(self, *args):
#         """
#         制作异常
#         :param args:异常信息
#         """
#         error = log('制作异常', args=args)
#         super().__init__(error)
