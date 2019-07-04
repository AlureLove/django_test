from django.db import models
import datetime
# Create your models here.
class Scene_Monitor(models.Model):
    STATUS = [
        (1, '在线'),
        (2, '离线')
    ]

    monitor_ID = models.IntegerField(default=0, verbose_name='监控表的id')
    environment_Monitor = models.IntegerField(choices=STATUS, default=1, verbose_name='环境监控')
    fire_Monitor = models.IntegerField(choices=STATUS, default=1, verbose_name='消防监控')
    safe_Monitor = models.IntegerField(choices=STATUS, default=1, verbose_name='安防监控')
    device_Num = models.IntegerField(default=0, verbose_name='设备数量')

class Environment_Monitor(models.Model):
    environment_Monitor = models.ForeignKey(Scene_Monitor, on_delete=models.CASCADE)
    temperature = models.FloatField(default='', verbose_name='温度')
    humidity = models.FloatField(default='', verbose_name='湿度')
    carbondioxide = models.FloatField(default='', verbose_name='二氧化碳')
    pm = models.FloatField(default='', verbose_name='PM2.5')
    candela = models.FloatField(default='', verbose_name='光照强度')

class Fire_Monitor(models.Model):
    fire_Monitor = models.ForeignKey(Scene_Monitor, on_delete=models.CASCADE)
    smoke = models.FloatField(default='', verbose_name='烟雾')
    CH4 = models.FloatField(default='', verbose_name='甲烷')
    fire = models.FloatField(default='', verbose_name='火光')

class Safe_Monitor(models.Model):
    INVADE = [
        (1, '入侵'),
        (2, '安全')
    ]
    STATUS = [
        (1, '在线'),
        (2, '离线')
    ]

    safe_Monitor = models.ForeignKey(Scene_Monitor, on_delete=models.CASCADE)
    invade_Examine = models.IntegerField(choices=INVADE, default=2, verbose_name='入侵检测')
    access_Status = models.IntegerField(choices=STATUS, default=1, verbose_name='门禁状态')

class Device_Monitor(models.Model):
    STATUS = [
        (1, '开启'),
        (2, '关闭')
    ]

    device_Num = models.ForeignKey(Scene_Monitor, on_delete=models.CASCADE)
    alarm_Light = models.IntegerField(choices=STATUS, default=2, verbose_name='报警灯')
    alarm_clock = models.IntegerField(choices=STATUS, default=2, verbose_name='报警器')
    water_pump = models.IntegerField(choices=STATUS, default=1, verbose_name='水泵')
    fan = models.IntegerField(choices=STATUS, default=1, verbose_name='风机')
    LED = models.IntegerField(choices=STATUS, default=1, verbose_name='LED显示屏')
