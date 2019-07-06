# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-05 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='authorityMGT_Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_Name', models.CharField(default='', max_length=50, verbose_name='角色名')),
                ('scene_ID', models.IntegerField(default=0, verbose_name='场景ID')),
                ('scene_Authority', models.IntegerField(choices=[(1, '查看'), (2, '控制'), (3, '告警处理'), (4, '告警确认'), (5, '门禁审批')], default=1, verbose_name='场景权限')),
            ],
        ),
        migrations.CreateModel(
            name='authorityMGT_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_Name', models.CharField(default='', max_length=50, verbose_name='角色名')),
                ('user_ID', models.IntegerField(default=0, verbose_name='用户ID')),
            ],
        ),
    ]
