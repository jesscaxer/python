from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Users(models.Model):
    mobile = models.CharField(max_length=11, validators=[
        MinLengthValidator(11)
    ])
    password = models.CharField(max_length=32)
    isdelete = models.BooleanField(default=False)
    addtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

