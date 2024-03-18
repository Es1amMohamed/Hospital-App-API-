from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator


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

        if not self.pk or "password" in self._modified_fields:
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

        if not self.pk or "password" in self.dirty_fields:
            self.password = make_password(self.password)
            self.password_confirmation = make_password(self.password_confirmation)

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

        if not self.pk or "password" in self.dirty_fields:
            self.password = make_password(self.password)
            self.password_confirmation = make_password(self.password_confirmation)

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
