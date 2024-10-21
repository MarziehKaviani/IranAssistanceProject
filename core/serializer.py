from rest_framework import serializers

from Person.models import Person
from Insurance.models import (
    InsuranceProvider, 
    Policyholder, 
    InsurancePolicy, 
    InsurancePlan
    )


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class InsuranceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceProvider
        fields = '__all__'


class PolicyholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policyholder
        fields = '__all__'


class InsurancePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePolicy
        fields = '__all__'


class InsurancePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePlan
        fields = '__all__'


class CompleteDataSerializer(serializers.Serializer):
    person = PersonSerializer()
    insurance_provider = InsuranceProviderSerializer()
    policyholder = PolicyholderSerializer()
    insurance_policy = InsurancePolicySerializer()
    insurance_plan = InsurancePlanSerializer()
