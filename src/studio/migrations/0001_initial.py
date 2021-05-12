# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, verbose_name='name', blank=True)),
                ('logo', models.CharField(max_length=400, verbose_name='log url', blank=True)),
                ('dsp', models.TextField(verbose_name='description', blank=True)),
                ('link_ios', models.CharField(max_length=400, verbose_name='link to IOS', blank=True)),
                ('link_gp', models.CharField(max_length=400, verbose_name='link to Google', blank=True)),
                ('link_face', models.CharField(max_length=400, verbose_name='link to Facebook page', blank=True)),
                ('link_twit', models.CharField(max_length=400, verbose_name='link to Twitter Page', blank=True)),
                ('email', models.CharField(max_length=100, verbose_name='contact us email', blank=True)),
                ('policy', models.TextField(verbose_name='private policy', blank=True)),
                ('ga_key', models.CharField(max_length=300, verbose_name='Google Analytics Key', blank=True)),
                ('fea_app', models.TextField(verbose_name='Featured App', blank=True)),
            ],
        ),
    ]
