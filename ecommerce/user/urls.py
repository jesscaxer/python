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
    # url(r'^$', views.MainClassView.as_view(), name='main'),
    # url(r'^add/$', views.AddClassView.as_view(), name='add'),
    # url(r'^detail/(.*?)/$', views.DetailClassView.as_view(), name='detail'),
    # url(r'^delete/(.*?)/$', views.DeleteClassView.as_view(), name='delete'),
    # url(r'^update/(.*?)/$', views.UpdateClassView.as_view(), name='update'),
    # url(r'^login/$', views.landingClassView.as_view(), name='login'),
]
