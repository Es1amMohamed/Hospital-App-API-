from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """this class will create the admin panel of the patient model"""

    list_display = ["id", "first_name", "phone_number", "email", "created_at"]
    list_filter = ["national_id_number", "phone_number", "gender"]
    search_fields = ["national_id_number", "phone_number", "gender"]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """this class will create the admin panel of the doctor model"""

    list_display = ["id", "first_name", "phone_number", "email", "created_at"]
    list_filter = ["national_id_number", "phone_number", "gender"]
    search_fields = [
        "national_id_number",
        "phone_number",
        "graduation_year",
        "membership_no",
    ]


@admin.register(Pharmacist)
class PharmacistAdmin(admin.ModelAdmin):
    """this class will create the admin panel of the pharmacist model"""

    list_display = ["id", "first_name", "phone_number", "email", "created_at"]
    list_filter = ["national_id_number", "phone_number", "gender"]
    search_fields = ["national_id_number", "phone_number", "shift"]


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    """this class will create the admin panel of the specialization model"""

    list_display = ["id", "name"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    """this class will create the admin panel of the patient profile model"""

    list_display = ["id", "Patient_name"]
    list_filter = ["Patient_name"]
    search_fields = ["Patient_name"]


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    """this class will create the admin panel of the doctor profile model"""

    list_display = ["id", "doctor_name"]
    list_filter = ["doctor_name"]
    search_fields = ["doctor_name"]


@admin.register(PharmacistProfile)
class PharmacistProfileAdmin(admin.ModelAdmin):
    """this class will create the admin panel of the pharmacist profile model"""

    list_display = ["id", "pharmacist_name"]
    list_filter = ["pharmacist_name"]
    search_fields = ["pharmacist_name"]
