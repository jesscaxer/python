# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-21 13:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_show', models.CharField(blank=True, max_length=50, null=True, verbose_name='头像')),
                ('mobile', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('1[35678]\\d{9}')], verbose_name='手机号码')),
                ('username', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='用户名')),
                ('password', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(32)], verbose_name='密码')),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=1, verbose_name='性别')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('school', models.CharField(blank=True, max_length=50, null=True, verbose_name='学校')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='地址')),
                ('home', models.CharField(blank=True, max_length=100, null=True, verbose_name='家庭所在地')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='更改时间')),
                ('isdelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
