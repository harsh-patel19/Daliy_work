from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from myapp.views import *

urlpatterns = [
    path("", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("student_list",student_list,name="student_list"),
    path("update/<int:id>/",student_update,name="student_update"),
    path("delete/<int:id>/",student_delete,name="student_delete"),
    path("students/",studentlist.as_view()),
    path("students/<int:id>/",studentdeatils.as_view()),
    path("api/register/",RegisterApi.as_view()),
    path("api/login/",LoginApi.as_view())

]

urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)