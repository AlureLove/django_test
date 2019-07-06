from django.db import models
import datetime
# Create your models here.

class User_Management(models.Model):
    SEX = [
        (1, '男'),
        (2, '女')
    ]

    STATUS = [
        (1, '冻结状态'),
        (2, '解冻状态')
    ]

    ROLE = [
        (1, '超级管理员'),
        (2, '高级管理员'),
        (3, '普通管理员')
    ]

    user_ID = models.IntegerField(default=0, verbose_name='用户id')
    user_Name = models.CharField(max_length=20, default='', verbose_name='用户姓名')
    user_Sex = models.IntegerField(choices=SEX, default=1, verbose_name='用户性别')
    user_Age = models.IntegerField(default='', verbose_name='用户年龄')
    user_Num = models.IntegerField(default='', verbose_name='用户工号')
    user_Image = models.ImageField(upload_to='user/%Y', verbose_name='用户头像')
    user_Telnum = models.CharField(max_length=10, default='', verbose_name='用户电话号码')
    user_Logtime = models.DateTimeField(default=datetime.datetime.now(), null=True, verbose_name='用户最近登陆时间')
    user_status = models.IntegerField(choices=STATUS, default=2, verbose_name='用户状态')
    user_role = models.IntegerField(choices=ROLE, default=3, verbose_name='用户角色')
    user_AccountName = models.CharField(max_length=30, default='', verbose_name='用户的账户名称')
    user_Password = models.CharField(max_length=10, default='', verbose_name='用户的账户密码')
    user_Address = models.CharField(max_length=60, default='', verbose_name='用户联系地址')
    user_Tips = models.CharField(max_length=60, default='', verbose_name='用户备注信息')
    user_CreateTime = models.DateTimeField(default=datetime.datetime.now(), null=True, verbose_name='用户创建时间')
    user_Summary = models.TextField(default='', verbose_name='用户概述')

class Stu(models.Model):
    name = models.CharField(max_length=30, verbose_name='学生姓名')
    age = models.IntegerField(default=0, verbose_name='学生年龄')

    # def __str__(self):
    #     return self.name()



