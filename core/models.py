from django.db import models
from django.utils.translation import gettext_lazy as _

from core import variables
from Person.models import Person


class InsuranceProvider(models.Model): # bimegar
    name = models.CharField(
        max_length=255,
        verbose_name=variables.NAME_VERBOSE_NAME,

    )
    unique_identifier = models.CharField(
        max_length=100,
        verbose_name=variables.UNIQUE_IDENTIFIER_VERBOSE_NAME,

    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=variables.CREATED_AT_VERBOSE_NAME  
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=variables.UPDATED_AT_VERBOSE_NAME  
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Insurance Provider")
        verbose_name_plural = _("Insurance Providers")


class PolicyHolder(models.Model):  # bimegozar 
    name = models.CharField(
        max_length=255,
        verbose_name=variables.NAME_VERBOSE_NAME,
    )

    unique_identifier = models.CharField(
        max_length=100,
        verbose_name=variables.UNIQUE_IDENTIFIER_VERBOSE_NAME,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=variables.CREATED_AT_VERBOSE_NAME 
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=variables.UPDATED_AT_VERBOSE_NAME  
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Policy Holder")
        verbose_name_plural = _("Policy Holders")


class InsurancePolicy(models.Model):
    start_date = models.DateField(
        verbose_name=variables.START_DATE_VERBOSE_NAME, 
        blank=False
    )
    end_date = models.DateField(
        verbose_name=variables.END_DATE_VERBOSE_NAME, 
        null=False,
        blank=False
    )
    unique_identifier = models.CharField(
        max_length=100,
        verbose_name=variables.UNIQUE_IDENTIFIER_VERBOSE_NAME, 
        null=False,
        blank=False
    )
    confirmation_date = models.DateField(
        verbose_name=variables.CONFIRMATION_DATE_VERBOSE_NAME, 
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=variables.CREATED_AT_VERBOSE_NAME 
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=variables.UPDATED_AT_VERBOSE_NAME 
    )
    def __str__(self):
        return self.unique_identifier

    class Meta:
        verbose_name = _("Insurance Policy")
        verbose_name_plural = _("Insurance Policies")


class InsurancePlan(models.Model):
    insurance_policy_number = models.CharField(
        max_length=100,
        verbose_name=variables.INSURANCE_POLICY_NUMBER_VERBOSE_NAME, 
        null=False,
        blank=False
    )
    name = models.CharField(
        max_length=255,
        verbose_name=variables.NAME_VERBOSE_NAME,
    )
    unique_identifier = models.CharField(
        max_length=100,
        verbose_name=variables.UNIQUE_IDENTIFIER_VERBOSE_NAME, 
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=variables.CREATED_AT_VERBOSE_NAME 
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=variables.UPDATED_AT_VERBOSE_NAME 
    )
    insurance_policy = models.ForeignKey(
        InsurancePolicy,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=variables.INSURANCE_POLICY_VERBOSE_NAME
    )

    def __str__(self):
        return f"{self.name} - {self.insurance_policy_number}"

    class Meta:
        verbose_name = _("Insurance Plan")
        verbose_name_plural = _("Insurance Plans")


class InsuredPerson(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=variables.PERSON_VERBOSE_NAME
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=variables.CREATED_AT_VERBOSE_NAME 
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=variables.UPDATED_AT_VERBOSE_NAME 
    )
    insurance_policy = models.ForeignKey(
        InsurancePolicy,
        on_delete=models.SET_NULL,
        null = True,
    )
    policy_holder = models.ForeignKey(
        PolicyHolder,
        on_delete=models.SET_NULL,
        null=True, 
        verbose_name=variables.POLICY_HOLDER_VERBOSE_NAME
    )
    insurance_provider = models.ForeignKey(
        InsuranceProvider,
        on_delete=models.SET_NULL,
        null=True, 
        verbose_name=variables.INSURANCE_PROVIDER_VERBOSE_NAME
    )
