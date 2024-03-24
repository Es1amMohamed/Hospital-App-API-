from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


app_name = "accounts"
router = DefaultRouter()
router.register(
    "doctor_signup", views.DoctorViewSet, basename="doctor_signup"
)  # this endpoint is used to create a doctor account
router.register(
    "pharmacist_signup", views.PharmacistViewSet, basename="Pharmacist_signup"
)  # this endpoint is used to create a pharmacist account
router.register(
    "specialization", views.SpecializationViewSet, basename="specialization"
)  # this endpoint is used to create a specialization
router.register(
    "update/profile",
    views.UpdatePatientProfileViewSet,
    basename="update_patient_profile",
)  # this endpoint is used to update a patient profile

router.register(
    "update/doctor/profile",
    views.UpdateDoctorProfileViewSet,
    basename="update_doctor_profile",
)

router.register(
    "update/pharmacist/profile",
    views.UpdatePharmacistProfileViewSet,
    basename="update_pharmacist_profile",
)

urlpatterns = [
    path(
        "signup/", views.signup, name="signup"
    ),  # this endpoint is used to create a new account
    path("", include(router.urls)),
    path("patient/login/", views.patient_login, name="login"),
    path(
        "doctor/login/",
        views.DoctorViewSet.as_view({"post": "login"}),
        name="doctor_login",
    ),
    path(
        "pharmacist/login/",
        views.PharmacistViewSet.as_view({"post": "login"}),
        name="pharmacist_login",
    ),
]
