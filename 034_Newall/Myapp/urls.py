from django.urls import path
from Myapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",Employees_list,name="Employees_list"),
    path("update/<int:id>/",Employees_update,name="Employees_update"),
    path("delete/<int:id>/",Employees_delete,name="Employees_delete")
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
