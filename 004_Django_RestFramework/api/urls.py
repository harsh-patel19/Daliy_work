from django.urls import path
from api.views import *

urlpatterns =[
    path('students/',StudentList.as_view()),
    path('students/<int:pk>/',StudentDetails.as_view())
]