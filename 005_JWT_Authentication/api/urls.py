from django.urls import path
from api.views import *

urlpatterns =[
    path('posts/',post_list,name="post_list")
]
