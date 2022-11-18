from django.urls import path
from userApp import views

urlpatterns = [
    path("",views.userValidate,name="uservalidate"),
    path("loginuser/",views.loginuser,name="loginuser"),
]
    