from django import forms
from userApp.models import user

class userForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-Control","placeholder":"Enter UserName","autofocus":"autofocus"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-Control","placeholder":"Enter password"}))
    confirmpassword=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-Control","placeholder":"confirm password"}))
    class Meta:
        model=user
        fields='__all__'