# Generated by Django 2.2.8 on 2020-02-02 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200202_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='createTime',
        ),
    ]
