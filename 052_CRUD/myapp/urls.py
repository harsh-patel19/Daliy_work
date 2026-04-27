from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    
    path("",user_register,name="register"),
    path("login",user_login,name="login"),
    path("logout",user_logout,name="logout"),
    path("student",home,name="student_list"),
    path("update/<int:id>/",user_update,name="update"),
    path("delete/<int:id>/",user_delete,name="delete")


]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
