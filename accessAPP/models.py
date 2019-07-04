from django.db import models
import datetime
# Create your models here.


class accessAPP_Application(models.Model):
    STATUS = [
        (1, '待审批'),
        (2, '已通过'),
        (3, '已拒绝')
    ]
    apply_Time = models.DateTimeField(default=datetime.datetime.now(), null=True, verbose_name='申请时间')
    user_ID = models.IntegerField(default=0, verbose_name='用户ID')
    scene_ID = models.IntegerField(default=0, verbose_name='场景ID')
    apply_Detail = models.CharField(max_length=50, default='', verbose_name='申请说明')
    apply_Status = models.IntegerField(choices=STATUS, default=1, verbose_name='审批状态')
    approval_Time = models.DateTimeField(default='', null=True, verbose_name='审批时间')
    approval_User = models.IntegerField(default=0, verbose_name='审批人')
    approval_Detail = models.CharField(max_length=50, default='', verbose_name='审批反馈')
