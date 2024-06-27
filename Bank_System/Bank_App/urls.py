from django.urls import path
from .views import *


urlpatterns=[
    path('index/',index),
    path('login/',banklogin),
    path('signup/',Signup_view),
    path('Personal_Info/',PersonaInfo),
    path('Edit Profile/<int:id>',EditProfile),
    path('Transfer/<int:id>',MoneyTransfer),
    path('Add Amount/<int:id>',addAmount),
    path('withdraw Amount/<int:id>',withdrawAmount),
    path('Send_Moneyto_Account/<int:id>',send_Money_to_Account_number),
    path('Statement/<int:id>',Statement),
    path('Deposite_Statement/',DepositeStatment),
    path('Withdraw_Statement/',WithdrawStatement),
    path('Success/',Success),
    path('WithdrawSuccess/',Withdrawsuccess),
    path('InsufficientBalance/',InsufficientBalance),
    path('PasswordError/',PasswordError),
    path('ForgetPassword/',forgetpassword),
    path('changepassword/<int:id>',changepassword),
    path('passwordchangesuccess/',passwordchangesuccess),
    path('checkyourmail/',checkyourmail)

]