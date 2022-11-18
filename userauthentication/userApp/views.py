from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import userForm
from .models import user
from django.http import HttpResponse


# Create your views here.
def userValidate(request):
    form = userForm()
    if request.method=='POST':
        form=userForm(request.POST)
        if request.POST["password"]==request.POST["confirmpassword"]:
            # form=userForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect("/loginuser")
        else:
            messages.warning(request,"passwords don't match")
            return render(request,"userApp/userregistrationform.html",{"form":form})
    return render(request,"userApp/userregistrationform.html",{"form":form})

def loginuser(request):
    if request.method=="POST":
        uname=request.POST['username']
        pwd=request.POST['password']
        loginuser=user.objects.filter(username=uname,password=pwd)
        if loginuser:
            messages.success(request,"logged in successfully")
            # return redirect("/loginuser")
            return render(request,"userApp/loginmessage.html")
        else:
            messages.info(request,"Enter valid credentials")   
            return redirect("/loginuser")
    return render(request,"userApp/loginuser.html")
