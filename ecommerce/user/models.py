from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


# Create your models here.
# 用户表
# ID
# 手机号
# 昵称
# 密码
# 性别
# 生日
# 学校
# 老家
# 添加时间
# 修改时间
# 是否删除

class Users(models.Model):
    head_show = models.ImageField(upload_to="head/%Y%m", default="head/head_show.jpg", verbose_name="用户头像")
    mobile = models.CharField(max_length=11, unique=True, validators=[
        RegexValidator(r'1[35789]\d{9}')
    ], verbose_name='手机号码')
    username = models.CharField(max_length=20, null=True, blank=True, validators=[
        MinLengthValidator(1)
    ], verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    sex = models.CharField(max_length=1, choices=(('1', '男'), ('2', '女')), default='1', null=True, blank=True, verbose_name='性别')
    birthday = models.DateField(null=True, blank=True, verbose_name='生日')
    school = models.CharField(max_length=50, null=True, blank=True, verbose_name='学校')
    location = models.CharField(max_length=100,  null=True, blank=True, verbose_name='地址')
    home = models.CharField(max_length=100,  null=True, blank=True, verbose_name='家庭所在地')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='更改时间')
    isdelete = models.BooleanField(default=False, verbose_name='是否删除')
    class Meta:
        db_table = 'users'

