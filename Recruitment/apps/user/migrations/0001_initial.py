# Generated by Django 2.2.8 on 2020-01-30 15:49

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nic_name', models.CharField(blank=True, max_length=15, null=True, verbose_name='昵称')),
                ('gender', models.BooleanField(blank=True, choices=[(0, '女'), (1, '男')], null=True, verbose_name='性别')),
                ('mobile', models.CharField(max_length=15, unique=True, verbose_name='手机号')),
                ('avatar', models.ImageField(blank=True, default='media/avatar/avatar.jpg', null=True, upload_to='avatar', verbose_name='头像')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('intro', models.CharField(blank=True, max_length=100, null=True, verbose_name='介绍')),
                ('site', models.URLField(blank=True, null=True, verbose_name='个人主页')),
                ('user_type', models.BooleanField(choices=[(0, '求职者'), (1, '招人者')], default=0, verbose_name='用户类型')),
                ('city', models.CharField(blank=True, max_length=32, null=True, verbose_name='所在城市')),
                ('companyId', models.CharField(blank=True, max_length=32, null=True, verbose_name='所属公司')),
                ('selfPosition', models.CharField(blank=True, max_length=32, null=True, verbose_name='岗位')),
                ('graduatedSchool', models.CharField(blank=True, max_length=60, null=True, verbose_name='毕业院校')),
                ('education', models.SmallIntegerField(blank=True, choices=[(0, '小学'), (1, '初中'), (2, '高中'), (3, '专科'), (4, '本科'), (5, '硕士'), (6, '博士')], null=True, verbose_name='学历')),
                ('specialty', models.CharField(blank=True, max_length=60, null=True, verbose_name='专业')),
                ('unifiedAdmission', models.BooleanField(blank=True, choices=[(1, '统招'), (0, '非统招')], null=True, verbose_name='是否统招')),
                ('admissionTime', models.DateField(blank=True, null=True, verbose_name='入学时间')),
                ('graduationTime', models.DateField(blank=True, null=True, verbose_name='毕业时间')),
                ('work_status', models.SmallIntegerField(blank=True, choices=[(0, '已离职'), (1, '在职中'), (2, '保密'), (3, '已退休')], default=1, null=True, verbose_name='工作状态')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
