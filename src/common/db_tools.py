# -*- encoding:utf-8 -*-
from django.db import models
from django.apps import apps

import json


def get_or_none(model, **kw):
    """
    """
    try:
        obj = model.objects.filter(**kw).order_by('-id')[0]
        return obj
    except IndexError:
        return None



def to_dict(instance,filt_attr=None,include=None,exclude=None):
    """
    fields=['name','age'] 虽然中函数中fields是django中的model.field对象，但是这里为了方便，接受外部
                         输入是字段的名字
                         
    filt_attr(instance)是可调用对象，返回一个字典，包含已经处理过的属性。这些属性不会再被to_jd操作。
    
    注意，返回的字典，是可以json化的才行。
    """
    fields=instance._meta.fields
    if include:
        fields=filter(lambda field:field.name in include,fields)
    if exclude:
        fields=filter(lambda field:field.name not in exclude,fields)
    if filt_attr:
        out=filt_attr(instance)
    else:
        out={}
    for field in fields:
        if field.name in out:
            continue
        else:
            if isinstance(field,models.ForeignKey):
                foreign=getattr(instance,field.name)
                if foreign:
                    out[field.name]=foreign.pk
                else:
                    out[field.name]=None
            elif isinstance(field,models.DateTimeField):
                out[field.name]=getattr(instance,field.name).strftime('%Y-%m-%d %H:%M:%S')
            else:
                out[field.name]=field.get_prep_value( getattr(instance,field.name) )
    out['pk']=instance.pk
    out['_class']= instance.__module__.split('.')[0]+'.'+instance.__class__.__name__
    return out


def from_dict(dc,model=None,pre_proc=None):
    """

    1. 半自动：
    processed_attr=pre_proc(dc,model) ; 返回处理过的字典processed，该processed用于剔除传入的dc参数
    
    """
    processed={}
    if model is None and '_class' in dc:
        model=apps.get_model(dc['_class'])
    if pre_proc:
        processed=pre_proc(dc,model)
    for k in processed:
        dc.pop(k)         # 去除被pre_proc处理过的值， (因为处理过的值，不应再被 _convert_foreign处理)
    _convert_foreign(dc,model)
    dc.update(processed)   # 把pre_proc的值合并回去 ，(因为下面要给 instance赋值)
    pk=dc.get('pk')
    if pk:
        instance=model.objects.get(pk=pk) 
        for k,v in dc.items():
            setattr(instance,k,v)       
        return instance            
    else:
        instance=model.objects.create(**dc)
        return instance
    
def _convert_foreign(dc,model):
    fields=model._meta.fields
    for field in fields:
        if field.name in dc and isinstance(field,models.ForeignKey):
            dc[field.name]=_deserilize_foreignkey(field, dc[field.name])    

def _deserilize_foreignkey(field,pk):
    if pk is not None:
        model=field.rel.to
        return model.objects.get(pk=pk)
    else:
        return None

def _field_name_to_filed(fields,instance):
    out = []
    for name in fields:
        for field in instance._meta.fields:
            if field.name==name:
                out.append(field)
                break  
    return out
                
            
            
    