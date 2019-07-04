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