from django.urls import path
from myapp.views import *

urlpatterns = [
    # AUTH
    path('', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('student/', student_list, name='list'),
    path('create/', student_create, name='student_create'),
    path('update/<int:id>/', student_update, name='update'),
    path('delete/<int:id>/', student_delete, name='delete')
]