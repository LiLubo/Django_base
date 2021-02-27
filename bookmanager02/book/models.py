from django.db import models
from django.http import HttpResponse

# Create your models here.
"""
1.模型类 需要继承自 models.Model
2.属性    属性名 = models.类型（选项）
    1）id 系统会自动生成
       属性名对应的就是字段名
       属性名不要使用python关键字
       不要使用连续的下划线
    2）类型 MySQL的类型
    3）选项 是否有默认值,是否唯一,是否为空
            CharField 必须设置max_length
3.改变表的名称
    默认表的名称是:子应用名_类名 都是小写
    修改表的名字(见代码)
SQL 语句：
    create table qq_user(
        id int,
        name varchar(10) not null default '',
        )
"""


class BookInfo(models.Model):

    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    # 在一对多的关系模型中 系统会自动添加一个 关联模型类名（小写）_set的字段
    # peopleinfo_set = [PeopleInfo对象, PeopleInfo对象......]
    #
    def __str__(self):

        return self.name

    # 修改表的名字
    class Meta:     # 固定写法
        db_table = 'bookinfo'
        verbose_name = '书籍管理'   # admin站点使用


class PeopleInfo(models.Model):

    # 枚举类型
    # 定义有序字典
    GENDER_NAME = (
        (1, 'male'),
        (2, 'female')
    )

    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_NAME, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    # 外键
    # 系统会自动为外键添加下划线_id
    # 外键的级联操作
    #
    # 主表 和 从表   1 对 多
    # 主表的一条数据如果删除了,可以进行以下操作
    #
    # CASCADE级联，删除主表数据时连通一起删除外键表中数据
    # PROTECT保护，通过抛出ProtectedError异常，来阻止删除主表中被外键应用的数据
    # SET_NULL设置为NULL，仅在该字段null = True允许为null时可用
    # SET_DEFAULT设置为默认值，仅在该字段设置了默认值时可用
    # SET() 设置为特定值或者调用特定方法
    # DO_NOTHING不做任何操作，如果数据库前置指明级联性，此选项会抛出IntegrityError异常

    book = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'peopleinfo'












