from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from COFFEEAPP.views import *

urlpatterns = [
    path("",index,name="index"),
    path("about",about,name="about"),
    path("admin",admin,name="admin"),
    path("booking",booking,name="booking"),
    path("cart",cart,name="cart"),
    path("chatbot",chatbot,name="chatbot"),
    path("contact",contact,name="contact"),
    path("login",login,name="login"),
    path("menu",menu,name="menu"),
    path("order",order,name="order"),
    path("reviews",reviews,name="reviews"),
    path("suggestions",suggestions,name="suggestions")

]


urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)