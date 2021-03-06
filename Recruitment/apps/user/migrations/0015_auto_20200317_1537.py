# Generated by Django 2.2.8 on 2020-03-17 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20200310_1427'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='NewsLike',
        ),
        migrations.CreateModel(
            name='NewsComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.BigIntegerField(default=0, verbose_name='父级评论')),
                ('reply', models.BigIntegerField(default=0, verbose_name='被回复评论')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Article', verbose_name='文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论用户')),
            ],
            options={
                'verbose_name': '动态评论',
                'verbose_name_plural': '动态评论',
            },
        ),
    ]
