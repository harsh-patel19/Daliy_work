from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from myapp.views import *

urlpatterns = [
    # path("product/",productdeatils.as_view()),
    # path("product/<int:id>/",Productall.as_view())

    path("",user_reg,name="register"),
    path("login",user_login,name="login"),
    path("home",user_home,name="home"),
    path("update/<int:id>/",user_update,name="update"),
    path("delete/<int:id>/",user_delete,name="delete")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)