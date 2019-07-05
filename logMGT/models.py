from django.db import models
import datetime
# Create your models here.


class logMGT_Logging(models.Model):
    STATUS = [
        (1, '上线'),
        (2, '下线'),
        (3, '')
    ]
    scene_ID = models.IntegerField(default=0, verbose_name='场景ID')
    scene_IDCode = models.CharField(max_length=10, default='', verbose_name='场景识别码')
    device_ID = models.IntegerField(default=0, verbose_name='设备ID')
    device_Status = models.IntegerField(choices=STATUS, default=3, verbose_name='设备状态')
    user_ID = models.IntegerField(default=0, verbose_name='用户ID')
    device_Control = models.CharField(max_length=50, default='', verbose_name='设备控制')
    user_Action = models.CharField(max_length=50, default='', verbose_name='用户行为')


class logMGT_List(models.Model):
    STATUS = [
        (1, '状态变化'),
        (2, '设备操作'),
        (3, '数据变化'),
        (4, '门禁开锁')
    ]
    log_Time = models.DateTimeField(default=datetime.datetime.now(), null=True, verbose_name='日志时间')
    scene_ID = models.IntegerField(default=0, verbose_name='场景ID')
    scene_IDCode = models.CharField(max_length=10, default='', verbose_name='场景识别码')
    log_Type = models.IntegerField(choices=STATUS, default=3, verbose_name='日志类型')
    log_Detail = models.CharField(max_length=50, default='', verbose_name='日志描述')
