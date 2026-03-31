from django.urls import path
from Myapp.views import *

urlpatterns = [

    # ── Auth ──────────────────────────────
    path('',          login_view,   name='login'),
    path('logout/',   logout_view,  name='logout'),

    # ── Dashboard ─────────────────────────
    path('dashboard/', dashboard,   name='dashboard'),

    # ── Patient ───────────────────────────
    path('patients/',           patient_list,   name='patient_list'),
    path('patients/add/',       add_patient,    name='add_patient'),
    path('patients/edit/<int:pk>/', edit_patient, name='edit_patient'),
    path('patients/delete/<int:pk>/', delete_patient, name='delete_patient'),

    # ── Doctor ────────────────────────────
    path('doctors/',            doctor_list,    name='doctor_list'),
    path('doctors/add/',        add_doctor,     name='add_doctor'),
    path('doctors/edit/<int:pk>/',   edit_doctor,   name='edit_doctor'),
    path('doctors/delete/<int:pk>/', delete_doctor, name='delete_doctor'),

    # ── Appointment ───────────────────────
    path('appointments/',           appointment_list,   name='appointment_list'),
    path('appointments/add/',       add_appointment,    name='add_appointment'),
    path('appointments/cancel/<int:pk>/', cancel_appointment, name='cancel_appointment'),
    path('appointments/done/<int:pk>/',   done_appointment,   name='done_appointment'),

]
