from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserInfo(AbstractUser):
    nid = models.AutoField(primary_key=True)
    tel = models.CharField(verbose_name='手机号', max_length=64, null=True, blank=True)
    addr = models.CharField(max_length=64, verbose_name='地址信息', null=True, blank=True)
    name = models.CharField(max_length=64, verbose_name='姓名', null=True, blank=True)
    sex = models.CharField(max_length=64, verbose_name='性别', null=True, blank=True)
    age = models.IntegerField(verbose_name='年龄', null=True, blank=True)
    birth = models.CharField(max_length=64, verbose_name='出生日期', null=True, blank=True)
    role = models.CharField(verbose_name='用户角色', max_length=16, default='普通用户')

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name_plural = '用户信息'


class Product(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='产品名称', max_length=128, null=True, blank=True)
    title = models.CharField(verbose_name='产品中文名', max_length=128)
    logo = models.CharField(verbose_name='产品logo', max_length=256, null=True)
    cover = models.CharField(verbose_name='产品封面', max_length=256, null=True)
    description = models.TextField(verbose_name='产品简介')
    subDescription = models.TextField(verbose_name='产品描述')
    link = models.CharField(verbose_name='产品链接', max_length=128, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = '产品信息'


class Job(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='岗位名称', max_length=256)
    description = models.TextField(verbose_name='岗位描述')
    requirement = models.TextField(verbose_name='岗位需求')

    category = models.ForeignKey(
        to='Category',
        to_field='nid',
        on_delete=models.CASCADE,
        verbose_name='种类',
        null=True,
        blank=True,
    )

    city = models.ForeignKey(
        to='City',
        to_field='nid',
        on_delete=models.CASCADE,
        verbose_name='城市',
        null=True,
        blank=True,
    )

    recruit_type = models.ForeignKey(
        to='RecruitType',
        to_field='nid',
        on_delete=models.CASCADE,
        verbose_name='类型',
        null=True,
        blank=True,
    )

    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = '岗位'


class Category(models.Model):
    nid = models.AutoField(primary_key=True)
    code = models.CharField(verbose_name='种类编号', max_length=128, null=True, blank=True)
    name = models.CharField(verbose_name='种类名称', max_length=64)
    en_name = models.CharField(verbose_name='category', max_length=64)
    image = models.CharField(verbose_name='图片', max_length=128, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = '种类'


class City(models.Model):
    nid = models.AutoField(primary_key=True)
    code = models.CharField(verbose_name='城市编号', max_length=128, null=True, blank=True)
    name = models.CharField(verbose_name='城市名称', max_length=64)
    en_name = models.CharField(verbose_name='city', max_length=64)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = '城市'


class RecruitType(models.Model):
    nid = models.AutoField(primary_key=True)
    type = models.CharField(verbose_name='岗位类型', max_length=64)
    en_type = models.CharField(verbose_name='type', max_length=64)

    def __str__(self):
        return str(self.type)

    class Meta:
        verbose_name_plural = '类型'
