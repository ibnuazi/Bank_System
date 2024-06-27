
from django import forms

# class login(forms.Form):
class signup(forms.Form):
    firstname=forms.CharField(max_length=200)
    lastname=forms.CharField(max_length=200)
    phone=forms.CharField(max_length=12)
    email=forms.EmailField()
    image=forms.FileField()
    password=forms.IntegerField()
    confirm_password=forms.IntegerField()

class login_form(forms.Form):
    email=forms.EmailField()
    password=forms.IntegerField()
