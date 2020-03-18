from django.db import models
from Recruitment.utils.models import BaseModel

# Create your models here.
class Province(BaseModel):
    name = models.CharField(max_length=10, unique=True, verbose_name="名称")
    class Meta:
        verbose_name = '省份'
        verbose_name_plural = verbose_name

class Banners(BaseModel):
    title = models.CharField(max_length=50, verbose_name="标题")
    link = models.URLField(verbose_name="跳转连接")
    image = models.ImageField(verbose_name="图片路径")
    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

class JobBigCategory(BaseModel):
    name = models.CharField(max_length=32, verbose_name="名称")
    class Meta:
        verbose_name = '职位主分类'
        verbose_name_plural = verbose_name

class JobSubCategory(BaseModel):
    name = models.CharField(max_length=32, verbose_name="名称")
    parent = models.ForeignKey('JobBigCategory', related_name="sub_category", verbose_name='所属主分类', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '职位子分类'
        verbose_name_plural = verbose_name

class Category(BaseModel):
    name = models.CharField(max_length=32, verbose_name="名称")
    parent = models.ForeignKey('JobSubCategory',related_name="category", verbose_name='所属子分类', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '职位分类'
        verbose_name_plural = verbose_name

class Company(BaseModel):
    companySizeChoices = (
        (0, '15-50'),
        (1, '50-150'),
        (2, '150-500'),
        (3, '500-2000'),
        (4, '2000以上'),
    )
    companyId = models.CharField(max_length=32, verbose_name="公司id")
    companyShortName = models.CharField(max_length=100, verbose_name="公司简称")
    companyFullName = models.CharField(max_length=100, verbose_name="公司全称")
    companyLogo = models.ImageField(upload_to="companyLogo", verbose_name="公司Logo")
    companySize = models.SmallIntegerField(choices=companySizeChoices, verbose_name="公司规模")
    industryField = models.CharField(max_length=100, verbose_name="经营领域")
    financeStage = models.CharField(max_length=32, verbose_name="是否需要融资")
    companyLabelList = models.CharField(max_length=200, verbose_name="公司标签", help_text="多个标签之间用逗号分隔")
    businessLicense = models.ImageField(upload_to="license", blank=True, null=True, verbose_name="营业执照")
    capital = models.IntegerField(verbose_name="注册资金", help_text="单位：万人民币")
    createPerson = models.CharField(max_length=32, verbose_name="创始人")
    createPersonIntro = models.TextField(verbose_name="创始人简介")
    createPersonAvatar = models.ImageField(upload_to="createPerson", null=True, blank=True, verbose_name="创始人头像")
    signature = models.CharField(max_length=40, verbose_name="公司签名")
    companyIntro = models.TextField(verbose_name="公司介绍")
    createTime = models.DateField(verbose_name="公司创建时间")
    companySite = models.URLField(null=True, blank=True, verbose_name="公司首页")
    legalRepresentative = models.CharField(max_length=32, verbose_name="法人代表")
    legalize = models.BooleanField(choices=((0, '未认证'), (1, '已认证')), verbose_name="是否经过认证", default=0)
    latitude = models.CharField(max_length=32, verbose_name="纬度")
    longitude = models.CharField(max_length=32, verbose_name="经度")
    class Meta:
        verbose_name = '公司列表'
        verbose_name_plural = verbose_name

    @property
    def company_size(self):
        return self.get_companySize_display()


class Position(BaseModel):
    education_level = (
        (0, '小学'),
        (1, '初中'),
        (2, '高中'),
        (3, '专科'),
        (4, '本科'),
        (5, '硕士'),
        (6, '博士')
    )
    positionName = models.CharField(max_length=200, verbose_name="职位名称")
    companyId = models.CharField(max_length=32, verbose_name="所属公司")
    publisher = models.ForeignKey("user.Account", related_name="pub_position", verbose_name="发布者", on_delete=models.CASCADE)
    firstType = models.CharField(max_length=100, verbose_name="第一分类", help_text="多个分类之间用逗号分隔，例：销售类")
    secondType = models.CharField(max_length=100, verbose_name="第二分类", help_text="多个分类之间用逗号分隔，例：销售管理")
    thirdType = models.CharField(max_length=100, verbose_name="第三分类", help_text="多个分类之间用逗号分隔，例：大客户销售管理")
    skillLabels = models.CharField(max_length=100, verbose_name="技术标签", help_text="多个分类之间用逗号分隔")
    positionLabels = models.CharField(max_length=100, verbose_name="职位标签", help_text="多个分类之间用逗号分隔")
    industryLabels = models.CharField(max_length=100, verbose_name="行业标签", help_text="多个分类之间用逗号分隔")
    positionIntro = models.TextField(verbose_name="职位描述")
    city = models.CharField(max_length=32, verbose_name="工作地点")
    district = models.CharField(max_length=32, blank=True, null=True, verbose_name="工作地点-区")
    salary = models.CharField(max_length=32, verbose_name="月薪", help_text="例：10k-20k")
    workYear = models.CharField(max_length=32, verbose_name="工作时间", help_text="例：5-10")
    jobNature = models.SmallIntegerField(choices=((0, '兼职'), (1, '全职')), verbose_name="工作类型", help_text="兼职/全职")
    education = models.SmallIntegerField(choices=education_level, verbose_name="学历")
    isSchoolJob = models.BooleanField(verbose_name="是否为校招")
    positionAdvantage = models.CharField(max_length=200, blank=True, null=True, verbose_name="职位优势", help_text="多个之间用逗号分隔")
    subwayLine = models.CharField(max_length=100, blank=True, null=True, verbose_name="地铁", help_text="例：1号线")
    stationName = models.CharField(max_length=32, blank=True, null=True, verbose_name="站名", help_text="例：西单站")
    class Meta:
        verbose_name = '职位列表'
        verbose_name_plural = verbose_name