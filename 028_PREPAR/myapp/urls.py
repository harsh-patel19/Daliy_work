from django.urls import path
from myapp.views import *

urlpatterns =[

    path("student/",Studentlist.as_view()),
    path("student/<int:id>/",Studentdetails.as_view())
]