from django.shortcuts import render,redirect
from databaseApp.models import students_details
from databaseApp.forms import displaystudentform
from django.contrib import messages
# Create your views here.
def display_students(request):
    students=students_details.objects.all()
    context={
        'students':students
    }
    return render(request,"databaseApp/studentList.html",context)

def displaystudentinforms(request):
    form = displaystudentform()
    if request.method == 'POST':
        form=displaystudentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../studentdetails')
            messages.info(request,"record saved")
    return render(request,"databaseApp/studentform.html",{'form':form})

def deletestudent(request,id):
      student=students_details.objects.get(id=id)
      student.delete()
      return redirect('../../studentdetails')

def updatestudent(request,id):
    student=students_details.objects.get(id=id)
    # updatestudent={
    #     "ssno":student.sno,
    #     "ssname":student.sname,
    #     "ssaddress":student.saddress,

    # }
    if request.method == 'POST':
        student.sno= request.POST["sno"]
        student.sname= request.POST["sname"]
        student.saddress=request.POST["saddress"]
        student.save()
        return redirect('../../studentdetails')

        #   form=displaystudentform(request.POST,instance=student)
        #   if form.is_valid():
        #      form.save()
             
    return render(request,"databaseApp/update.html",{'student':student})

     
def titlepage(request):
    return render(request,"databaseApp/titlepage.html")

    
   
