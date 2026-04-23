from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path("",product_list,name="product_list"),
    path("update/<int:id>/",product_update,name="product_update"),
    path("delete/<int:id>/",product_delete,name="product_delete")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
