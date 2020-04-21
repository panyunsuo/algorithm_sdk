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


class AbnormalAlgorithmPlatform(object):
    class IncorrectAccountPassword(Exception):
        def __init__(self, *args):
            """
            账号密码错误
            :param args:异常信息
            """
            error = log('账号或密码错误', args=args)
            super().__init__(error)

    class InsufficientAccountPermissions(Exception):
        def __init__(self, *args):
            """
            账号权限不足
            :param args:异常信息
            """
            error = log('账号权限不足', args=args)
            super().__init__(error)

    class MissingParameters(Exception):
        def __init__(self, *args):
            """
            缺少参数
            :param args:异常信息
            """
            error = log('缺少参数', args=args)
            super().__init__(error)

    class AbnormalProduction(Exception):
        def __init__(self, *args):
            """
            制作异常
            :param args:异常信息
            """
            error = log('制作异常', args=args)
            super().__init__(error)

    class ProductionNotCompleted(Exception):
        def __init__(self, *args):
            """
            制作未完成
            :param args:异常信息
            """
            error = log('制作未完成', args=args)
            super().__init__(error)

    class UnknownFailure(Exception):
        def __init__(self, *args):
            """
            未知异常
            :param args:异常信息
            """
            error = log('未知异常', args=args)
            super().__init__(error)

    class ServerCrash(Exception):
        def __init__(self, *args):
            """
            服务器崩溃
            :param args:异常信息
            """
            error = log('服务器崩溃', args=args)
            super().__init__(error)

    @staticmethod
    def code_filter(code):
        code_abnormal = {
            401: AbnormalAlgorithmPlatform.IncorrectAccountPassword,
            402: AbnormalAlgorithmPlatform.InsufficientAccountPermissions,
            403: AbnormalAlgorithmPlatform.MissingParameters,
            501: AbnormalAlgorithmPlatform.ProductionNotCompleted,
            502: AbnormalAlgorithmPlatform.AbnormalProduction,
            500: AbnormalAlgorithmPlatform.ServerCrash
            }
        return code_abnormal.get(code)


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
#
# class AbnormalProduction(Exception):
#     def __init__(self, *args):
#         """
#         制作异常
#         :param args:异常信息
#         """
#         error = log('制作异常', args=args)
#         super().__init__(error)
