
from django import forms
from databaseApp.models import students_details

class displaystudentform(forms.ModelForm):
    class Meta:
        model=students_details
        fields='__all__'