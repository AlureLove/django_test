from django.db import models
import datetime
# Create your models here.
class Scene_Management(models.Model):
    STATUS = [
        (1, '在线'),
        (2, '离线')
    ]

    PRIORITY = [
        (1, '高'),
        (2, '中'),
        (3, '低')
    ]

    scene_ID = models.IntegerField(default=0, verbose_name='场景id')
    scene_IDCode = models.CharField(max_length=10, default='', verbose_name='场景识别码')
    scene_Name = models.CharField(max_length=30, default='', verbose_name='场景名称')
    scene_Password = models.CharField(max_length=10, default='', verbose_name='场景密码')
    scene_LinkTime = models.DateTimeField(default=datetime.datetime.now(), verbose_name='场景接入时间')
    scene_Status = models.IntegerField(choices=STATUS, default=1, verbose_name='场景状态')
    scene_CreateTime = models.DateTimeField(default=datetime.datetime.now(), verbose_name='场景创建时间')
    scene_DeviceNum = models.IntegerField(default=0, verbose_name='场景设备的数量')
    scene_Priority = models.IntegerField(choices=PRIORITY, default=1, verbose_name='场景优先级')

class Scene_Status(models.Model):
    STATUS = [
        (1, '在线'),
        (2, '离线')
    ]

    scene_Status = models.ForeignKey(Scene_Management, on_delete=models.CASCADE)
    scene_GatewayStatus = models.IntegerField(choices=STATUS, default=1, verbose_name='场景网关状态')
    date_UpdateTime = models.DateTimeField(default=datetime.datetime.now(), verbose_name='数据更新时间')
    device_OnlineRatio = models.FloatField(default='', verbose_name='设备在线比例')

