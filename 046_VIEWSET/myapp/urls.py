from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products',ProductViewset)

urlpatterns = router.urls

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)