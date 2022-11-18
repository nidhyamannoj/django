from django.contrib import admin
from .models import user

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list=['username','password','confirmpassword']
admin.site.register(user,userAdmin)


