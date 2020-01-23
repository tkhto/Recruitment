from django.db import models
from Recruitment.utils.models import BaseModel

# Create your models here.
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
    parent = models.ForeignKey('JobBigCategory',related_name="sub_category", verbose_name='所属主分类', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '子分类'
        verbose_name_plural = verbose_name

class Category(BaseModel):
    name = models.CharField(max_length=32, verbose_name="名称")
    parent = models.ForeignKey('JobSubCategory',related_name="category", verbose_name='所属子分类', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name