from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "phone_number", "email", "created_at"]
    list_filter = ["national_id_number", "phone_number", "gender"]
    search_fields = ["national_id_number", "phone_number", "gender"]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
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
    list_display = ["id", "first_name", "phone_number", "email", "created_at"]
    list_filter = ["national_id_number", "phone_number", "gender"]
    search_fields = ["national_id_number", "phone_number", "shift"]


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_filter = ["name"]
    search_fields = ["name"]
