from django.shortcuts import render

# Create your views here.
"""
视图
    就是python函数

两个要求：
        1.视图函数的第一个参数就是接收请求,这个请求指的就是HttpRequest的类对象
        2.必须返回一个响应
"""

# request
from django.http import HttpRequest
from django.http import HttpResponse


# 期望用户输入 http://127.0.0.1:8000/index 来访问视图函数
def index(request):

    # return HttpResponse('OK')

    # render参数：---->渲染模板
    # 1.request 请求
    # 2.templates 模板名字
    # 3.context=None 上下文

    context = {
        'name': 'I am Ali'
    }

    return render(request, 'book/index.html', context)
