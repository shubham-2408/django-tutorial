from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name ='home'),
    path('portfolio/',views.index , name= 'index'),
    path('job/',views.job)

]