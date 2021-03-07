from django.contrib import admin
from studentapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    l=['name','number','marks','place']
admin.site.register(Student,StudentAdmin)
