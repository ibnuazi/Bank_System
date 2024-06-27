from django.contrib import admin
from .models import *


admin.site.register(SignUp_model),
admin.site.register(add_amount),
admin.site.register(withdraw_amount),
admin.site.register(sendMoney)

# Register your models here.
