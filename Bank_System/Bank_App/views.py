
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.core.mail import send_mail

# Create your views here.



def Signup_view(request):
    if request.method=='POST':
        a=signup(request.POST,request.FILES)
        if a.is_valid():
            fname=a.cleaned_data['firstname']
            lname=a.cleaned_data['lastname']
            ph=a.cleaned_data['phone']
            acc = int("1511"+str(ph))
            mail=a.cleaned_data['email']
            img=a.cleaned_data['image']
            pin=a.cleaned_data['password']
            repin=a.cleaned_data['confirm_password']
            if pin == repin:
                b=SignUp_model(firstname=fname,lastname=lname,phone=ph,email=mail,image=img,password=pin,account_number=acc,balance=0,confirm_password=repin)
                b.save()
                subject = "Your account has been created"
                message = f"Your New account number is{acc}"
                email_from = "skyviewwwww@gmail.com"
                email_to = mail
                send_mail(subject, message, email_from, [email_to])
                return redirect(banklogin)
            else:
                return HttpResponse("registration failed")
    return render(request,'sign up.html')


def banklogin(request):
    if request.method=='POST':
        a=login_form(request.POST)
        if a.is_valid():
            mail=a.cleaned_data['email']
            pn=a.cleaned_data['password']
            b=SignUp_model.objects.all()
            for i in b:
                if i.email==mail and i.password==pn:
                    request.session['id']=i.id
                    return redirect(PersonaInfo)
            else:
                return redirect(PasswordError)
    return render(request,'login.html')

def index(request):
    return render (request,'index.html')

def PersonaInfo(request):
    try:
        id1=request.session['id']
        a=SignUp_model.objects.get(id=id1)
        img = str(a.image).split('/')[-1]
        return render(request,'personal_info.html',{'a':a,'img':img})
    except:
        return redirect(banklogin)


def EditProfile(request,id):
    a=SignUp_model.objects.get(id=id)
    if request.method=='POST':
        a.firstname=request.POST.get('firstname')
        a.lastname=request.POST.get('lastname')
        a.phone=request.POST.get('phone')
        a.email=request.POST.get('email')
        a.save()
        return redirect(PersonaInfo)

    return render(request,'Edit_Profile.html',{'a':a})

def MoneyTransfer(request,id):
    a = SignUp_model.objects.get(id=id)
    return render(request,'Transfer.html',{'a':a})

def addAmount(request,id):
    a=SignUp_model.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('amount')
        request.session['am']=am
        a.balance+=int(am)
        a.save()
        b=add_amount(amount=am,uid=request.session['id'])
        b.save()
        pincode=request.POST.get('password')
        if int(pincode)==a.password:
            return redirect(Success)
        else:
            return HttpResponse("Failed")
    return render(request,'add amount.html')

def withdrawAmount(request,id):
    a=SignUp_model.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('amount')
        request.session['am']=am
        if (int(am)<=int(a.balance)):
            a.balance-=int(am)
            a.save()
            b = withdraw_amount(amount=am, uid=request.session['id'])
            b.save()
            pincode=request.POST.get('password')
            if int(pincode)==a.password:
                return redirect(Withdrawsuccess)
            else:
                return HttpResponse(InsufficientBalance)
    return render(request,'withdraw amount.html')

def send_Money_to_Account_number(request,id):
    a=SignUp_model.objects.get(id=id)
    b=SignUp_model.objects.all()
    if request.method=='POST':
        ac=request.POST.get('account_number')
        cacc=request.POST.get('confirm_account_number')
        am=request.POST.get('amount')
        pin=request.POST.get('password')
        if int(ac)==int(cacc):
            for i in b:
                if int(ac)==i.account_number and int(pin)==i.password:
                    if a.balance>int(am):
                        a.balance-=int(am)
                        i.balance+=int(am)
                        i.save()
                        a.save()
                        c=withdraw_amount(amount=am,uid=request.session['id'])
                        c.save()
                        return redirect(TransferSuccess)
                    else:
                        return redirect(InsufficientBalance)
                else:
                    return HttpResponse("User Not Found")
    return render(request,'send money account.html')


def Statement(request,id):
    a=SignUp_model.objects.get(id=id)
    pin=request.POST.get('password')
    if request.method=='POST':
        if int(pin)==a.password:
            choice=request.POST.get('statement')
            if choice=='deposit':
                return redirect(DepositeStatment)
            elif choice=='withdraw':
                return redirect(WithdrawStatement)
        else:
            return HttpResponse("incorrect password")
    return render(request,'statement.html')


def DepositeStatment(request):
    a=add_amount.objects.all()
    id=request.session['id']
    return render(request,'DepositStatement.html',{'a':a ,'id':id})

def WithdrawStatement(request):
    a=withdraw_amount.objects.all()
    id=request.session['id']
    return render(request,'WithdrawStatement.html',{'a':a,'id':id})

def Success(request):
    am=request.session['am']
    return render(request,'Success.html',{'am':am})

def Withdrawsuccess(request):
    am=request.session['am']
    return render(request,'withdraw added success.html',{'am':am})

def TransferSuccess(request):
    am=request.session['am']
    return render(request,'transferSuccess.html',{'a':am})

def InsufficientBalance(request):
    return render(request,'insufficientBalance.html')

def PasswordError(requuest):
    return render(requuest,'passworderror.html')


def forgetpassword(request):
    a = SignUp_model.objects.all()
    if request.method == 'POST':
        em = request.POST.get('email')
        acc = request.POST.get('account_number')
        for i in a:
            if i.email == em and i.account_number == int(acc):
                id = i.id
                subject = "Password Change"
                message = f"http://127.0.0.1:8000/Bank_App/changepassword/{id}"
                email_from = "skyviewwwww@gmail.com"
                email_to = em
                send_mail(subject, message, email_from, [email_to])
                return redirect(checkyourmail)
        return HttpResponse("Sorry, no matching account found")
    return render(request, 'ForgetPassword.html')

def changepassword(request,id):
    a=SignUp_model.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('pass1')
        p2=request.POST.get('pass2')
        if int(p1==p2):
            a.password=p1
            a.save()
            return redirect(passwordchangesuccess)
        else:
            HttpResponse("Oops Password doesn't match")

    return render(request,'ChangePassword.html')

def passwordchangesuccess(request):
    return render(request,'passwordchangesuccess.html')

def checkyourmail(request):
    return render(request,'checkyourmail.html')