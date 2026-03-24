from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("",product_list,name="product_list"),
    path("update/<int:id>/",product_update,name="product_update"),
    path("delete<int:id>/",product_delete,name="product_delete"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)