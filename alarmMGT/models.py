
from django.db import models


# Create your models here.


class WarningRecord(models.Model):  # 警告记录
    warning_in_type_choices = [  # 备注
        ('environment', '环境监测'),
        ('fighting', '消防监测'),
        ('security', '安防监测'),
        ('scene', '场景监测')
    ]
    warning_in_state_choices = (
        ('pendingNew', '待处理'),
        ('pendingApproval', '待审核'),
        ('auditing', '审核通过'),
        ('auditFailed', '审核不通过')
    )
    warning_ID = models.AutoField(primary_key=True)
    warning_SummaryInfo = models.TextField(default='', verbose_name='警报概要信息')
    warning_StartTime = models.DateTimeField(verbose_name='警报开始时间')
    warning_EndTime = models.DateTimeField(verbose_name='警报结束时间')
    warning_Type = models.CharField(max_length=20, blank=False, choices=warning_in_type_choices,
                                    verbose_name='报警类型')  # 四种类型：环境监测、消防监测、安防监测、场景监测
    warning_Scene = models.IntegerField(blank=False, verbose_name='所属场景')  # 外键，场景识别码
    warning_Equipment = models.CharField(max_length=30, blank=False, verbose_name='告警设备')
    warning_Content = models.TextField(default='', verbose_name='告警内容')
    warning_State = models.CharField(max_length=30, blank=False, choices=warning_in_state_choices,
                                     verbose_name='告警状态')  # 四种状态：待处理、待审核、审核通过、审核不通过


class WarningHandleRecord(models.Model):  # 警告处理记录
    warning_in_level_choices = (
        ('serious', '严重警告'),
        ('important', '重要警告'),
        ('general', '一般警告')
    )
    warning_ID = models.AutoField(primary_key=True)
    # warning_RecordID = models.IntegerField(verbose_name='禁告记录ID')  # 外键，对应WarningRecord表中的ID
    warning_RecordID = models.ForeignKey(WarningRecord)
    warning_Person = models.CharField(max_length=30, blank=False, verbose_name='警告确认人')
    warning_HandleTime = models.DateTimeField(verbose_name='警告确认时间')
    warning_HandleIllustration = models.TextField(default='', verbose_name='解释说明')
    warning_VerifyTime = models.DateTimeField(verbose_name='审核时间')
    warning_VerifyFeedback = models.TextField(default='', verbose_name='审核反馈')
    warning_VerifyPerson = models.CharField(max_length=30, blank=False,
                                            verbose_name='审核人员')
    warning_Level = models.CharField(max_length=30,
                                     blank=False, choices=warning_in_level_choices,
                                     verbose_name='报警级别')  # 三种警告：严重告警、重要告警、一般告警。消防属于严重告警，安防、场景状态属于重要告警，环境属于一般告警


class WarningEnvironmentRecord(models.Model):  # 警告环境记录
    warning_ID = models.AutoField(primary_key=True)
    warning_UpdateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    warning_Temperature = models.FloatField(verbose_name='温度检测')
    warning_Humidity = models.FloatField(verbose_name='湿度检测')
    warning_CarbonDioxide = models.FloatField(verbose_name='二氧化碳检测')
    warning_PM = models.FloatField(verbose_name='PM2.5检测')


class WarningFightingRecord(models.Model):  # 警告消防记录
    warning_ID = models.AutoField(primary_key=True)
    warning_UpdateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    warning_CH4 = models.FloatField(blank=True, null=True, verbose_name='甲烷检测')
    warning_Smog = models.FloatField(blank=True, null=True, verbose_name='烟雾检测')
    warning_Fire = models.FloatField(blank=True, null=True, verbose_name='火光检测')


class WarningSecurityRecord(models.Model):  # 警告安全记录
    warning_ID = models.AutoField(primary_key=True)
    warning_UpdateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    warning_Invasion = models.BooleanField(blank=True, verbose_name='入侵检测')
    warning_EntranceGuard = models.BooleanField(blank=True, verbose_name='门禁检测')


class WarningSceneRecord(models.Model):  # 警告场景记录

    warning_ID = models.AutoField(primary_key=True)
    warning_UpdateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    warning_Online = models.BooleanField(verbose_name='是否在线')