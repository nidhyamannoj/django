from django.contrib import admin
from databaseApp.models import students_details

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list=['sno','sname','saddress','doj']
admin.site.register(students_details,studentAdmin)