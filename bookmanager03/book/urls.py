# 李禄波
# 2021/2/27 17:02
from django.urls import path
from book.views import create_book
urlpatterns = [
    path('create/', create_book),
]
