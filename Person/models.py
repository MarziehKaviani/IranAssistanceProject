from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import (AbstractBaseUser, Group, Permission,
                                        PermissionsMixin)

from core import variables
from validators import PhoneNumberValidator


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        """
        Create and return a user with an phone number and password.
        """
        if not phone_number:
            raise ValueError(variables.PHONE_NUMBER_REQUIRED)
        if not PhoneNumberValidator(phone_number).validate():
            raise ValueError(variables.INVALID_PHONE_NUMBER)
        
        phone_number = phone_number
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """
        Create and return a superuser with an phone number and password.
        """
        extra_fields.setdefault(variables.IS_STAFF, True)
        extra_fields.setdefault(variables.IS_ACTIVE, True)
        extra_fields.setdefault(variables.IS_SUPERUSER, True)

        return self.create_user(phone_number, password, **extra_fields)


class Person(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        verbose_name=variables.PHONE_NUMBER_VERBOSE_NAME,
    )
    email = models.EmailField(verbose_name=variables.EMAIL_VERBOSE_ENAME)
    
    name = models.CharField(
        max_length=32, verbose_name=variables.NAME_VERBOSE_NAME
    )

    last_name = models.CharField(
        max_length=32, verbose_name=variables.LAST_VERBOSE_NAME
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=variables.CREATED_AT_VERBOSE_NAME  
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=variables.UPDATED_AT_VERBOSE_NAME  
    )

    identity_number = models.CharField(max_length=11, verbose_name=variables.IDENTITY_NUMBER_VERBOSE_NAME,)

    birth_date = models.DateField(verbose_name=variables.BIRTH_DATE_VERBOSE_NAME, null=True, blank=True)  # TODO Set validator for this too

    father_name = models.CharField(max_length=255, verbose_name=variables.FATHER_NAME_VERBOSE_NAME, null=True, blank=True)

    place_of_issue = models.CharField(
        max_length=255, verbose_name=variables.PLACE_OF_ISSUE_VERBOSE_NAME, null=True, blank=True
    )
    is_active = models.BooleanField(default=True, verbose_name=variables.IS_ACTIVE_VERBOSE_NAME)
    is_staff = models.BooleanField(default=False, verbose_name=variables.IS_STAFF)
    
    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = [
        'name', 'last_name', 'identity_number', 'birth_date'
    ]

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}" 

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")
