from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path("",user_login,name="user_login"),
    path("user_logout",user_logout,name="user_logout"),
    path("register",register,name="register"),
    path("student_list",student_list,name="student_list"),
    path("update/<int:id>/",student_update,name="student_update"),
    path("delete/<int:id>/",student_delete,name="student_delete")
    

]
urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)