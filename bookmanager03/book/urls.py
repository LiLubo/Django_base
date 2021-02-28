# 李禄波
# 2021/2/27 17:02
from django.urls import path
from book.views import *
urlpatterns = [
    path('create/', create_book),

    # 获取路径中的参数
    path('<city_id>/<shop_id>/', shop),

    path('register/', register)
]
