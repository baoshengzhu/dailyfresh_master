#coding: utf-8

from django.db import models
from tinymce.models import HTMLField

"""商品分类表"""
class TypeInfo(models.Model):
    title = models.CharField(max_length=20)   #标题
    isDelete = models.BooleanField(default=False)    #是否删除、默认不删除
    def __str__(self):
        return self.title.encode('utf-8')

"""商品信息表"""
class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)   #标题
    gpic = models.ImageField(upload_to='df_goods')    #图片
    gprice = models.DecimalField(max_digits=5, decimal_places=2)    #价格  max_digits：总位数，decimal_places：小数位
    isDelete = models.BooleanField(default=False)   #是否删除
    gunit = models.CharField(max_length=20, default='500g')   #单位
    gclick = models.IntegerField()   #点击量
    gjianjie = models.CharField(max_length=200)   #简介
    gkucun = models.IntegerField    #库存
    gcontent = HTMLField()    #商品详情
    gtype = models.ForeignKey(TypeInfo)   #外键
    gadv = models.BooleanField(default=False)   #广告
    def __str__(self):
        self.gtitle.encode('utf-8')




