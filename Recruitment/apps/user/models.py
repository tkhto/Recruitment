from django.db import models

# Create your models here.
from django.contrib.auth.models import  AbstractUser

class Account(AbstractUser):
    gender = models.BooleanField(choices=((0, '女'), (1, '男')), blank=True, null=True, verbose_name='性别')
    mobile = models.CharField(max_length=15, unique=True, verbose_name='手机号')
    nic_name = models.CharField(max_length=15, blank=True, null=True, verbose_name='昵称')
    avatar = models.ImageField(upload_to="avatar", blank=True, null=True, verbose_name='头像')
    brithday = models.DateField(blank=True, null=True, verbose_name='生日')
    intro = models.CharField(max_length=100, blank=True, null=True, verbose_name='介绍')
    site = models.URLField(blank=True, null=True, verbose_name='个人主页')
    user_type = models.BooleanField(choices=((0, '普通用户'), (1, '企业用户')), verbose_name='用户类型')
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


class Province(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name="名称")
    order = models.SmallIntegerField(verbose_name="序号")
    status = models.BooleanField(choices=((0, True), (1, False)), verbose_name="是否上线")
    class Meta:
        verbose_name = '省份'
        verbose_name_plural = verbose_name

        """
        "北京","上海","天津","重庆","河北","山西","河南","辽宁","吉林",
					"黑龙江","内蒙古","江苏","山东","安徽","浙江","福建","湖北","湖南","广西","广东",
					"江西","四川","海南","贵州","云南","西藏","陕西","甘肃","青海","宁夏","新疆",
					"港澳","台湾","钓鱼岛","海外"
        """