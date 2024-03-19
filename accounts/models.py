from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
]

SHIFT = [
    ("Morning", "Morning"),
    ("Evening", "Evening"),
]


class Patient(models.Model):
    """
    in this model we will create the patient table in the database,
    and we will define the fields of the table.

    """

    user_name = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(validators=[MinLengthValidator(8)], max_length=100)
    password_confirmation = models.CharField(
        validators=[MinLengthValidator(8)], max_length=100
    )
    national_id_number = models.CharField(max_length=14, unique=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, unique=True)
    blood_type = models.CharField(max_length=5)
    gender = models.CharField(max_length=6, choices=GENDER)
    age = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        """
        this class will define the ordering of the patient

        """

        ordering = ["-created_at"]
        verbose_name_plural = "patients"
        verbose_name = "patient"

    def __str__(self):
        """
        this function will return the user_name of the patient in the admin panel

        """
        return self.user_name

    def clean(self):
        """
        this function will check if the password and password_confirmation are the same
        and if the age is not empty

        """

        if self.password != self.password_confirmation:
            raise ValidationError("passwords do not match")

        if not self.age:
            raise ValidationError("Age is required")

    def save(self, *args, **kwargs):
        """
        this function will save the password and password_confirmation in the database
        and will create the slug of the user_name

        """

        if not self.pk:
            self.password = make_password(self.password)
            self.password_confirmation = make_password(self.password_confirmation)

        if not self.slug:
            self.slug = slugify(self.user_name)

        super(Patient, self).save(*args, **kwargs)


class Doctor(models.Model):
    """
    in this model we will create the doctor table in the database,
    and we will define the fields of the table.

    """

    user_name = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(validators=[MinLengthValidator(8)], max_length=100)
    password_confirmation = models.CharField(
        validators=[MinLengthValidator(8)], max_length=100
    )
    specialization = models.ForeignKey(
        "Specialization", on_delete=models.PROTECT, related_name="doctor_specialty"
    )
    national_id_number = models.CharField(max_length=14, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=200)
    membership_no = models.CharField(max_length=30, unique=True)
    graduation_year = models.IntegerField(
        validators=[MinValueValidator(1970), MaxValueValidator(2024)]
    )
    gender = models.CharField(max_length=6, choices=GENDER)
    age = models.IntegerField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        """
        this class will define the ordering of the doctor

        """

        ordering = ["-created_at"]
        verbose_name_plural = "Doctors"
        verbose_name = "Doctor"

    def __str__(self):
        """
        this function will return the user_name of the doctor in the admin panel

        """

        return self.user_name

    def clean(self):
        """
        this function will check if the password and password_confirmation are the same
        and if the age is not empty
        and if the graduation_year is between 1970 and 2024

        """

        if self.password != self.password_confirmation:
            raise ValidationError("passwords do not match")

        if not self.age:
            raise ValidationError("Age is required")

        if self.graduation_year < 1970 or self.graduation_year > 2024:
            raise ValidationError("Invalid graduation year")

    def save(self, *args, **kwargs):
        """
        this function will save the password and password_confirmation in the database
        and will create the slug of the user_name

        """

        if not self.slug:
            self.slug = slugify(self.user_name)

        if not self.pk:
            self.password = make_password(self.password)
            self.password_confirmation = self.password

        super(Doctor, self).save(*args, **kwargs)


class Pharmacist(models.Model):
    """
    in this model we will create the pharmacist table in the database,
    and we will define the fields of the table.

    """

    user_name = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(validators=[MinLengthValidator(8)], max_length=100)
    password_confirmation = models.CharField(
        validators=[MinLengthValidator(8)], max_length=100
    )
    shift = models.CharField(max_length=10, choices=SHIFT)
    national_id_number = models.CharField(max_length=14, unique=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    age = models.IntegerField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        """
        this class will define the ordering of the pharmacist

        """

        ordering = ["-created_at"]
        verbose_name_plural = "Pharmacists"
        verbose_name = "Pharmacist"

    def __str__(self):
        """
        this function will return the user_name of the pharmacist in the admin panel

        """

        return self.user_name

    def clean(self):
        """
        this function will check if the password and password_confirmation are the same
        and if the age is not empty

        """

        if not self.age:
            raise ValidationError("Age is required")

        if self.password != self.password_confirmation:
            raise ValidationError("passwords do not match")

    def save(self, *args, **kwargs):
        """
        this function will save the password and password_confirmation in the database
        and will create the slug of the user_name

        """

        if not self.slug:
            self.slug = slugify(self.user_name)

        if not self.pk:
            self.password = make_password(self.password)
            self.password_confirmation = self.password

        super(Pharmacist, self).save(*args, **kwargs)


class Specialization(models.Model):
    """
    in this model we will create the specialization table in the database,
    and we will define the fields of the table.

    """

    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        """
        this class will define the ordering of the specialization

        """

        ordering = ["-created_at"]
        verbose_name_plural = "Specializations"
        verbose_name = "Specialization"

    def __str__(self):
        """
        this function will return the name of the specialization in the admin panel

        """

        return self.name

    def save(self, *args, **kwargs):
        """
        this function will create the slug of the specialization

        """

        if not self.slug:
            self.slug = slugify(self.name)

        super(Specialization, self).save(*args, **kwargs)


class PatientProfile(models.Model):
    """
    in this model we will create the patient_profile table in the database,
    and we will define the fields of the table.

    """

    Patient_name = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="patient_profile"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        """
        this class will define the ordering of the patient_profile

        """

        ordering = ["-created_at"]
        verbose_name_plural = "Patients Profiles"
        verbose_name = "Patient Profile"

    def __str__(self):
        """
        this function will return the name of the patient_profile in the admin panel

        """

        return f"{self.Patient_name} profile"

    def save(self, *args, **kwargs):
        """
        this function will create the slug of the patient_profile

        """

        if not self.slug:
            self.slug = slugify(self.Patient_name)

        super(PatientProfile, self).save(*args, **kwargs)


@receiver(post_save, sender=Patient)
def create_patient_profile(sender, instance, created, **kwargs):
    """
    this function will create the patient_profile when the patient is created

    """

    if created:
        PatientProfile.objects.create(Patient_name=instance)


class DoctorProfile(models.Model):
    """
    in this model we will create the doctor_profile table in the database,
    and we will define the fields of the table.

    """

    doctor_name = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="doctor_profile"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Doctors Profiles"
        verbose_name = "Doctor Profile"

    def __str__(self):
        return f"{self.doctor_name} profile"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.doctor_name)

        super(DoctorProfile, self).save(*args, **kwargs)


@receiver(post_save, sender=Doctor)
def create_doctor_profile(sender, instance, created, **kwargs):
    """
    this function will create the doctor_profile when the doctor.active is True

    """

    if instance.active:
        DoctorProfile.objects.create(doctor=instance)


class PharmacistProfile(models.Model):
    """
    in this model we will create the pharmacist_profile table in the database,
    and we will define the fields of the table.

    """

    pharmacist_name = models.ForeignKey(
        Pharmacist, on_delete=models.CASCADE, related_name="pharmacist_profile"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Pharmacists Profiles"
        verbose_name = "Pharmacist Profile"

    def __str__(self):
        return f"{self.pharmacist_name} profile"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.pharmacist_name)

        super(PharmacistProfile, self).save(*args, **kwargs)


@receiver(post_save, sender=Pharmacist)
def create_pharmacist_profile(sender, instance, created, **kwargs):
    """
    this function will create the pharmacist_profile when the pharmacist.active is True

    """

    if instance.active:
        PharmacistProfile.objects.create(pharmacist_name=instance)
