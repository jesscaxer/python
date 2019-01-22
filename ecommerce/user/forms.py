from datetime import date, datetime

from django import forms
from django.http import HttpResponse

from user import set_password
from user.models import Users



# 注册密码检验
class RegisterModelForm(forms.ModelForm):
    password = forms.CharField(min_length=8, max_length=20, error_messages={
        'min_length': '密码不能小于8位',
        'max_length': '密码最大长度为16',
        'required': '密码不能为空'
    })
    repassword = forms.CharField(min_length=8, max_length=20, error_messages={
        'min_length': '密码不能小于8位',
        'max_length': '密码最大长度为16',
        'required': '密码不能为空'
    })

    # 验证码

    captcha = forms.CharField(max_length=6,
                              error_messages={
                                  'required': "验证码必须填写"
                              })

    agree = forms.BooleanField(error_messages={
        'required': '必须同意用户协议'
    })


    class Meta:
        model = Users
        fields = ['mobile']
        error_messages = {
            'mobile': {
                'required': '号码不能为空',
            }
        }


    # 判断账号是否存在
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        flag = Users.objects.filter(mobile=mobile).exists()
        if flag:
            raise forms.ValidationError('用户已存在')
        else:
            return mobile

    # 判断两次密码是否一致
    def clean(self):
        pwd = self.cleaned_data.get('password')
        repwd = self.cleaned_data.get('repassword')
        if pwd and repwd and pwd != repwd:
            raise forms.ValidationError({'repassword': '两次密码不一致'})
        else:
            return self.cleaned_data




#登录验证
class LoginModelForm(forms.ModelForm):
    password = forms.CharField(min_length=8, max_length=20, error_messages={
        'min_length': '密码不能小于6位',
        'max_length': '密码最大长度为16',
        'required': '密码不能为空'
    })
    class Meta:
        model = Users
        fields = ['mobile']

        error_messages = {
            'mobile': {
                'required': '号码不能为空',
            }
        }


    #判断账号是否存在
    def clean(self):
        #从提交的数据中提取mobile数据
        mobile = self.cleaned_data.get('mobile')
        password = self.cleaned_data.get('password')
        # 将密码进行加密
        password = set_password(password)
        #从数据库中读取该用户是否存在
        try:
            user = Users.objects.get(mobile=mobile)
        except Users.DoesNotExist:
            raise forms.ValidationError({'mobile': '账号不存在！'})
        #从数据库中获取密码
        password2 = user.password
        #判断从数据库获取的密码与用户输入的密码是否一致
        if password and password2 and password != password2:
            raise forms.ValidationError({'password': '密码错误！'})
        else:
            self.cleaned_data['user'] = user
            return self.cleaned_data




#登录验证
class InforModelForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'birthday', 'school', 'location', 'home']

        error_messages = {
            'username': {
                'required': '用户名不能为空',
                'max_length': '用户名长度不能超过50个字符'},
            'birthday': {'required': '出生日期必填'},
            'school': {'max_length': '内容过长'},
            'location': {'max_length': '内容过长'},
            'home': {'max_length': '内容过长'},
        }


    # # 判断出生日期
    # def clean_birthday(self):
    #     # 从提交的数据中提取mobile数据
    #     birthday = self.cleaned_data.get('birthday')
    #     # 从数据库中读取该用户名是否存在
    #     now_date = datetime.date()
    #     #判断出生日期与当前时间
    #     if birthday > now_date:
    #         raise forms.ValidationError('出生日期不能小于当前日期!')
    #     else:
    #         return birthday


# 修改密码
class Update_passwordForm(forms.Form):
    old_password = forms.CharField(min_length=6, max_length=20, error_messages={
        'min_length': '密码不能小于6位',
        'max_length': '密码最大长度为16',
        'required': '密码不能为空'
    })
    new_password = forms.CharField(min_length=6, max_length=20, error_messages={
        'min_length': '密码不能小于6位',
        'max_length': '密码最大长度为16',
        'required': '密码不能为空'
    })
    repassword = forms.CharField(min_length=6, max_length=20, error_messages={
        'min_length': '密码不能小于6位',
        'max_length': '密码最大长度为16',
        'required': '密码不能为空'
    })

    # 判断账号是否存在
    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        old_password = set_password(old_password)
        old_password = Users.objects.filter(password=old_password).exists()
        #判断用户输入的密码和数据库的密码是否一致
        if old_password:
            return old_password
        else:
            raise forms.ValidationError('输入用户旧密码错误！')

    # 判断两次密码是否一致
    def clean(self):
        pwd = self.cleaned_data.get('new_password')
        repwd = self.cleaned_data.get('repassword')
        if pwd and repwd and pwd != repwd:
            raise forms.ValidationError({'repassword': '两次密码不一致'})
        else:
            return self.cleaned_data



# 注册密码检验
class ForgetModelForm(forms.ModelForm):
    password = forms.CharField(min_length=8, max_length=20, error_messages={
        'min_length': '密码不能小于8位',
        'max_length': '密码最大长度为16',
        'required': '密码不能为空'
    })
    repassword = forms.CharField(min_length=8, max_length=20, error_messages={
        'min_length': '密码不能小于8位',
        'max_length': '密码最大长度为16',
        'required': '密码不能为空'
    })

    # 验证码

    captcha = forms.CharField(max_length=6,
                              error_messages={
                                  'required': "验证码必须填写"
                              })
    class Meta:
        model = Users
        fields = ['mobile']
        error_messages = {
            'mobile': {
                'required': '号码不能为空',
            }
        }

    # 判断两次密码是否一致
    def clean(self):
        pwd = self.cleaned_data.get('password')
        repwd = self.cleaned_data.get('repassword')
        if pwd and repwd and pwd != repwd:
            raise forms.ValidationError({'repassword': '两次密码不一致'})
        else:
            return self.cleaned_data
