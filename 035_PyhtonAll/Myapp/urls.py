from django.urls import path
from Myapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",employees_list,name="employees_list"),
    path("update/<int:id>/",employee_update,name="employee_update"),
    path("delete/<int:id>/",employee_delete,name="employee_delete"),
    path("employee",Employeeslist.as_view()),
    path("employee/<int:id>/",EmployeesDeatils.as_view())
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)