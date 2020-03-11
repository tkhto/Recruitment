# Generated by Django 2.2.8 on 2020-02-02 13:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_company_companysite'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='createPersonAvatar',
            field=models.ImageField(blank=True, null=True, upload_to='createPerson', verbose_name='创始人头像'),
        ),
        migrations.AddField(
            model_name='company',
            name='createTime',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='公司创建时间'),
            preserve_default=False,
        ),
    ]
