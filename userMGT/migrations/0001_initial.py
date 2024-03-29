# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-05 15:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='学生姓名')),
                ('age', models.IntegerField(default=0, verbose_name='学生年龄')),
            ],
        ),
        migrations.CreateModel(
            name='User_Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ID', models.IntegerField(default=0, verbose_name='用户id')),
                ('user_Name', models.CharField(default='', max_length=20, verbose_name='用户姓名')),
                ('user_Sex', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='用户性别')),
                ('user_Age', models.IntegerField(default='', verbose_name='用户年龄')),
                ('user_Num', models.IntegerField(default='', verbose_name='用户工号')),
                ('user_Image', models.ImageField(upload_to='media', verbose_name='用户头像')),
                ('user_Telnum', models.CharField(default='', max_length=10, verbose_name='用户电话号码')),
                ('user_Logtime', models.DateTimeField(default=datetime.datetime(2019, 7, 5, 15, 25, 33, 203358), null=True, verbose_name='用户最近登陆时间')),
                ('user_status', models.IntegerField(choices=[(1, '冻结状态'), (2, '解冻状态')], default=2, verbose_name='用户状态')),
                ('user_role', models.IntegerField(choices=[(1, '超级管理员'), (2, '高级管理员'), (3, '普通管理员')], default=3, verbose_name='用户角色')),
                ('user_AccountName', models.CharField(default='', max_length=30, verbose_name='用户的账户名称')),
                ('user_Password', models.CharField(default='', max_length=10, verbose_name='用户的账户密码')),
                ('user_Address', models.CharField(default='', max_length=60, verbose_name='用户联系地址')),
                ('user_Tips', models.CharField(default='', max_length=60, verbose_name='用户备注信息')),
                ('user_CreateTime', models.DateTimeField(default=datetime.datetime(2019, 7, 5, 15, 25, 33, 203358), null=True, verbose_name='用户创建时间')),
                ('user_Summary', models.TextField(default='', verbose_name='用户概述')),
            ],
        ),
    ]
