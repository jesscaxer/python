from datetime import date

from django import forms
from django.http import HttpResponse

from user import encrption_pwd
from user.models import Users



# 注册密码检验
class RegisterModelForm(forms.ModelForm):
    password = forms.CharField(min_length=8, max_length=20, error_messages={
        'min_length': '密码不能小于6位',
        'max_length': '密码最大长度为16',
        'required': '密码不能为空'
    })
    repassword = forms.CharField(min_length=8, max_length=20, error_messages={
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


     # 判断用户名是否存在
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        flag = Users.objects.filter(mobile=mobile).exists()
        if flag:
            raise forms.ValidationError({'mobile': '用户已存在'})

        else:
            return mobile

    # 判断两次密码是否一致
    def clean(self):
        pwd = self.cleaned_data.get('password')
        repwd = self.cleaned_data.get('repassword')
        if pwd and repwd and pwd != repwd:
            raise forms.ValidationError({'repwd': '两次密码不一致'})
        else:
            return self.cleaned_data


