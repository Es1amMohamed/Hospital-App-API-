from rest_framework import serializers
from .models import *


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ["id", "slug", "created_at"]


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ["id", "slug", "created_at"]


class PharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist
        exclude = ["id", "slug", "created_at"]


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        exclude = ["id", "slug", "created_at"]
