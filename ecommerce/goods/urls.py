from django.conf.urls import url

from goods import views

urlpatterns = [
    url(r'^$', views.IndexClassView.as_view(), name='register'),
    url(r'^detail/(.*?)/$', views.DetailClassView.as_view(), name='detail'),
    url(r'^category/$', views.CategoryClassView.as_view(), name='category'),
    # url(r'^infor/$', views.IforClassView.as_view(), name='infor'),
    # url(r'^update_password/$', views.Update_passwordClassView.as_view(), name='update_password'),
    # url(r'^SendMsm/$', views.SendMsm.as_view(), name='SendMsm'),
    # url(r'^forget/$', views.ForgetClassView.as_view(), name='forget'),

]
