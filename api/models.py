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


class Resume(models.Model):
    nid = models.AutoField(primary_key=True)
    user_id = models.IntegerField(verbose_name='用户id')
    name = models.CharField(verbose_name='用户姓名', max_length=256)
    phone = models.CharField(verbose_name='联系方式', max_length=256)
    email = models.CharField(verbose_name='邮箱', max_length=256)
    school = models.CharField(verbose_name='学校', max_length=256)
    degree = models.CharField(verbose_name='学历', max_length=256)
    profession = models.CharField(verbose_name='专业', max_length=256, null=True, blank=True)
    duration = models.CharField(verbose_name='持续时间', max_length=256)

    work_info = models.ManyToManyField(
        to='WorkInfo',
        verbose_name='工作经历'
    )
    project_info = models.ManyToManyField(
        to='ProjectInfo',
        verbose_name='项目经历'
    )
    change_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = '简历'


class WorkInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    company = models.CharField(verbose_name='公司名称', max_length=256)
    position = models.CharField(verbose_name='职位', max_length=256)
    duration = models.CharField(verbose_name='持续时间', max_length=256)
    description = models.TextField(verbose_name='描述', null=True, blank=True)
    types = models.CharField(verbose_name='工作类别', default='正式', max_length=256)

    def __str__(self):
        return str(self.company)

    class Meta:
        verbose_name_plural = '工作经历'


class ProjectInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='项目名称', max_length=256)
    role = models.CharField(verbose_name='项目角色', max_length=256)
    duration = models.CharField(verbose_name='持续时间', max_length=256)
    link = models.CharField(verbose_name='项目链接', max_length=256, null=True)
    description = models.TextField(verbose_name='描述')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = '项目经历'


class Delivery(models.Model):
    user_id = models.IntegerField(verbose_name='用户id')
    job_id = models.IntegerField(verbose_name='岗位id')
    status_choice = (
        ('简历筛选', '简历筛选'),
        ('待检阅', '待检阅'),
        ('面试中', '面试中'),
        ('待签约', '待签约'),
        ('已结束', '已结束')
    )
    status = models.CharField(verbose_name='投递状态', max_length=256, default='简历筛选', choices=status_choice)
    create_date = models.DateTimeField(verbose_name='投递时间', auto_now_add=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name_plural = '投递记录'


class ResumeFile(models.Model):
    nid = models.AutoField(primary_key=True)
    user_id = models.IntegerField(verbose_name='用户id')
    file = models.FileField(verbose_name='简历文件', upload_to='resume/')
    create_date = models.DateTimeField(verbose_name='上传时间', auto_now_add=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name_plural = '简历文件'
