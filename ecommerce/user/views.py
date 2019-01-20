from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from user import set_password
from user.forms import RegisterModelForm, LoginModelForm
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
            #将密码进行哈希加密
            password = set_password(password)
            #保存数据库
            Users.objects.create(mobile=mobile, password=password)
            return redirect('user:login')
        else:
            #如果表单数据不合理则抛出错误
            # 清洗数据并获取相应的信息
            mobile = form.cleaned_data.get('mobile')
            #获取错误信息
            errors = form.errors
            #准备参数
            context = {
                'mobile': mobile,
                'errors': errors
            }
            #返回注册页面
            return render(request, 'user/reg.html', context=context)



#登录页面
class LoginClassView(View):
    #如果请求参数为get则返回到登录页面
    def get(self, request):
        return render(request, 'user/login.html')
    #如果请求参数为post时
    def post(self,request):
        #接收请求参数
        data = request.POST
        #创建实例对象
        form = LoginModelForm(data)
        #判断提交的表单数据是否合理
        if form.is_valid():
            return redirect('user:member')
        else:
            # 如果表单数据不合理则抛出错误
            # 清洗数据并获取相应的信息
            mobile = form.cleaned_data.get('mobile')
            # 获取错误信息
            errors = form.errors
            # 准备参数
            context = {
                'mobile': mobile,
                'errors': errors
            }
            # 返回登录页面页面
            return render(request, 'user/login.html', context=context)


#个人中心
class MemberClassView(View):
    def get(self, requset):
        return render(requset, 'user/member.html')