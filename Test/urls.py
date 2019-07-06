"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import rest_framework.authtoken.views
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='InterfaceDevelop API') #配置的api名字

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^userMGT/', include('userMGT.urls'))

    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api_token_auth/', obtain_jwt_token),
    url(r'^api/', schema_view), #图形化界面
    url(r'^userMGT/', include('userMGT.urls', namespace='userMGT', app_name='userMGT')),
]
