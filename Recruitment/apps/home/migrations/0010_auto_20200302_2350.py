# Generated by Django 2.2.8 on 2020-03-02 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200202_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='capital',
            field=models.IntegerField(help_text='单位：万人民币', verbose_name='注册资金'),
        ),
    ]