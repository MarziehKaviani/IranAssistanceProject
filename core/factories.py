from Insurance.models import (
    InsurancePlan,
    InsurancePolicy, 
    Policyholder, 
    InsuranceProvider
)

from Person.models import Person


class PersonFactory:
    @staticmethod
    def create(data):
        return Person.objects.create(**data)


class InsuranceProviderFactory:
    @staticmethod
    def create(data):
        return InsuranceProvider.objects.create(**data)


class PolicyholderFactory:
    @staticmethod
    def create(data):
        return Policyholder.objects.create(**data)


class InsurancePolicyFactory:
    @staticmethod
    def create(data):
        return InsurancePolicy.objects.create(**data)


class InsurancePlanFactory:
    @staticmethod
    def create(data):
        return InsurancePlan.objects.create(**data)