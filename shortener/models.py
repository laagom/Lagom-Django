from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)


class Users(AbstractUser):
    full_name = models.CharField(max_length=30, null=True)
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING, null=True)



class User(models.Model):
    ''' 커스텀 커맨드를 위한 모델 생성 '''
    name = models.CharField(max_length=128, help_text="사용자 이름")
    content = models.TextField(max_length=1024, help_text="사용자 설명")
