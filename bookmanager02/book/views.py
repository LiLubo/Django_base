from django.http import HttpResponse
from django.shortcuts import render
from book.models import *
# Create your views here.


def index(request):

    # 在这里实现增删改查
    return HttpResponse(BookInfo.objects.all())


""" 增加数据 """
# 方式1:
book = BookInfo(
    name='月牙',
    pub_date='2020-1-1',
    readcount=100
)
# 该方式必须要调用 对象名.save() 方法才能将数据添加到数据库中
book.save()

# 方式2：
# objects --- 代理 从而实现增删改查
BookInfo.objects.create(
    name='月圆',
    pub_date='2021-1-1',
    readcount=1000,
)


""" 修改数据 """
# 方式1：
book = BookInfo.objects.get(id=3)  # 相当于 select * from BookInfo where id = 6
book.name = '弦月'
# 该方式必须通过 save() 方法来将修改后的内容提交到数据库
book.save()

# 方式2：
# filter 过滤
BookInfo.objects.filter(id=3).update(
    name='上弦月',
    commentcount=888,
)


""" 删除数据 """
# 物理删除 和 逻辑删除（标记位）
# 方式1：
BookInfo.objects.get(id=6).delete()

# 方式2：
BookInfo.objects.filter(id=5).delete()


""" 查询数据 """
# 基本查询
# get查询单一结果，如果不存在会抛出模型类.DoesNotExist异常
try:

    BookInfo.objects.get(id=2)

except Exception as e:
    print(e, '未找到相应信息')

# all查询多个结果
BookInfo.objects.all()

# count查询结果数量
BookInfo.objects.all().count()  # 等价 BookInfo.objects.count()

# 过滤查询
# 格式：模型类名.objects.filter(属性名_运算符=值)
# 格式：模型类名.objects.exclude(属性名_运算符=值)
# 格式：模型类名.objects.get(属性名_运算符=值)

# 查询编号为1的图书
book = BookInfo.objects.get(id=1)  # 等价于BookInfo.objects.get(id__exact=1)
BookInfo.objects.get(pk=1)  # pk: primary key 主键
BookInfo.objects.filter(id=1)  # 该方式获取的是一个列表

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='月')

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=(1, 3, 5))

# 查询编号大于3的图书
# 大于 gt
# 大于等于 gte
# 小于 lt
# 小于等于 lte
BookInfo.objects.filter(id__gt=3)

# 查询编号不等于3的图书
BookInfo.objects.exclude(id=3)

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')


# F对象
# 两个属性的比较
# 语法形式： 模型类名.objects.filter(属性名__运算符=F('第二个属性名'))
# 查询阅读量大于评论量的图书
from django.db.models import F
BookInfo.objects.filter(readcount__gte=F('commentcount'))
# 查询阅读量大于评论量两倍的图书
BookInfo.objects.filter(readcount__gte=F('commentcount')*2)

# Q对象
# 并且查询
# 查询阅读量大于20 且编号小于3的图书
BookInfo.objects.filter(readcount__gt=20, id__lt=3)
# 等价于BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)

# 或者查询
# 或者语法： 模型类名.objects.filter(Q(属性名_运算符=值)|Q(属性名_运算符=值)|...)
# 并且语法： 模型类名.objects.filter(Q(属性名_运算符=值)&Q(属性名_运算符=值)|...)
# 非语法： 模型类名.objects.filter(~Q(属性名_运算符=值))
# 查询阅读量大于20或者编号小于3的图书
from django.db.models import Q
BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))

# 查询id不为3的图书
BookInfo.objects.filter(~Q(id=3))


""" 聚合函数 """
from django.db.models import Sum, Max, Min, Avg, Count
# 模型类名.objects.aggregate(xxx('字段名'))
# 求阅读量之和
BookInfo.objects.aggregate(Sum('readcount'))

""" 排序 """
# 根据阅读量进行排序
BookInfo.objects.all().order_by('readcount')






