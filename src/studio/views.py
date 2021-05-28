# -8- encoding:utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from forms import StudioForm
from common.port import jsonpost
from ajax import get_globals
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from os import path
import os
import json
from models import Studio
from common.db_tools import to_dict
# Create your views here.

def display_list(request):
    return render(request,'studio/disp_list.html')

@csrf_exempt
def add(request):
    if request.method=='GET':
        return render(request,'studio/add.html')
    else:
        return jsonpost(request, get_globals())

@csrf_exempt
def edit(request,studio_pk):
    if request.method=='GET':
        studio = Studio.objects.get(pk=studio_pk)
        return render(request,'studio/studio_edit.html',context={'studio':json.dumps(to_dict(studio))})
    else:
        return jsonpost(request, get_globals())    

@csrf_exempt
def upload_log(request):
    file=request.FILES.get('file')
    studio=request.REQUEST.get('studio')
    logo=Logo(file,studio)
    if logo.is_valid():
        logo.save()
        return HttpResponse(json.dumps({'url':logo.get_url()}),content_type="application/json")
    else:
        return HttpResponse(json.dumps({'msg':logo.get_msg()}),content_type="application/json")


class Logo(object):
    def __init__(self,file,studio_name):
        self.file=file
        # self.file_name='logo_{name}.{suffix}'.format(name=studio_name,suffix=file.name.split('.')[-1])
        self.file_name='logo_{name}'.format(name=file.name)
        self.studio=studio_name
        self.msg=[]
    
    def is_valid(self):
        if self.file.name.lower().endswith(('.jpg','.png','.gif')):
            return True
        else:
            self.msg.append('file formate should be jpg,png,gif only')
            return False
    
    def save(self):
        file_path=self._get_path()
        with open(file_path,'wb') as f:
            for chunk in self.file.chunks():
                f.write(chunk)
                
    def _get_path(self):
        file_dir= path.join(settings.MEDIA_ROOT,self.studio)
        try:
            os.makedirs(file_dir)
        except os.error as e:
            pass 
        file_path = path.join(file_dir,self.file_name)
        return file_path
    
    def get_msg(self):
        return ';'.join(self.msg)
    def get_url(self):
        return '/media/{studio}/{file_name}'.format(studio=self.studio,file_name=self.file_name)
    