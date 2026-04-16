from django.urls import path
from Myapp.views import *

urlpatterns = [
    path('get/', get, name='get_students'),
    path('post/', post, name='create_student'),
    path('put/<int:id>/', put, name='update_student'),
    path('patch/<int:id>/', patch, name='partial_update_student'),
    path('delete/<int:id>/', delete, name='delete_student'),
    path("students/",studentview.as_view()),
    path("students/<int:id>/",Studentdetails.as_view())
]