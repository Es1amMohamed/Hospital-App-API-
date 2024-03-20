from django.shortcuts import get_object_or_404, render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets


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


class DoctorViewSet(viewsets.ViewSet):
    """this class is used to create a pharmacist account and check if the email already exists"""

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


class SpecializationViewSet(viewsets.ModelViewSet):
    """this class is used to create a specialization and check if the specialization already exists"""

    serializer_class = SpecializationSerializer
    queryset = Specialization.objects.all()


@api_view(["GET"])
def get_patient_profile(request, pk):
    """
    this function will get the patient profile
    """

    patient = get_object_or_404(Patient, pk=pk)
    serializer = PatientProfileSerializer(patient)
    return Response(serializer.data)


class UpdatePatientProfileViewSet(viewsets.ModelViewSet):
    """this class is used to update a patient profile and check if the patient profile already exists"""

    serializer_class = UpdateProfilePatientSerializer
    queryset = Patient.objects.all()
