from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator


GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
]

SHIFT = [
    ("Morning", "Morning"),
    ("Evening", "Evening"),
]


class Patient(models.Model):
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
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def clean(self):
        if self.password != self.password_confirmation:
            raise ValidationError("passwords do not match")

        if not self.age:
            raise ValidationError("Age is required")

    def save(self, *args, **kwargs):

        if not self.pk or "password" in self.dirty_fields:
            self.password = make_password(self.password)

        if not self.slug:
            self.slug = slugify(self.name)

        super(Patient, self).save(*args, **kwargs)


class Doctor(models.Model):
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
    graduation_year = models.DateTimeField()
    gender = models.CharField(max_length=6, choices=GENDER)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def clean(self):
        if self.password != self.password_confirmation:
            raise ValidationError("passwords do not match")

        if not self.age:
            raise ValidationError("Age is required")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        if not self.pk or "password" in self.dirty_fields:
            self.password = make_password(self.password)

        super(Doctor, self).save(*args, **kwargs)


class Pharmacist(models.Model):
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
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def clean(self):
        if self.password != self.password_confirmation:
            raise ValidationError("passwords do not match")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        if not self.pk or "password" in self.dirty_fields:
            self.password = make_password(self.password)

        super(Pharmacist, self).save(*args, **kwargs)


class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Specialization, self).save(*args, **kwargs)
