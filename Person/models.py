from django.db import models
from django.utils.translation import gettext_lazy as _

from core import variables


class Person(models.Model):
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

    birth_date = models.DateField(verbose_name=variables.BIRTH_DATE_VERBOSE_NAME, null=True, blank=True)  

    father_name = models.CharField(max_length=255, verbose_name=variables.FATHER_NAME_VERBOSE_NAME, null=True, blank=True)

    place_of_issue = models.CharField(
        max_length=255, verbose_name=variables.PLACE_OF_ISSUE_VERBOSE_NAME, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}" 

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")
