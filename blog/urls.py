
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login,name='login'),
    path('delete/<id>',views.delete,name='delete'),
    path('edit/<id>',views.edit,name='edit'),

    path('teacher',views.teacher,name='teacher'),
    path('addteacher',views.addteacher,name='addteacher'),



    # path('gallery/<id>',views.gallery),

    
 

]
