# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-05 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device_Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarm_Light', models.IntegerField(choices=[(1, '开启'), (2, '关闭')], default=2, verbose_name='报警灯')),
                ('alarm_clock', models.IntegerField(choices=[(1, '开启'), (2, '关闭')], default=2, verbose_name='报警器')),
                ('water_pump', models.IntegerField(choices=[(1, '开启'), (2, '关闭')], default=1, verbose_name='水泵')),
                ('fan', models.IntegerField(choices=[(1, '开启'), (2, '关闭')], default=1, verbose_name='风机')),
                ('LED', models.IntegerField(choices=[(1, '开启'), (2, '关闭')], default=1, verbose_name='LED显示屏')),
            ],
        ),
        migrations.CreateModel(
            name='Environment_Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(default='', verbose_name='温度')),
                ('humidity', models.FloatField(default='', verbose_name='湿度')),
                ('carbondioxide', models.FloatField(default='', verbose_name='二氧化碳')),
                ('pm', models.FloatField(default='', verbose_name='PM2.5')),
                ('candela', models.FloatField(default='', verbose_name='光照强度')),
            ],
        ),
        migrations.CreateModel(
            name='Fire_Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smoke', models.FloatField(default='', verbose_name='烟雾')),
                ('CH4', models.FloatField(default='', verbose_name='甲烷')),
                ('fire', models.FloatField(default='', verbose_name='火光')),
            ],
        ),
        migrations.CreateModel(
            name='Safe_Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invade_Examine', models.IntegerField(choices=[(1, '入侵'), (2, '安全')], default=2, verbose_name='入侵检测')),
                ('access_Status', models.IntegerField(choices=[(1, '在线'), (2, '离线')], default=1, verbose_name='门禁状态')),
            ],
        ),
        migrations.CreateModel(
            name='Scene_Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitor_ID', models.IntegerField(default=0, verbose_name='监控表的id')),
                ('environment_Monitor', models.IntegerField(choices=[(1, '在线'), (2, '离线')], default=1, verbose_name='环境监控')),
                ('fire_Monitor', models.IntegerField(choices=[(1, '在线'), (2, '离线')], default=1, verbose_name='消防监控')),
                ('safe_Monitor', models.IntegerField(choices=[(1, '在线'), (2, '离线')], default=1, verbose_name='安防监控')),
                ('device_Num', models.IntegerField(default=0, verbose_name='设备数量')),
            ],
        ),
        migrations.AddField(
            model_name='safe_monitor',
            name='safe_Monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sceneMOT.Scene_Monitor'),
        ),
        migrations.AddField(
            model_name='fire_monitor',
            name='fire_Monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sceneMOT.Scene_Monitor'),
        ),
        migrations.AddField(
            model_name='environment_monitor',
            name='environment_Monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sceneMOT.Scene_Monitor'),
        ),
        migrations.AddField(
            model_name='device_monitor',
            name='device_Num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sceneMOT.Scene_Monitor'),
        ),
    ]
