from django.db import models


# Create your models here.
class VideoInformation(models.Model):
    video_ID = models.AutoField(primary_key=True)  # id一般是自增主键
    video_IdentifyingCode = models.IntegerField()
    video_Name = models.CharField(max_length=30, blank=False, verbose_name='视频名称')
    video_describe = models.TextField(default='', verbose_name='描述')
    video_StreamAddress = models.URLField(blank=False,   verbose_name='流地址')
