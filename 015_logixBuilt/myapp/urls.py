from django.urls import path
from myapp.views import *

urlpatterns = [
    path("students/",student_list),
    path("students/<int:pk>/",student_deatils)
]