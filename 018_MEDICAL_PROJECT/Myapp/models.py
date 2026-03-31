from django.db import models

# Create your models here.
class Doctor(models.Model):
 
    SPECIALIZATION_CHOICES = [
        ('Cardiology',   'Cardiology'),
        ('Neurology',    'Neurology'),
        ('Orthopedics',  'Orthopedics'),
        ('Gynecology',   'Gynecology'),
        ('Pediatrics',   'Pediatrics'),
        ('General',      'General'),
        ('ENT',          'ENT'),
        ('Dermatology',  'Dermatology'),
    ]
 
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Busy',      'Busy'),
    ]
 
    name           = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES)
    phone          = models.CharField(max_length=15)
    email          = models.EmailField(unique=True)
    experience     = models.PositiveIntegerField(help_text="Experience in years")
    status         = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    created_at     = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"
 
 
# ───────────────────────────
# PATIENT MODEL
# ───────────────────────────
class Patient(models.Model):
 
    GENDER_CHOICES = [
        ('Male',   'Male'),
        ('Female', 'Female'),
        ('Other',  'Other'),
    ]
 
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]
 
    ADMISSION_TYPE_CHOICES = [
        ('OPD',       'OPD (Outpatient)'),
        ('IPD',       'IPD (Inpatient)'),
        ('Emergency', 'Emergency'),
    ]
 
    DEPARTMENT_CHOICES = [
        ('Cardiology',  'Cardiology'),
        ('Neurology',   'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('Gynecology',  'Gynecology'),
        ('Pediatrics',  'Pediatrics'),
        ('General',     'General'),
        ('ENT',         'ENT'),
    ]
 
    # Personal Details
    first_name     = models.CharField(max_length=50)
    last_name      = models.CharField(max_length=50)
    dob            = models.DateField(verbose_name="Date of Birth")
    gender         = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group    = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES, blank=True)
    phone          = models.CharField(max_length=15)
    email          = models.EmailField(blank=True)
    address        = models.TextField(blank=True)
 
    # Medical Details
    department     = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    doctor         = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='patients')
    admission_type = models.CharField(max_length=20, choices=ADMISSION_TYPE_CHOICES, default='OPD')
    admission_date = models.DateField(null=True, blank=True)
    symptoms       = models.TextField(blank=True)
 
    created_at     = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
 
 
# ───────────────────────────
# APPOINTMENT MODEL
# ───────────────────────────
class Appointment(models.Model):
 
    STATUS_CHOICES = [
        ('Pending',   'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Done',      'Done'),
    ]
 
    patient    = models.ForeignKey(Patient,     on_delete=models.CASCADE, related_name='appointments')
    doctor     = models.ForeignKey(Doctor,      on_delete=models.CASCADE, related_name='appointments')
    date       = models.DateField()
    time       = models.TimeField()
    reason     = models.CharField(max_length=200, blank=True)
    status     = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.patient} → Dr.{self.doctor.name} on {self.date}"