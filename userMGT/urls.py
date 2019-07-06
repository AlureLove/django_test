from django.conf.urls import url, include
from django.contrib import admin

from userMGT import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
   # url(r'^userMGT/', include('userMGT.urls')) #优先找app下的urls
    #url(r'^user_list/', views.UserList, name='user_list'), #用户列表路径配置
    url(r'^index_class/', views.IndexClass.as_view(), name='index_class'),

]