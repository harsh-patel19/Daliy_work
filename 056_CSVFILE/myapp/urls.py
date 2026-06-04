from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",home,name="home"),
    path("update/<int:id>/",update,name="update"),
    path("delete/<int:id>/",user_delete,name="delete")
    
]