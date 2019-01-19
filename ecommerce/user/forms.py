from datetime import date

from django import forms

from user import encrption_pwd
from user.models import Users



# 注册密码检验
class RegisterModelForm(forms.ModelForm):
    password = forms.CharField(min_length=8, max_length=20, error_messages={
        'min_length': '密码不能小于8位',
        'max_length': '密码最大长度为20',
        'required': '密码不能为空'
    })
    repwd = forms.CharField(min_length=8, max_length=20, error_messages={
        'min_length': '密码不能小于8位',
        'max_length': '密码最大长度为20',
        'required': '密码不能为空'
    })

    class Meta:
        model = Users
        fields = ['mobile']

        error_messages = {
            'mobile': {
                'required': '号码不能为空',
                'max_length': '最大长度不能超过11',
                'min_length': '最小长度不能小于11'
            }
        }


     # 判断用户名是否存在
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        flag = Users.objects.filter(username=mobile).exists()
        if flag:
            raise forms.ValidationError({
                'mobile': '用户名已存在'
            })
        else:
            return mobile

    # 判断两次密码是否一致
    def clean(self):
        pwd = self.cleaned_data.get('password')
        repwd = self.cleaned_data.get('repwd')
        if pwd and repwd and pwd != repwd:
            raise forms.ValidationError({'repwd': '两次密码不一致'})
        else:
            return self.cleaned_data


# 登陆检验

# class LoginModelForm(forms.ModelForm):
#     password = forms.CharField(max_length=20, min_length='8', error_messages={
#         'required': '密码不能为空',
#         'min_length': '密码最低长度位8',
#         'max_length': '密码最大长度位20'
#     })
#
#     class Meta:
#         model = Users
#         fields = ['username']
#         error_messages = {
#             'username': {
#                 'required': '用户名不能为空',
#                 'max_length': '最大长度不能超过20',
#                 'min_length': '最小长度不能小于2',
#             }
#         }
#
#     def clean(self):
#         # 验证用户名
#         username = self.cleaned_data.get('username')
#         # 查询数据库
#         try:
#             user = Users.objects.get(username=username)
#         except Users.DoesNotExist:
#             raise forms.ValidationError({'username': '用户名错误'})
#
#         # 验证密码
#         password = self.cleaned_data.get('password', '')
#         if user.password != encrption_pwd(password):
#             raise forms.ValidationError({'password': '密码错误'})
#
#         # 返回所有清洗后的数据
#         self.cleaned_data['user'] = user
#         return self.cleaned_data
# '''
# class LoginModelForm(forms.ModelForm):
#     """注册表单模型类"""
#
#     # 单独定义一个字段
#     password = forms.CharField(max_length=16,
#                                min_length=8,
#                                error_messages={
#                                    'required': '必须填写密码',
#                                    'min_length': '密码最小长度必须为8位',
#                                    'max_length': '密码最大长度不能超过16位',
#                                })
#
#     class Meta:
#         model = Users
#         fields = ['username']
#
#         error_messages = {
#             "username": {
#                 'required': '用户名必须填写',
#                 'max_length': '用户名长度不能大于20',
#             }
#         }
#
#     def clean(self):
#         # 验证用户名
#         username = self.cleaned_data.get('username')
#         # 查询数据库
#         try:
#             user = Users.objects.get(username=username)
#         except Users.DoesNotExist:
#             raise forms.ValidationError({'username': '用户名错误'})
#
#         # 验证密码
#         password = self.cleaned_data.get('password','')
#         if user.password != encrption_pwd(password):
#             raise forms.ValidationError({'password': '密码错误'})
#
#         # 返回所有清洗后的数据
#         self.cleaned_data['user'] = user
#         return self.cleaned_data
# '''
