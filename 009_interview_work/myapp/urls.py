from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('update/<int:id>/', product_update, name='product_update'),
    path('delete/<int:id>/', product_delete, name='product_delete'),
]