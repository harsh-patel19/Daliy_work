from django.urls import path
from myapp.views import *

urlpatterns =[
    path("student/",Studentview.as_view()),
    path("student/<int:id>/",StudentDeatils.as_view())
]