# 李禄波
# 2021/2/25 10:32

from django.urls import path
from .views import index

# 要访问子应用里的路由需要通过 工程路由 + 子应用路由
# 固定写法 urlpatterns = []
urlpatterns = [
    # path(路由, 视图函数名)
    path('index/', index)
]