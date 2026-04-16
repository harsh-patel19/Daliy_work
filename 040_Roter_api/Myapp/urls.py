from Myapp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students',StudentViweset)

urlpatterns = router.urls



