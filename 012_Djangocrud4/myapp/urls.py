from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *


urlpatterns =[
    path("",student_list,name="student_list"),
    path("update/<int:id>/",student_update,name="student_update"),
    path("delete/<int:id>/",student_delete,name="student_delete"),
    path('students/',StudentList.as_view()),
    path('students/<int:pk>/',StudentDetails.as_view())
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)