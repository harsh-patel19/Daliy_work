from django.urls import path
from myapp.views import *

urlpatterns =[ 
    
    path("",Employees_list,name="Employees_list"),
    path("update/<int:id>/",Employees_update,name="Employees_update"),
    path("delete/<int:id>/",Employees_delete,name="Employees_delete")

]