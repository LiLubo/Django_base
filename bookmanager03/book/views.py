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


'''
第一次请求，携带查询字符串
http://127.0.0.1:8000/set_cookie/?username=lubo&password=1234567
服务器接收到请求之后，获取username,设置cookie信息，cookie信息包括username
浏览器接收到服务器的响应之后应该把cookie保存起来

第二次 及其之后的请求，在访问http://127.0.0.1:8000这个域名的时候都会携带cookie信息
服务器就可以读取cookie信息，从而判断用户的身份
'''


def set_cookie(request):

    # 1.获取查询字符串数据
    username = request.GET.get('username')
    password = request.GET.get('password')

    # 2.服务器设置cookie信息
    # 响应对象.set_cookie(参数1，参数2，参数3)
    # 参数1：key   参数2：value(只能是字符串)   参数3：cookie过期时间（秒数）
    res = HttpResponse('set_cookie')
    # 默认过期时间为当前会话结束时，即浏览器关闭
    res.set_cookie('name', username, max_age=3600)

    res.set_cookie('password', password)

    # 删除cookie
    res.delete_cookie('password')

    return res


def get_cookie(request):

    # 获取cookie
    print(request.COOKIES)
    # {'name': 'lubo'}
    name = request.COOKIES.get('name')
    password = request.COOKIES.get('password')

    return HttpResponse((name, password))


"""
Session(保存在服务端,依赖于cookie)
第一次请求 http://127.0.0.1:8000/set_session/?username=lubo 
服务器端设置session信息 
服务器同时会生成一个sessionid的信息
浏览器接收到这个信息之后，会把cookie数据保存起来

2.第二次及其之后的请求，都会携带这个sessionid，服务器会验证sessionid，没有问题则会读取相应的数据实现业务逻辑
"""


def set_session(request):

    # 1.获取用户信息
    username = request.GET.get('username')

    # 2.设置session信息
    # 假如通过模型查询获取到了用户的信息
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username

    # clear 删除session中的数据 但是保留key
    # request.session.clear()

    # flash 删除session中的数据 都不保留
    # request.session.flush()

    # 设置session有效期
    request.session.set_expiry(100)

    return HttpResponse('set_session')


def get_session(request):

    user_id = request.session.get('user_id')
    username = request.session.get('username')

    content = '{}, {}'.format(user_id, username)
    return HttpResponse(content)


''' 类视图 '''


# 一个函数处理两种逻辑
def login(request):
    print(request.method)

    if request.method == 'GET':

        return HttpResponse('get 逻辑')

    elif request.method == 'POST':

        return HttpResponse('post 逻辑')

    return HttpResponse('login')


''' 
类视图的定义
1.继承自View
2.类视图中的方法是通过http方法小写来区分不同的请求方式
from django.views import View
class 类视图名字(View):
    def get(self, request):
    
        return HttpResponse('xxx')
        
    def http_method_lower(self, request):
    
        return HttpResponse('xxx')

'''
from django.views import View


class LoginView(View):

    def get(self, request):

        return HttpResponse('get')

    def post(self, request):

        return HttpResponse('post')


"""
打开我的订单/个人中心页面
已经登录 则正常访问
如果未登录 则跳转到登录界面

定义我的订单类视图
判断用户是否已经登录
    ·标识符实现
    ·多继承实现
        ·LoginRequiredMixin 
            ·导包：from django.contrib.auth.mixins import LoginRequiredMixin
            ·该类的内部会进行用户是否登录(admin站点)的判断
            如登录成功则会打开相应页面，否则会跳转到系统的 accounts/login/?next=/order/ 页面中
"""

# LoginRequiredMixin 作用是实现只有已登录的用户才能访问订单页面
from django.contrib.auth.mixins import LoginRequiredMixin


# 注意此处需要先继承LoginRequiredMixin
class OrderView(LoginRequiredMixin, View):

    def get(self, request):

        # # 登录标识符
        # is_login = False
        #
        # if not is_login:
        #     return HttpResponse('请登录,跳转至登录界面')

        return HttpResponse('GET 我的订单页面，需登录才能使用')

    def post(self, request):
        return HttpResponse('POST 我的订单页面，需登录才能使用')
