from django.urls import path,include
from rest_framework.routers import DefaultRouter
from myapp.views import *

router = DefaultRouter()
router.register('students',Studentviewset)

urlpatterns =[
    path("",include(router.urls))
]