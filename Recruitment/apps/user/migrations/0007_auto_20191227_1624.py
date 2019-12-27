# Generated by Django 2.2.8 on 2019-12-27 08:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20191226_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobBigCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.IntegerField(verbose_name='显示顺序')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否上架')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
            ],
            options={
                'verbose_name': '主分类',
                'verbose_name_plural': '主分类',
            },
        ),
        migrations.RemoveField(
            model_name='province',
            name='order',
        ),
        migrations.RemoveField(
            model_name='province',
            name='status',
        ),
        migrations.AddField(
            model_name='province',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='添加时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='province',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='逻辑删除'),
        ),
        migrations.AddField(
            model_name='province',
            name='is_show',
            field=models.BooleanField(default=False, verbose_name='是否上架'),
        ),
        migrations.AddField(
            model_name='province',
            name='orders',
            field=models.IntegerField(default=1, verbose_name='显示顺序'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='province',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.CreateModel(
            name='JobSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.IntegerField(verbose_name='显示顺序')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否上架')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.JobBigCategory', verbose_name='所属主分类')),
            ],
            options={
                'verbose_name': '子分类',
                'verbose_name_plural': '子分类',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.IntegerField(verbose_name='显示顺序')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否上架')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.JobSubCategory', verbose_name='所属子分类')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
    ]
