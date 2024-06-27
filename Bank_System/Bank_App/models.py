from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SignUp_model(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    phone=models.CharField(max_length=12)
    account_number=models.IntegerField()
    email=models.EmailField()
    image=models.FileField(upload_to='Bank_App/static')
    password=models.IntegerField()
    confirm_password=models.IntegerField()
    balance=models.IntegerField()
    def __str__(self):
        return self.lastname

class add_amount(models.Model):
    uid = models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.uid

class withdraw_amount(models.Model):
    uid = models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.uid

class sendMoney(models.Model):
    uid=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.uid,self.amount

