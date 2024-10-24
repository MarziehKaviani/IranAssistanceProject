from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import (
    InsuranceProvider, 
    PolicyHolder, 
    InsurancePolicy, 
    InsurancePlan
    )
from Person.serializers import PersonSerializer
from core import variables


class InsuranceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceProvider
        fields = [
            variables.UNIQUE_IDENTIFIER,
            variables.NAME,
        ]


class PolicyholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyHolder
        fields = [
            variables.UNIQUE_IDENTIFIER,
            variables.NAME,
        ]


class InsurancePolicySerializer(serializers.ModelSerializer):
    """
    Serializer for InsurancePolicy model.
    Validates that the end date is after the start date.
    """
    class Meta:
        model = InsurancePolicy
        fields = [
            variables.UNIQUE_IDENTIFIER,
            variables.START_DATE,
            variables.END_DATE,
            variables.CONFIRMATION_DATE
        ]
    def validate(self, attrs):
        if attrs[variables.END_DATE] < attrs[variables.START_DATE]:
            raise serializers.ValidationError({variables.END_DATE: _("The end date must be after start date.")})
        return super().validate(attrs)


class InsurancePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePlan
        fields = [
            variables.UNIQUE_IDENTIFIER,
            variables.NAME,
            variables.INSURANCE_POLICY_NUMBER,
        ]


class CompleteDataSerializer(serializers.Serializer):
    """
    Serializer for handling and validating nested data for multiple models:
    - insured_person: PersonSerializer
    - insurance_provider: InsuranceProviderSerializer
    - policy_holder: PolicyholderSerializer
    - insurance_policy: InsurancePolicySerializer
    - insurance_plan: InsurancePlanSerializer
    
    Combines data for multiple related models in one structure for efficient input handling.
    """
    insured_person = PersonSerializer()
    insurance_provider = InsuranceProviderSerializer()
    policy_holder = PolicyholderSerializer()
    insurance_policy = InsurancePolicySerializer()
    insurance_plan = InsurancePlanSerializer()    
