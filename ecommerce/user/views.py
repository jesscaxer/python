from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from user.forms import RegisterModelForm
from user.models import Users


class RegisterClassView(View):
    #创建与请求方法同名的方法
    def get(self, request):
        #当点击注册请求方法为get时返回注册页面
        return render(request, 'user/reg.html')
    #当请求方式为Post时
    def post(self,request):
        #接收请求参数
        data = request.POST
        #创建实例化对象
        form = RegisterModelForm(data)
        # 判断数据是否合理
        if form.is_valid():
            #清洗数据并获取相应的信息
            mobile = form.cleaned_data.get('mobile')
            password = form.cleaned_data.get('password')
            #保存数据库
            Users.objects.create(mobile=mobile, password=password)
            return HttpResponse('ok')
        else:
            return HttpResponse('not ok')