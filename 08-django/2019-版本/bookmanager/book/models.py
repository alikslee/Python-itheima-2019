from django.db import models


# Create your models here.

# 准备书籍列表信息的模型类
class Book(models.Model):
    name = models.CharField(max_length=64, verbose_name='名称')
    pub_date = models.DateField(verbose_name='发布日期', null=True)
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'book'  # 指明数据库表名
        verbose_name = '图书'  # 指明数据库表名

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name


class People(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )

    name = models.CharField(max_length=64, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='名称')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='图书')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'people'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name














