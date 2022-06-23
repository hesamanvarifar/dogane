
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be provide')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,  password):
        if not email:
            raise ValueError('Email must be provide')

        superuser = self.model(
            email=self.normalize_email(email)
        )

        superuser.set_password(password)
        superuser.role = 'admin'
        superuser.is_superuser = True
        superuser.is_staff = True

        superuser.save()
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    CHOICES = (
        ('reception', 'Reception'),
        ('admin', 'Admin'),
        ('technician', 'Technician'),
        ('inspector', 'Inspector'),
    )
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(
        max_length=255, choices=CHOICES, default='reception')
    objects = UserManager()
    USERNAME_FIELD = "email"


class Car(models.Model):
    name = models.CharField(max_length=255)
    is_repaired = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    part = models.ManyToManyField('Carpart')

    def __str__(self):
        return self.name


class CarPart(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
