from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', home, name='home'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('add-employee/', add_employee, name='add_employee'),
    path('update-employee/<int:id>/', update_employee, name='update_employee'),
    path('delete-employee/<int:id>/', delete_employee, name='delete_employee'),
    path('api', employee_api,name='api'),
]