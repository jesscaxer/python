# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

# from user.forms import RegisterModelForm, LoginModelForm
# from user.helper import check_login
# from user.models import Users
import hashlib

from user.forms import RegisterModelForm
from user.models import Users


def encrption_pwd(password):
    password = password
    password = hashlib.md5(password.encode('utf-8'))
    password = password.hexdigest()
    return password



def set_password(password):
    # 加密方法
    h = hashlib.md5(password.encode('utf-8'))
    return h.hexdigest()


# 注册页
class RegisterClassView(View):

    def get(self, request):
        # 显示注册页面表单
        return render(request, 'user/reg.html')

    def post(self, request):
        # 请求方式为post保存表单提交的数据到数据库
        data = request.POST
        form = RegisterModelForm(data)
        if form.is_valid():
            mobile = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password =encrption_pwd(password)
            Users.objects.create(mobile=mobile, password=password)


            # # 操作数据库
            # cleaned_data = form.cleaned_data
            # # 创建一个用户
            # user = Users()
            # user.username = cleaned_data.get('username')
            # user.password = set_password(cleaned_data.get('password'))
            # user.save()
            return HttpResponse('user:main')

        else:
            context = {
                'mobile': form.cleaned_data.get('mobile')
            }
            return render(request, 'user/reg.html', context=context)


# #登陆页
# class landingClassView(View):
#     def get(self, request):
#         return render(request, 'loginitem/login.html')
#
#     def post(self, request):
#         data = request.POST
#         form = LoginModelForm(data)
#         if form.is_valid():
#             user = form.cleaned_data.get('user')
#             request.session['ID'] = user.pk
#             request.session['username'] = user.username
#             return redirect('login:main')
#         else:
#             return render(request, 'loginitem/login.html', {'form': form})
#
#
# # 主页面类
#
# class MainClassView(View):
#     @check_login
#     def get(self, request):
#         # 进入主页面
#         # 查询数据
#         data = ToDoList.objects.all()
#         # Paginator 实现分页
#         paginator = Paginator(data, 4)
#         # 获取当前页面的页码
#         page = request.GET.get('page', 1)
#
#         # 获取对应页码的数据
#         try:
#             data = paginator.page(page)
#         except PageNotAnInteger:
#             # 页码不是整数 显示第一页
#             data = paginator.page(1)
#         except EmptyPage:
#             # 页码为空 显示最后一页
#             data = paginator.page(paginator.num_pages)
#
#         context = {
#             'data': data
#         }
#         # 渲染页面
#         return render(request, 'loginitem/main.html', context=context)
#
# # 添加页
# class AddClassView(View):
#     @check_login
#     def get(self, request):
#         return render(request, 'loginitem/add.html')
#
#     def post(self, request):
#         # 获取表单传递的信息
#         data = request.POST
#         # 验证数据是否合法
#         form = AddModelForm(data)
#         # 数据合法
#         if form.is_valid():
#             form.save()
#             return redirect('login:main')
#         # 数据不合法
#         else:
#             context = {
#                 'errors': form.errors,
#                 'data': data
#             }
#             # 返回添加页并回返数据
#             return render(request, 'loginitem/add.html', context=context)
#
# # 详情页
# class DetailClassView(View):
#     @check_login
#     def get(self, request, ToDoId):
#         # 查询对应id的数据
#         data = ToDoList.objects.get(pk=ToDoId)
#         context = {
#             'data': data
#         }
#         # 渲染html页面
#         return render(request, 'loginitem/detail.html', context=context)
#
# # 删除页面
# class DeleteClassView(View):
#     @check_login
#     def get(self, request, ToDOId):
#         # 查询出对应id的数据删除
#         ToDoList.objects.filter(pk=ToDOId).delete()
#         # 跳转回主页
#         return redirect('login:main')
#
#
#
# # 更新数据
# class UpdateClassView(View):
#     # 进入表单修改页面
#     @check_login
#     def get(self, request, ToDoId):
#         # 查询数据
#         data = ToDoList.objects.get(pk=ToDoId)
#         context = {
#             'data': data
#         }
#         # 渲染页面
#         return render(request, 'loginitem/update.html', context=context)
#
#     # 保存表单提交的数据
#     def post(self, request, ToDoId):
#         # 获取数据
#         data = request.POST
#         item = ToDoList.objects.get(pk=ToDoId)
#         # 对数据进行验证
#         form = AddModelForm(data, instance=item)
#         if form.is_valid():
#             # 数据合法
#             form.save()
#             # ToDoList.objects.filter(pk=ToDoId).update(title=data['title'], todotime=data['todotime'], content=data['content'])
#             return redirect('login:detail', ToDoId )
#         else:
#             # 数据不合法
#             context = {
#                 'errors': form.errors,
#                 'data': data
#             }
#             # 回现页面
#             return render(request, 'loginitem/update.html', context=context)
