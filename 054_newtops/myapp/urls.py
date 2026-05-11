from django.urls import path
from myapp.views import *


urlpatterns = [

    path("",user_register,name="register"),
    path("login",user_login,name="login"),
    path("index",user_index,name="index"),
    path("update/<int:id>/",user_update,name="update"),
    path("delete/<int:id>/",user_delete,name="delete"),
    path("get",get,name="get"),
    path("post",post,name="post"),
    path("put/<int:id>/",put,name="put"),
    path("delete/<int:id>/",delete,name="delete"),
    path("students",studentdeatils.as_view()),
    path("students/<int:id>/",Studentallview.as_view())
    

]

