from rest_framework import serializers
from .models import *


class PatientSerializer(serializers.ModelSerializer):
    """this class will create the serializer of the patient model"""

    class Meta:
        model = Patient
        exclude = ["id", "slug", "created_at"]


class DoctorSerializer(serializers.ModelSerializer):
    """this class will create the serializer of the doctor model"""

    specialization_id = serializers.PrimaryKeyRelatedField(
        queryset=Specialization.objects.all(), source="specialization", write_only=True
    )

    class Meta:
        model = Doctor
        exclude = ["id", "slug", "created_at", "specialization"]

    def create(self, validated_data):
        """in this function we will create the specialization of the doctor"""
        specialization_id = validated_data.pop("specialization_id", None)
        if specialization_id:
            validated_data["specialization"] = specialization_id
        return super().create(validated_data)


class PharmacistSerializer(serializers.ModelSerializer):
    """this class will create the serializer of the pharmacist model"""

    class Meta:
        model = Pharmacist
        exclude = ["id", "slug", "created_at"]


class SpecializationSerializer(serializers.ModelSerializer):
    """this class will create the serializer of the specialization model"""

    class Meta:
        model = Specialization
        exclude = ["id", "slug", "created_at"]


class PatientProfileSerializer(serializers.ModelSerializer):
    """this class will create the serializer of the patient profile model"""

    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "address", "email", "gender", "blood_type"]


class UpdateProfilePatientSerializer(serializers.ModelSerializer):
    """
    this class will create the serializer of the patient model
    to check if the patient profile already
    exists and update it

    """

    class Meta:
        model = Patient
        exclude = ["id", "slug", "created_at", "password", "password_confirmation"]
