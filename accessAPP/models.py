<<<<<<< HEAD
# from django.db import models
# import datetime
# # Create your models here.
# #类名为表名的一部分
# class Department(models.Model):
#     STATUS = [
#         (1, '解冻状态'),
#         (2, '冻结状态')
#     ]
#     depname = models.CharField(max_length=60, default='', verbose_name='部门名称')#必须指定maxlength
#     create_time = models.DateTimeField(datetime.datetime.now(), null=True)
#     person_num = models.IntegerField(default=0)
#     depstatus = models.IntegerField(choices=STATUS, default=1)
#     detail = models.TextField(default='', verbose_name='描述')
#     price = models.FloatField
=======
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
>>>>>>> 057363deb0e6e74aa741349b4cd1e3425d66df89
