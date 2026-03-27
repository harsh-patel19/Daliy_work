from django.urls import path
from myapp.views import *
# from rest_framework.routers import DefaultRouter


# urlpatterns =[

#     path("student/",Studentlist.as_view()),
#     path("student/<int:id>/",StudenDeatils.as_view())
# ]

# urls.py

from rest_framework.routers import DefaultRouter
from myapp.views import *

router = DefaultRouter()
router.register('student', studentviewset)
router.register('Course', Courseviewset)



urlpatterns = router.urls
