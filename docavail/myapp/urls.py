from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path("login/",views.login, name='login'),
    path('register/',views.register,name='register'),
    path('patient/',views.ureg,name='patient'),
    path('Logout/',views.Logout,name='Logout'),
    path('dhome/',views.dhome,name='dhome'),
]