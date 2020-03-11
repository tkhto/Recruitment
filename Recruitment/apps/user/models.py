from django.db import models
from Recruitment.utils.models import BaseModel
# Create your models here.
from django.contrib.auth.models import AbstractUser

education_level = (
    (0, '小学'),
    (1, '初中'),
    (2, '高中'),
    (3, '专科'),
    (4, '本科'),
    (5, '硕士'),
    (6, '博士')
)

class Account(AbstractUser):
    work_status_list = (
        ("0", '已离职'),
        ("1", '在职中'),
        ("2", '保密'), 
        ("3", '已退休')
    )
    nic_name = models.CharField(max_length=15, blank=True, null=True, verbose_name='昵称')
    gender = models.CharField(max_length=1, choices=(("0", '女'), ("1", '男')), blank=True, null=True, verbose_name='性别')
    mobile = models.CharField(max_length=15, unique=True, verbose_name='手机号')
    avatar = models.ImageField(upload_to="avatar", default="media/avatar/avatar.jpg", blank=True, null=True, verbose_name='头像')
    birthday = models.DateField(blank=True, null=True, verbose_name='生日')
    intro = models.CharField(max_length=100, blank=True, null=True, verbose_name='介绍')
    site = models.URLField(blank=True, null=True, verbose_name='个人主页')
    user_type = models.CharField(max_length=1, choices=(("0", '求职者'), ("1", '招人者')), default=0, verbose_name='用户类型')
    city = models.CharField(max_length=32, blank=True, null=True, verbose_name="所在城市")
    companyId = models.CharField(max_length=32, blank=True, null=True, verbose_name="所属公司")
    selfPosition = models.CharField(max_length=32, blank=True, null=True, verbose_name="岗位")
    work_status = models.CharField(max_length=1, choices=work_status_list, default=1, blank=True, null=True, verbose_name='工作状态')
    # 教育经历
    graduatedSchool = models.CharField(max_length=60, blank=True, null=True, verbose_name="毕业院校")
    education = models.SmallIntegerField(choices=education_level, blank=True, null=True, verbose_name="学历")
    specialty = models.CharField(max_length=60, blank=True, null=True, verbose_name="专业")
    unifiedAdmission = models.CharField(max_length=1, choices=(("1", "统招"), ("0", "非统招")), blank=True, null=True, verbose_name="是否统招")
    admissionTime = models.DateField(verbose_name="入学时间", blank=True, null=True)
    graduationTime = models.DateField(verbose_name="毕业时间", blank=True, null=True)
    # 社交信息
    weibo = models.CharField(max_length=200, blank=True, null=True)
    github = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

class News(models.Model):
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE, verbose_name="用户id")
    content = models.TextField(verbose_name="内容")
    pub_date = models.DateTimeField(auto_now=True, verbose_name="发布日期")
    is_delete = models.BooleanField(choices=((1, '是'), (0, '否')), default=0, verbose_name="是否删除")
    class Meta:
        verbose_name = '动态'
        verbose_name_plural = verbose_name

class Like(models.Model):
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE, verbose_name="用户id")
    news_id = models.ForeignKey(to=News, on_delete=models.CASCADE, verbose_name="动态id")
    class Meta:
        verbose_name = '动态点赞'
        verbose_name_plural = verbose_name

class Article(models.Model):
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE, verbose_name="用户id")
    title = models.CharField(max_length=100, verbose_name="文章标题")
    tag = models.TextField(verbose_name="文章标签")
    html_code = models.TextField(verbose_name="html内容")
    md_code = models.TextField(verbose_name="markdown内容")
    pub_date = models.DateTimeField(auto_now=True, verbose_name="发布日期")
    update_date = models.DateTimeField(auto_now_add=True, verbose_name="更新日期")
    read_num = models.IntegerField(verbose_name="阅读量", default=0)
    is_delete = models.BooleanField(choices=((1, '是'), (0, '否')), default=0, verbose_name="是否删除")
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

class ArticleLike(models.Model):
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE, verbose_name="用户id")
    news_id = models.ForeignKey(to=News, on_delete=models.CASCADE, verbose_name="动态id")
    class Meta:
        verbose_name = '文章点赞'
        verbose_name_plural = verbose_name

class ArticleComments(models.Model):
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE, verbose_name="评论用户")
    parent = models.BigIntegerField(default=0, verbose_name="父级评论")
    reply = models.BigIntegerField(default=0, verbose_name="被回复评论")
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, verbose_name="文章")
    content = models.TextField(verbose_name="评论内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name

class Resume(models.Model):
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE, verbose_name="用户id")
    title = models.CharField(max_length=100, verbose_name="简历标题")
    html_code = models.TextField(verbose_name="html内容")
    md_code = models.TextField(verbose_name="markdown内容")
    pub_date = models.DateTimeField(auto_now=True, verbose_name="发布日期")
    update_date = models.DateTimeField(auto_now_add=True, verbose_name="更新日期")
    is_show = models.BooleanField(choices=((1, '是'), (0, '否')), default=1, verbose_name="是否展示")
    is_delete = models.BooleanField(choices=((1, '是'), (0, '否')), default=0, verbose_name="是否删除")
    class Meta:
        verbose_name = '简历'
        verbose_name_plural = verbose_name