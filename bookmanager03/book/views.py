from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
# Create your views here.


def create_book(request):

    book = BookInfo.objects.create(
        name='雪中悍刀行',
        pub_date='2018-1-1',
        readcount=1000,
    )
    return HttpResponse('create')
