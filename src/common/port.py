# -*- encoding:utf-8 -*-

import json
import inspect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings

def jsonpost(request, scope):
    """
    该函数会路由ajax请求，ajax发送的json格式为{'order':['func3','func2'],func1:{name:'heyulin'},func2:{arg:..},func3:{arg:}}
    jsonpost根据参数scope里面查询同名函数，按照循序，优先调用order中的函数
    
    example:
    
    下面是一个现成的views函数
    
def ajax_view(request):
    if request.method=='POST':
        try:
            return jsonpost(request, get_globlas())
        except KeyError as e:
            rt={'status':'error','msg':'key error '+str(e) +' \n may function name error'}
            return HttpResponse(json.dumps(rt),content_type="application/json")
            
    """
    router=RouterAjax(request, scope,rt_except=not settings.DEBUG)
    return router.run()

class RouterAjax(object):
    def __init__(self,request,scope,rt_except=False):
        self.request=request
        self.scope=scope
        self.rt_except=rt_except
        self.rt={}
        self.msgs=[]
        
    def run(self):
        self.commands = json.loads(self.request.body)
        self.orders=self.commands.pop('order',[])
        if self.rt_except:
            try:
                self.proc_order()
                self.proc_common()
            except (UserWarning,TypeError) as e:
                self.msgs.append(str(e))
            except KeyError as e:
                self.msgs.append('no function %s'%k)
        else:
            self.proc_order()
            self.proc_common()
        self.rt['msg']=';'.join(self.msgs)
        return HttpResponse(json.dumps(self.rt), content_type="application/json")     

    def proc_order(self):
        for k in self.orders:
            func = self.scope[k]
            kw=self.commands.pop(k)                
            self.rt[k]=self._run_func(func,**kw)
            
    def proc_common(self):
        for k, kw in self.commands.items():
            func = self.scope[k]
            self.rt[k]=self._run_func(func,**kw) 
    
    def _run_func(self,func,**kw):
        args=inspect.getargspec(func).args
        if 'request' in args:
            kw['request']=self.request
        if 'user' in args:
            user=self._get_user()
            if user:
                kw['user']=user
            else:
                raise UserWarning,'function need login ,but you are not login'
                
        return func(**kw)    
    
    def _get_user(self):
        if self.request.user.is_authenticated():
            return self.request.user
        else:
            return None    
                

