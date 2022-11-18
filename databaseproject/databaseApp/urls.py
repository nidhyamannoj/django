from django.urls import path
from databaseApp import views

urlpatterns=[
path('studentdetails/',views.display_students,name="display_students"),
path('studentdetailsform/',views.displaystudentinforms,name="displaystudentinforms"),
path('studentdetails/delete/<id>',views.deletestudent,name="deletestudent"),
path('studentdetails/update/<id>',views.updatestudent,name="updatestudent"),
path("",views.titlepage,name="titlepage"),
]