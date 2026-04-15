from django.urls import path
from Myapp.views import *

urlpatterns = [
    path("",student_list,name="student_list"),
    path("update/<int:id>/",student_update,name="student_update"),
    path("delete/<int:id>/",student_delete,name="student_delete"),
    path("student/",StudentDeatils.as_view()),
    path("student/<int:id>/",Studentlist.as_view())
]