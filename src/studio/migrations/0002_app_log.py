# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sku', models.CharField(default='', max_length=300, verbose_name='SKU')),
                ('icon', models.CharField(max_length=300, verbose_name='Icon Url', blank=True)),
                ('screenshots', models.TextField(verbose_name='Screen Shot', blank=True)),
                ('fea_graph', models.CharField(max_length=300, verbose_name='Featured Graphics', blank=True)),
                ('status', models.CharField(blank=True, max_length=100, verbose_name='Status', choices=[('normal', 'Normal'), ('abnormal', 'Abnormal'), ('error', 'Error')])),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default='', max_length=100, verbose_name='Log Category')),
                ('key', models.CharField(max_length=100, verbose_name='Log Key', blank=True)),
                ('type', models.CharField(default='normal', max_length=100, verbose_name='Status', choices=[('normal', 'Normal'), ('warning', 'Waring'), ('error', 'Error')])),
                ('time', models.DateTimeField(auto_now=True, verbose_name='date time')),
                ('title', models.CharField(max_length=400, verbose_name='title', blank=True)),
                ('content', models.TextField(verbose_name='Log Content', blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
