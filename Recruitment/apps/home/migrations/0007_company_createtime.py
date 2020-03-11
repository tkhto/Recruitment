# Generated by Django 2.2.8 on 2020-02-02 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_company_createtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='createTime',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='公司创建时间'),
            preserve_default=False,
        ),
    ]
