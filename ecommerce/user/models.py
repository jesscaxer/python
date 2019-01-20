from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


# Create your models here.
# 用户表
# ID
# 手机号
# 昵称
# 密码
# 性别
# 学校
# 老家
# 添加时间
# 修改时间
# 是否删除

class Users(models.Model):
    mobile = models.CharField(max_length=11, unique=True, validators=[
        RegexValidator(r'1[35678]\d{9}')
    ], placeorder='手机号码')
    username = models.CharField(max_length=11, null=True, blank=True, validators=[
        MinLengthValidator(11)
    ])
    password = models.CharField(max_length=32, validators=[
        MinLengthValidator(32)])
    sex = models.CharField(max_length=5, choices=(('1', '男'), ('2', '女')), default='1')
    school = models.CharField(max_length=100, null=True, blank=True, validators=[
        MinLengthValidator(4)
    ])
    loction = models.CharField(max_length=100,  null=True, blank=True, validators=[
        MinLengthValidator(4)
    ])
    home = models.CharField(max_length=100,  null=True, blank=True, validators=[
        MinLengthValidator(4)
    ])
    add_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'

