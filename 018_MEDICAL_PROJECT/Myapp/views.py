from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Myapp.models import *


# ─────────────────────────────────────────
# AUTH VIEWS
# ─────────────────────────────────────────

def login_view(request):
    """Login page — POST se username/password check karo"""
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def logout_view(request):
    """Logout karo aur login page pe bhejo"""
    logout(request)
    return redirect('login')


# ─────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────

@login_required(login_url='login')
def dashboard(request):
    """Dashboard — counts aur recent patients"""
    context = {
        'total_patients':     Patient.objects.count(),
        'total_doctors':      Doctor.objects.count(),
        'total_appointments': Appointment.objects.count(),
        'admitted_today':     Patient.objects.filter(admission_type='IPD').count(),
        'recent_patients':    Patient.objects.order_by('-created_at')[:5],
    }
    return render(request, 'dashboard.html', context)


# ─────────────────────────────────────────
# PATIENT VIEWS
# ─────────────────────────────────────────

@login_required(login_url='login')
def patient_list(request):
    """Saare patients dikhao — search bhi karo"""
    search = request.GET.get('search', '')
    patients = Patient.objects.all().order_by('-created_at')

    if search:
        patients = patients.filter(first_name__icontains=search) | \
                   patients.filter(last_name__icontains=search)

    return render(request, 'patient_list.html', {
        'patients': patients,
        'search':   search,
    })


@login_required(login_url='login')
def add_patient(request):
    """Naya patient add karo"""
    doctors = Doctor.objects.filter(status='Available')

    if request.method == 'POST':
        Patient.objects.create(
            first_name     = request.POST.get('first_name'),
            last_name      = request.POST.get('last_name'),
            dob            = request.POST.get('dob'),
            gender         = request.POST.get('gender'),
            blood_group    = request.POST.get('blood_group', ''),
            phone          = request.POST.get('phone'),
            email          = request.POST.get('email', ''),
            address        = request.POST.get('address', ''),
            department     = request.POST.get('department'),
            doctor         = get_object_or_404(Doctor, pk=request.POST.get('doctor')),
            admission_type = request.POST.get('admission_type'),
            admission_date = request.POST.get('admission_date') or None,
            symptoms       = request.POST.get('symptoms', ''),
        )
        messages.success(request, 'Patient successfully added!')
        return redirect('patient_list')

    return render(request, 'add_patient.html', {'doctors': doctors})


@login_required(login_url='login')
def edit_patient(request, pk):
    """Patient ki details update karo"""
    patient = get_object_or_404(Patient, pk=pk)
    doctors = Doctor.objects.all()

    if request.method == 'POST':
        patient.first_name     = request.POST.get('first_name')
        patient.last_name      = request.POST.get('last_name')
        patient.dob            = request.POST.get('dob')
        patient.gender         = request.POST.get('gender')
        patient.blood_group    = request.POST.get('blood_group', '')
        patient.phone          = request.POST.get('phone')
        patient.email          = request.POST.get('email', '')
        patient.address        = request.POST.get('address', '')
        patient.department     = request.POST.get('department')
        patient.doctor         = get_object_or_404(Doctor, pk=request.POST.get('doctor'))
        patient.admission_type = request.POST.get('admission_type')
        patient.admission_date = request.POST.get('admission_date') or None
        patient.symptoms       = request.POST.get('symptoms', '')
        patient.save()
        messages.success(request, 'Patient updated successfully!')
        return redirect('patient_list')

    return render(request, 'add_patient.html', {
        'patient': patient,
        'doctors': doctors,
    })


@login_required(login_url='login')
def delete_patient(request, pk):
    """Patient delete karo"""
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    messages.success(request, 'Patient deleted.')
    return redirect('patient_list')


# ─────────────────────────────────────────
# DOCTOR VIEWS
# ─────────────────────────────────────────

@login_required(login_url='login')
def doctor_list(request):
    """Saare doctors dikhao"""
    doctors = Doctor.objects.all().order_by('name')
    return render(request, 'doctor_list.html', {'doctors': doctors})


@login_required(login_url='login')
def add_doctor(request):
    """Naya doctor add karo"""
    if request.method == 'POST':
        Doctor.objects.create(
            name           = request.POST.get('name'),
            specialization = request.POST.get('specialization'),
            phone          = request.POST.get('phone'),
            email          = request.POST.get('email'),
            experience     = request.POST.get('experience'),
            status         = request.POST.get('status', 'Available'),
        )
        messages.success(request, 'Doctor added successfully!')
        return redirect('doctor_list')

    return render(request, 'add_doctor.html')


@login_required(login_url='login')
def edit_doctor(request, pk):
    """Doctor details update karo"""
    doctor = get_object_or_404(Doctor, pk=pk)

    if request.method == 'POST':
        doctor.name           = request.POST.get('name')
        doctor.specialization = request.POST.get('specialization')
        doctor.phone          = request.POST.get('phone')
        doctor.email          = request.POST.get('email')
        doctor.experience     = request.POST.get('experience')
        doctor.status         = request.POST.get('status')
        doctor.save()
        messages.success(request, 'Doctor updated!')
        return redirect('doctor_list')

    return render(request, 'add_doctor.html', {'doctor': doctor})


@login_required(login_url='login')
def delete_doctor(request, pk):
    """Doctor delete karo"""
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    messages.success(request, 'Doctor deleted.')
    return redirect('doctor_list')


# ─────────────────────────────────────────
# APPOINTMENT VIEWS
# ─────────────────────────────────────────

@login_required(login_url='login')
def appointment_list(request):
    """Saari appointments dikhao"""
    appointments = Appointment.objects.all().order_by('-date', '-time')
    patients     = Patient.objects.all()
    doctors      = Doctor.objects.all()

    return render(request, 'appointments.html', {
        'appointments': appointments,
        'patients':     patients,
        'doctors':      doctors,
    })


@login_required(login_url='login')
def add_appointment(request):
    """Nayi appointment book karo"""
    if request.method == 'POST':
        Appointment.objects.create(
            patient = get_object_or_404(Patient, pk=request.POST.get('patient')),
            doctor  = get_object_or_404(Doctor,  pk=request.POST.get('doctor')),
            date    = request.POST.get('date'),
            time    = request.POST.get('time'),
            reason  = request.POST.get('reason', ''),
            status  = 'Pending',
        )
        messages.success(request, 'Appointment booked!')
    return redirect('appointment_list')


@login_required(login_url='login')
def cancel_appointment(request, pk):
    """Appointment cancel karo"""
    appt = get_object_or_404(Appointment, pk=pk)
    appt.status = 'Cancelled'
    appt.save()
    messages.success(request, 'Appointment cancelled.')
    return redirect('appointment_list')


@login_required(login_url='login')
def done_appointment(request, pk):
    """Appointment done mark karo"""
    appt = get_object_or_404(Appointment, pk=pk)
    appt.status = 'Done'
    appt.save()
    messages.success(request, 'Appointment marked as done.')
    return redirect('appointment_list')
