from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
  def create_user(self, email, username, role, password=None, **extra_fields):
    if not email:
      raise ValueError("The Email field must be set")
    
    if role == 1: 
      extra_fields.setdefault("is_staff", True)

    email = self.normalize_email(email.lower())
    user = self.model(email=email, username=username, role=role, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, username, password=None, **extra_fields):
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault("is_superuser", True)

    if extra_fields.get("is_staff") is not True:
        raise ValueError("Superuser must have is_staff=True.")
    if extra_fields.get("is_superuser") is not True:
        raise ValueError("Superuser must have is_superuser=True.")

    return self.create_user(email, username, 2, password, **extra_fields)
  
class CustomUser(AbstractUser):
  username = None
  email = models.EmailField(unique=True)
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []
  USER_ROLE_CHOICES = [(0, "Student"), (1, "Teacher"), (2, "Superuser")]
  role = models.PositiveSmallIntegerField(choices=USER_ROLE_CHOICES)

  objects = CustomUserManager()

  def __str__(self):
      return f"{self.last_name}, {self.first_name}; {self.user_type}"