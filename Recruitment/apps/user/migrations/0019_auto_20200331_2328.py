# Generated by Django 2.2.8 on 2020-03-31 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200328_1451'),
        ('user', '0018_auto_20200331_2251'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='deliveryrecord',
            unique_together={('user', 'position')},
        ),
    ]
