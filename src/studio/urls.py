from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.display_list),
    url(r'^add/$',views.add),
    url(r'^edit/(.+)',views.edit),
    url(r'^upload/log',views.upload_log)
]
