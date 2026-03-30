from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("student",StudentView.as_view()),
    # path("student/<int:id>/",Studentdeatils.as_view())
    path("",student_list,name="student_list"),
    path("update/<int:id>/",student_update,name="update"),
    path("delet/<int:id>/",student_delete,name="delete")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)