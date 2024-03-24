from django.shortcuts import get_object_or_404, render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated


@api_view(["POST"])
def signup(request):
    """
    this function will create a new account
    """

    data = request.data
    user = PatientSerializer(data=data)

    if user.is_valid():
        if not Patient.objects.filter(email=data["email"]).exists():
            user = Patient.objects.create(
                user_name=data["user_name"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                password=data["password"],
                password_confirmation=data["password_confirmation"],
                national_id_number=data["national_id_number"],
                address=data["address"],
                phone_number=data["phone_number"],
                blood_type=data["blood_type"],
                gender=data["gender"],
                age=data["age"],
            )

            return Response(
                "message: Account created successfully", status=status.HTTP_201_CREATED
            )

        else:
            return Response(
                "message: Email already exists", status=status.HTTP_400_BAD_REQUEST
            )

    else:
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def patient_login(request):
    """
    this function will login the patient and return the patient profile
    """

    data = request.data
    patient = Patient.objects.filter(email=data["email"]).first()

    if patient is not None and check_password(data["password"], patient.password):
        serializer = ProfilePatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(
            "message: Invalid credentials", status=status.HTTP_400_BAD_REQUEST
        )


class DoctorViewSet(viewsets.ViewSet):
    """this class is used to create a Doctor account and check if the email already exists"""

    def create(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            if not Doctor.objects.filter(email=email).exists():
                serializer.save()
                return Response(
                    "message: Account created successfully, Wait for approval",
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    "message: Email already exists", status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request):
        """
        this function will login the doctor and return the doctor data
        """

        data = request.data
        doctor = Doctor.objects.filter(email=data["email"]).first()

        if (
            doctor is not None
            and check_password(data["password"], doctor.password)
            and doctor.active
        ):
            serializer = DoctorProfileSerializer(doctor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                "message: Invalid credentials", status=status.HTTP_400_BAD_REQUEST
            )


class PharmacistViewSet(viewsets.ViewSet):
    """this class is used to create a pharmacist account and check if the email already exists"""

    def create(self, request):
        serializer = PharmacistSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            if not Pharmacist.objects.filter(email=email).exists():
                serializer.save()
                return Response(
                    "message: Account created successfully, Wait for approval",
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    "message: Email already exists", status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request):
        """
        this function will login the pharmacist and return the pharmacist data
        """

        data = request.data
        pharmacist = Pharmacist.objects.filter(email=data["email"]).first()

        if (
            pharmacist is not None
            and check_password(data["password"], pharmacist.password)
            and pharmacist.active
        ):
            serializer = PharmacistProfileSerializer(pharmacist)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                "message: Invalid credentials", status=status.HTTP_400_BAD_REQUEST
            )


class SpecializationViewSet(viewsets.ModelViewSet):
    """this class is used to create a specialization and check if the specialization already exists"""

    serializer_class = SpecializationSerializer
    queryset = Specialization.objects.all()


class UpdatePatientProfileViewSet(viewsets.ModelViewSet):
    """this class is used to update a patient profile and check if the patient profile already exists"""

    serializer_class = ProfilePatientSerializer
    queryset = Patient.objects.all()


class UpdateDoctorProfileViewSet(viewsets.ModelViewSet):
    """this class is used to update a doctor profile and check if the doctor profile already exists"""

    serializer_class = DoctorProfileSerializer
    queryset = Doctor.objects.all()


class UpdatePharmacistProfileViewSet(viewsets.ModelViewSet):
    """this class is used to update a pharmacist profile and check if the pharmacist profile already exists"""

    serializer_class = PharmacistProfileSerializer
    queryset = Pharmacist.objects.all()
