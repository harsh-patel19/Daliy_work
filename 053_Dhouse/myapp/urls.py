from django.urls import path
from myapp.views import *
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns =[
    # path("",get,name="get"),
    # path("post",post,name="post")
    path("",user_regitser,name="regitser"),
    path("login",user_login,name="login"),
    path("index",user_index,name="index"),
    path("update/<int:id>/",user_update,name="update"),
    path("delete/<int:id>/",user_delete,name="delete"),
    path('students/',Studentview.as_view()),
    path("students/<int:id>/",Studentdeatils.as_view())

]