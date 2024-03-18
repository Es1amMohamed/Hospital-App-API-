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

urlpatterns = [
    path(
        "signup/", views.signup, name="signup"
    ),  # this endpoint is used to create a new account
    path("", include(router.urls)),
]
