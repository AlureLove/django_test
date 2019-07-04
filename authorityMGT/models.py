from django.db import models

# Create your models here.


class authorityMGT_Role(models.Model):
    STATUS = [
        (1, '查看'),
        (2, '控制'),
        (3, '告警处理'),
        (4, '告警确认'),
        (5, '门禁审批')
    ]
    role_Name = models.CharField(max_length=50, default='', verbose_name='角色名')
    scene_ID = models.IntegerField(default=0, verbose_name='场景ID')
    scene_Authority = models.IntegerField(choices=STATUS, default=1, verbose_name='场景权限')

class authorityMGT_User(models.Model):
    role_Name = models.CharField(max_length=50, default='', verbose_name='角色名')
    user_ID = models.IntegerField(default=0, verbose_name='用户ID')

