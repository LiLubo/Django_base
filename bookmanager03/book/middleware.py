# 李禄波
# 2021/3/7 14:29
from django.utils.deprecation import MiddlewareMixin

'''
多个中间件的执行顺序
    ·在请求视图被处理前，中间件由上至下依次执行
    ·在请求视图被处理后，中间件由下至上依次执行

'''


class TestMiddleWare1(MiddlewareMixin):

    def process_request(self, request):
        print('111 每次请求前会调用执行')

    def process_response(self, request, response):
        print('111 每次响应前会调用执行')

        return response


class TestMiddleWare2(MiddlewareMixin):

    def process_request(self, request):
        print('222 每次请求前会调用执行')

    def process_response(self, request, response):
        print('222 每次响应前会调用执行')

        return response

