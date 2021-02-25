# 李禄波
# 2021/2/25 17:01

from django.urls import path
from .views import index

urlpatterns = [
    path('home/', index)
]
