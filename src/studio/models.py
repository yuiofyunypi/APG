# -*- encoding:utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.admin.models import LogEntry

# Create your models here.

class Studio(models.Model):
    name = models.CharField('name', max_length=300, blank=True)
    logo = models.CharField('log url', max_length=400, blank=True)
    dsp = models.TextField(verbose_name='description', blank=True)
    link_ios = models.CharField('link to IOS',max_length=400, blank=True)
    link_gp = models.CharField('link to Google',max_length=400, blank=True)
    link_face = models.CharField('link to Facebook page',max_length=400, blank=True)
    link_twit = models.CharField('link to Twitter Page',max_length=400, blank=True)
    email = models.CharField('contact us email', max_length=100, blank=True)
    policy = models.TextField(verbose_name='private policy', blank=True)
    ga_key = models.CharField('Google Analytics Key', max_length=300, blank=True)
    fea_app = models.TextField(verbose_name='Featured App', blank=True)
    
    

class App(models.Model):
    StatusChoice=(
        ('normal','Normal'),
        ('abnormal','Abnormal'),
        ('error','Error'),
    )
    sku = models.CharField('SKU', max_length=300, default='')
    icon = models.CharField('Icon Url', max_length=300, blank=True)
    screenshots = models.TextField(verbose_name='Screen Shot', blank=True)
    fea_graph = models.CharField('Featured Graphics', max_length=300, blank=True)
    status=models.CharField('Status', max_length=100, choices=StatusChoice, blank=True)


class Log(models.Model):
    LOG_Type=(
        ('normal','Normal'),
        ('warning','Waring'),
        ('error','Error')
    )
    category = models.CharField('Log Category', max_length=100, default='')
    key = models.CharField('Log Key', max_length=100, blank=True)
    type = models.CharField('Status', max_length=100, choices=LOG_Type,default='normal')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True)
    time = models.DateTimeField(verbose_name='date time',auto_now=True)
    title = models.CharField('title', max_length=400, blank=True)
    content = models.TextField(verbose_name='Log Content', blank=True)
    
    
    
    
    
    