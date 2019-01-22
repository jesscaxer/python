"""ecommerce URL Configuration

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

from django.conf.urls import url

from user import views


urlpatterns = [
    url(r'^register/$', views.RegisterClassView.as_view(), name='register'),
    url(r'^login/$', views.LoginClassView.as_view(), name='login'),
    url(r'^member/$', views.MemberClassView.as_view(), name='member'),
    url(r'^infor/$', views.IforClassView.as_view(), name='infor'),
    url(r'^update_password/$', views.Update_passwordClassView.as_view(), name='update_password'),
    url(r'^SendMsm/$', views.SendMsm.as_view(), name='SendMsm'),
    url(r'^forget/$', views.ForgetClassView.as_view(), name='forget'),

]
