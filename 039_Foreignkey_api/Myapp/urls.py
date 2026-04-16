from django.urls import path
from Myapp.views import *

urlpatterns = [
    path("Student/",StudentApi.as_view()),
    path("Student/<int:id>/",StudentApi.as_view())
]