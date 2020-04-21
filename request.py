"""
@File    :   response.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/20 13:30
"""
import requests

from .algorithm_error import UnknownType
from .resopnse import Response


class Request(object):

    def __init__(self):
        self.sess = requests.Session()

    def _request(self, url, data, method, headers=None, timeout=5):
        """
        请求服务器
        :param url:请求地址
        :param data: 请求数据
        :param method: 请求方式 有 GET POST PUT
        :param headers: 请求头
        :param timeout: 超时时间
        :return:
        """
        if method.upper() == 'GET':
            resp = self.sess.get(url, params=data, headers=headers, timeout=timeout)
        elif method.upper() == 'POST':
            resp = self.sess.post(url, json=data, headers=headers, timeout=timeout)
        elif method.upper() == 'PUT':
            resp = self.sess.put(url, data=data, headers=headers, timeout=timeout)
        else:
            raise UnknownType('没有', method, '请求方式')

        return resp

    def post(self, url, data, headers=None, timeout=5):
        resp = self._request(url, data, 'POST', headers, timeout)
        return Response(resp)

    def get(self, url, params, headers=None, timeout=5):
        resp = self._request(url, params, 'GET', headers, timeout)
        return Response(resp)

    def put(self, url, data, headers=None, timeout=5):
        resp = self._request(url, data, 'PUT', headers, timeout)
        return Response(resp)


request = Request()
