from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, email, phone_number, password, user_type, **extra_fields):
        if not email or not phone_number:
            raise ValueError("Email or Phone Number Must be provided")

        user = self.model(
            email=email,
            phone_number=phone_number,
            user_type=user_type,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, phone_number, password, user_type, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, phone_number, password, user_type, **extra_fields)

    def create_superuser(self, email, phone_number, password, user_type, **extra_fields):
        user_type = "admin"
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, phone_number, password, user_type, **extra_fields)


USER_TYPES = [
    ("farmers", "Farmers"),
    ("ranchers", "Ranchers"),
    ("consumer", "Consumer"),

    # Superuser
    ("admin", "Admin")
]


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    # Verification fields
    user_type = models.CharField(
        max_length=10, choices=USER_TYPES, default="consumer")
    otp = models.CharField(max_length=12, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(auto_now=True)

    # Default fields
    USERNAME_FIELD = 'email' or 'phone_number'
    REQUIRED_FIELDS = [
        "phone_number",
        "user_type"
    ]
    objects = UserManager()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
