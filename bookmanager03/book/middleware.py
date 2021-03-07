# 李禄波
# 2021/3/7 14:29
from django.utils.deprecation import MiddlewareMixin


class TestMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        print('每次请求前会调用执行')

        username = request.COOKIES.get('name')
        if username is None:
            print('没有用户信息')
        else:
            print('存在用户信息')

    def process_response(self, request, response):
        print('每次响应前会调用执行')

        return response

