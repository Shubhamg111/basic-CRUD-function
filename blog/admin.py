from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Students)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display=['name','address']
    search_fields=['name','address']

@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display=['name','address']
    search_fields=['name','address']