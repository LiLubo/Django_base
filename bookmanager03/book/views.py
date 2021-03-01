from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from book.models import BookInfo
# Create your views here.


def create_book(request):

    book = BookInfo.objects.create(
        name='雪中悍刀行',
        pub_date='2018-1-1',
        readcount=1000,
    )
    return HttpResponse('create')


def shop(request, city_id, mobile):

    # # 验证参数的正确性
    # import re
    # if not re.match('\d{5}', shop_id):
    #     return HttpResponse('商店不存在')

    """
    查询字符串
    http://ip:port/path/path/?key=value&key1=value

    url 以 ? 为分隔
    ?之前是 请求路径
    ?之后是 查询字符串  类似于字典
    """
    # 获取查询字符串
    # <QueryDict: {'order': ['lalala']}>
    # QueryDict具有字典的特性 且可以一键多值
    # query_parms = request.GET
    # print(query_parms)
    #
    # # 当一键多值时，获取键值需要使用getlist(),否则只能得到最后一个键值
    # order = query_parms.getlist('order')
    #
    # # order = query_parms.get('order')
    # # order = query_parms['order']
    # print(order)
    print(city_id, mobile)
    return HttpResponse('禄波的小商店')


def register(request):

    # 获取表单数据
    data = request.POST
    print(data)
    return HttpResponse('register')


def json(request):

    # json 数据不能通过 request.POST 获取
    body = request.body
    print(body)
    # b'{\r\n    "name": "lubo",\r\n    "age": 18\r\n}'

    body_str = body.decode()
    print(body_str)
    # <class 'str'>
    # {
    #     "name": "lubo",
    #     "age": 18
    # }

    # JSON形式的字符串可以转换成字典
    import json
    body_dict = json.loads(body_str)
    print(body_dict)
    # {'name': 'lubo', 'age': 18}

    # 打印请求头
    # print(request.META)
    print(request.META['SERVER_PORT'])
    # 8000
    return HttpResponse('json')


def method(request):

    print(request.method)

    return HttpResponse('method')


from django.http import JsonResponse


def response(request):

    # HttpResponse的三个参数
    # content 响应体
    # content_type 响应体的数据类型
    # status 状态码(100-599)
    # 1xx
    # 2xx
    #   200 成功
    # 3xx
    # 4xx 请求有问题
    #   404 找不到页面 路由有问题
    #   403 禁止访问 权限有问题
    # 5xx
    # return HttpResponse('response', status=200)

    # 设置响应头
    # res = HttpResponse('response', status=200)
    #
    # res['name'] = 'lubo'
    #
    # return res

    # jsonResponse
    # 先导包
    # Json <--> dict
    info = {    # 字典
        'name': 'lubo',
        'gender': True,
    }
    friend = [  # 列表
        {
            'name': '小花',
            'mobile': 121341141,
        },
        {
            'name': '小草',
            'mobile': 1231435,
        }
    ]
    # data 是返回的响应数据，一般是字典类型
    # safe=True 表示data传的是字典数据
    # JsonResponse 可以把字典类型的数据转换成Json类型
    # safe=False 表示data传的不是字典数据

    # res = JsonResponse(data=friend, safe=False, charset='utf-8')
    # return res

    # json.loads json字符串转换成字典
    # json.dumps 字典转换成json字符串
    # import json
    # data = json.dumps(friend)
    # res = HttpResponse(data)
    # return res

    # 重定向
    return redirect('http://www.baidu.com')

