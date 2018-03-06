#coding: utf-8

from django.db import models

class UserInfo(models.Model):
    """设计表需要的字段"""
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    ushou = models.CharField(max_length=120, default='')   #收货地址
    uaddress = models.CharField(max_length=100, default='')   #详细地址
    uyoubain = models.CharField(max_length=6, default='')    #邮编
    uphone = models.CharField(max_length=11, default='')   #手机号
    #default, blank  是python层面的约束，，不影响数据库的表结构，所以修改之后不用再迁移数据库

















