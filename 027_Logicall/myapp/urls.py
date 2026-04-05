from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path("",student_list,name="student_list"),
    path("update/<int:id>/",student_update,name="student_update"),
    path("delete/<int:id>/",student_delete,name="student_delete"),
    path("student/",Studentview.as_view()),
    path("student/<int:id>/",Studentdetails.as_view())

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

