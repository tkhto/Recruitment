from django.db import models
from Recruitment.utils.models import BaseModel
# Create your models here.
from django.contrib.auth.models import  AbstractUser

class Account(AbstractUser):
    gender = models.BooleanField(choices=((0, '女'), (1, '男')), blank=True, null=True, verbose_name='性别')
    mobile = models.CharField(max_length=15, unique=True, verbose_name='手机号')
    nic_name = models.CharField(max_length=15, blank=True, null=True, verbose_name='昵称')
    avatar = models.ImageField(upload_to="avatar", default="media/avatar/avatar.jpg", blank=True, null=True, verbose_name='头像')
    brithday = models.DateField(blank=True, null=True, verbose_name='生日')
    intro = models.CharField(max_length=100, blank=True, null=True, verbose_name='介绍')
    site = models.URLField(blank=True, null=True, verbose_name='个人主页')
    user_type = models.BooleanField(choices=((0, '普通用户'), (1, '企业用户')), default=0, verbose_name='用户类型')
    work_status_list = (
        (0, '已离职'),
        (1, '在职中'),
        (2, '保密'), 
        (3, '已退休')
    )
    work_status = models.SmallIntegerField(choices=work_status_list, default=1, blank=True, null=True, verbose_name='工作状态')
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Province(BaseModel):
    name = models.CharField(max_length=10, unique=True, verbose_name="名称")
    class Meta:
        verbose_name = '省份'
        verbose_name_plural = verbose_name

class JobBigCategory(BaseModel):
    name = models.CharField(max_length=32, verbose_name="名称")
    class Meta:
        verbose_name = '主分类'
        verbose_name_plural = verbose_name

class JobSubCategory(BaseModel):
    name = models.CharField(max_length=32, verbose_name="名称")
    parent = models.ForeignKey('JobBigCategory', verbose_name='所属主分类', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '子分类'
        verbose_name_plural = verbose_name

class Category(BaseModel):
    name = models.CharField(max_length=32, verbose_name="名称")
    parent = models.ForeignKey('JobSubCategory', verbose_name='所属子分类', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name