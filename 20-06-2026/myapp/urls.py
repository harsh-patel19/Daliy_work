from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urls import *
urlpatterns = [

    path("",user_register,name="register"),
    path("login",user_login,name="login"),
    path("home",home,name="home"),
    path("update/<int:id>/",user_update,name="update"),
    path("delete/<int:id>/",user_delete,name="delete"),
    path("product",ProductALL.as_view()),
    path("product/<int:id>/",Productalldetails.as_view())
    
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)