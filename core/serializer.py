from rest_framework import serializers

from .models import (
    InsuranceProvider, 
    PolicyHolder, 
    InsurancePolicy, 
    InsurancePlan
    )
from Person.serializers import PersonSerializer
from core import variables, validators


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
            raise serializers.ValidationError({variables.END_DATE: "The end date must be after start date."})
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
    insured_person = PersonSerializer()
    insurance_provider = InsuranceProviderSerializer()
    policy_holder = PolicyholderSerializer()
    insurance_policy = InsurancePolicySerializer()
    insurance_plan = InsurancePlanSerializer()    
