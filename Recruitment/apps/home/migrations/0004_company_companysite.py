# Generated by Django 2.2.8 on 2020-02-01 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200131_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='companySite',
            field=models.URLField(blank=True, null=True, verbose_name='公司首页'),
        ),
    ]
