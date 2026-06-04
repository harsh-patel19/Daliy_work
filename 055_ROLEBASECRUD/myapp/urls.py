from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

     path('', home, name='home'),

    path('register/', register, name='register'),

    path('login/', user_login, name='login'),

    path('logout/', user_logout, name='logout'),

    path('update/<int:id>/',update, name='update'),

    path('delete/<int:id>/',delete, name='delete'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)