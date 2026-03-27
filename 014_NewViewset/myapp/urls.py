# urls.py

from rest_framework.routers import DefaultRouter
from myapp.views import *

router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('courses', CourseViewSet)
router.register('employee',EmployeeViewSet)

urlpatterns = router.urls