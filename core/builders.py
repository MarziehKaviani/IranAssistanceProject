from Person.models import Person
from Insurance.models import (
    InsuranceProvider,
    PolicyHolder,
    InsurancePolicy,
    InsurancePlan
)
from core import variables


class DataBuilder:

    def __init__(self, json_data):
        self.json_data = json_data

    def get_person(self):
        person_data = self.json_data[variables.PERSON]
        person, created = Person.objects.get_or_create(**person_data)
        return person

    def get_insurance_provider(self):
        provider_data = self.json_data[variables.INSURANCE_PROVIDER]
        provider, created = InsuranceProvider.objects.get_or_create(**provider_data)
        return provider

    def get_insurance_plan(self):
        plan_data = self.json_data[variables.INSURANCE_PLAN]
        plan, created = InsurancePlan.objects.get_or_create(**plan_data)
        return plan

    def get_policy_holder(self):
        policyholder_data = self.json_data[variables.POLICY_HOLDER]
        policyholder, created = PolicyHolder.objects.get_or_create(
            unique_identifier=policyholder_data[variables.UNIQUE_IDENTIFIER],
            defaults=policyholder_data
        )
        return policyholder
    
    def get_insurance_policy(self):
        policy_data = self.json_data[variables.INSURANCE_POLICY]
        policy, created = InsurancePolicy.objects.get_or_create(
            policy_number=policy_data[variables.POLICY_NUMBER],
            defaults=policy_data
        )
        return policy

    def build(self) -> dict:
        person = self.get_person()
        provider = self.get_insurance_provider()
        holder = self.get_policy_holder()
        policy = self.get_insurance_policy()
        plan = self.get_insurance_plan()

        return {
            variables.PERSON: person,
            variables.INSURANCE_PROVIDER: provider,
            variables.POLICY_HOLDER: holder,
            variables.INSURANCE_POLICY: policy,
            variables.INSURANCE_PLAN: plan
        }
