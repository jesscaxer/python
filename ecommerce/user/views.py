import random
import re
import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django_redis import get_redis_connection

from user import set_password
from user.forms import RegisterModelForm, LoginModelForm, InforModelForm, Update_passwordForm, ForgetModelForm
from user.helper import send_sms
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
            # mobile = form.cleaned_data.get('mobile')
            #获取错误信息
            errors = form.errors
            #准备参数
            context = {
                'mobile': request.POST.get('mobile'),
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
            #创建session
            # 获取清洗后的user信息
            user = form.cleaned_data.get('user')
            #创建session
            request.session['id'] = user.id
            request.session['mobile'] = user.mobile
            request.session['head_show'] = user.head_show
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
    def get(self, request):
        #判断是否存在session,如果没有则返回到登录页面
        if request.session.get('id') is None:
            return redirect('user:login')
        #如果有则返回个人中心
        else:
            #接收session参数
            mobile = request.session.get('mobile')
            #准备将mobile数据传入个人中心
            context = {'mobile': mobile}
            #返回个人中心页面
            return render(request, 'user/member.html', context=context)
    def post(self,request):
        return HttpResponse('ok')




#修改密码
class Update_passwordClassView(View):
    def get(self, request):
        # 判断是否存在session,如果没有则返回到登录页面
        if request.session.get('id') is None:
            return redirect('user:login')
        # 如果有则返回个人中心
        else:
            return render(request, 'user/password.html')
    def post(self,request):
        data = request.POST
        #创建实例化对象
        form = Update_passwordForm(data)
        # 判断数据是否合理
        if form.is_valid():
            # 接收请求参数
            mobile = request.session.get('mobile')
            new_password = form.cleaned_data.get('new_password')
            #将密码进行哈希加密
            password = set_password(new_password)
            #保存数据库
            Users.objects.filter(mobile=mobile).update(password=password)
            return redirect('user:member')
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
            return render(request, 'user/password.html', context=context)


#个人资料
class IforClassView(View):
    #当请求方式为get的时候
    def get(self, request):
        # 判断是否存在session,如果没有则返回到登录页面
        if request.session.get('id') is None:
            return redirect('user:login')
        # 如果有则返回资料修改页面
        else:
            # 接收session参数
            id1 = request.session.get('id')
            # 根据id将用户的个人信息从数据库中查询出来
            user = Users.objects.get(id=id1)
            # 返回资料修改页面
            return render(request, 'user/infor.html', context={'user': user})
    def post(self,request):
        #接收参数
        data = request.POST
        #创建实例化对象
        user_id = request.session.get("id")
        head_show = request.FILES.get("head_show")
        form = InforModelForm(data, instance=Users.objects.get(pk=user_id))
        #判断数据是否合理
        if form.is_valid():
            #清洗数据
            infor = form.cleaned_data
            id = request.session.get('id')
            #合理则更新数据
            Users.objects.filter(id=id).update(
                head_show=head_show,
                username=infor.get('name'),
                sex=infor.get('sex'),
                birthday=infor.get('birthday'),
                school=infor.get('school'),
                location=infor.get('location'),
                home=infor.get(' home'),)
            return render(request, 'user/member.html')
        else:
            # 如果表单数据不合理则抛出错误
            # 清洗数据并获取相应的信息
            mobile = form.cleaned_data.get('mobile')
            # 获取错误信息
            errors = form.errors#如果表单数据不合理则抛出错误
            #准备参数
            context = {
                'mobile': mobile,
                'errors': errors
            }
            return render(request, 'user/infor.html', context=context)




#忘记密码
class ForgetClassView(View):
    def get(self, request):
        return render(request, 'user/forgetpassword.html')

        # 当请求方式为Post时

    def post(self, request):
        # 接收请求参数
        data = request.POST
        #获取电话号码
        mobile = request.POST.get('mobile')
        # 创建实例化对象
        form = ForgetModelForm(data, instance=Users.objects.get(mobile=mobile))
        # 判断数据是否合理
        if form.is_valid():
            # 清洗数据并获取相应的信息
            mobile = form.cleaned_data.get('mobile')
            password = form.cleaned_data.get('password')
            # 将密码进行哈希加密
            password = set_password(password)
            # 保存数据库
            Users.objects.filter(mobile=mobile).update(password=password)
            return redirect('user:login')
        else:
            # 如果表单数据不合理则抛出错误
            # 清洗数据并获取相应的信息
            # mobile = form.cleaned_data.get('mobile')
            # 获取错误信息
            errors = form.errors
            # 准备参数
            context = {
                'mobile': request.POST.get('mobile'),
                'errors': errors
            }
            # 返回修改密码的页面
            return render(request, 'user/forgetpassword.html', context=context)







class SendMsm(View):
    """发送短消验证码"""

    def get(self, request):
        pass

    def post(self, request):
        # 1, 接收参数
        mobile = request.POST.get('mobile', '')
        rs = re.search('^1[3-9]\d{9}$', mobile)
        # 判断参数合法性
        if rs is None:
            return JsonResponse({'error': 1, 'errmsg': '电话号码格式错误!'})
        # 2. 处理数据

        # 模拟,最后接入运营商
        """
            1. 生成随机验证码
            2. 保存验证码 保存到redis中, 存取速度快,并且可以方便的设置有效时间
            3. 接入运营商
        """

        # 1. 生成随机验证码字符串
        random_code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        print("=============随机验证码为==={}==============".format(random_code))

        # 2. 保存验证码到redis中
        # 获取连接
        r = get_redis_connection()
        # 保存手机号码对应的验证码
        r.set(mobile, random_code)
        r.expire(mobile, 60)  # 设置60秒后过期

        # 首先获取当前手机号码的发送次数
        key_times = "{}_times".format(mobile)
        now_times = r.get(key_times)  # 从redis获取的二进制,需要转换
        # print(int(now_times))
        if now_times is None or int(now_times) < 100:
            # 保存手机发送验证码的次数, 不能超过5次
            r.incr(key_times)
            # 设置一个过期时间
            r.expire(key_times, 3600)  # 一个小时后再发送
        else:
            # 返回,告知用户发送次数过多
            return JsonResponse({"error": 1, "errmsg": "发送次数过多"})

        #3. 接入运营商
        __business_id = uuid.uuid1()
        params = "{\"code\":\"%s\",\"product\":\"跳舞的兔子\"}" % random_code
        # print(params)
        rs = send_sms(__business_id, mobile, "注册验证", "SMS_2245271", params)
        print(rs.decode('utf-8'))


        # 3. 合成响应
        return JsonResponse({'error': 0})



