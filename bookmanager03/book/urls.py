# 李禄波
# 2021/2/27 17:02
from django.urls import path
from book.views import *


# 1.自定义转换器
class MobileConverter:
    # 验证数据的关键是：正则
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据给视图函数
    def to_python(self, value):
        return int(value)

    # 见匹配结果用于反向解析传值时使用
    def to_ulr(self, value):
        return str(value)
# 2.注册转换器
from django.urls.converters import register_converter
# 该函数的两个参数：
# converter 转换器的类名
# type_name 转换器的名字
register_converter(MobileConverter, 'phone')


urlpatterns = [
    path('create/', create_book),

    # 获取路径中的参数
    # <转换器名字:变量名>
    # 转换器会对变量数据进行正则的验证
    path('<int:city_id>/<phone:mobile>/', shop),

    path('register/', register),

    path('json/', json),

    path('method/', method),
]
