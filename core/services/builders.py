from Person.models import Person
from Insurance.models import (
    InsuranceProvider,
    PolicyHolder,
    InsurancePolicy,
    InsurancePlan,
    InsuredPerson
)
from core import variables


class InsuranseDataBuilder:

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
    
    def get_insured_person(self, person, insurance_policy, policy_holder, insurance_provider):
        insured_person_data = {
            "insurance_policy": insurance_policy,
            "policy_holder": policy_holder,
            "insurance_provider": insurance_provider,
        }
        insured_person, created = InsuredPerson.objects.get_or_create(**insured_person_data)
        return insured_person



class InsuranseDataDirector:
    def __init__(self, builder: InsuranseDataBuilder):
        self._builder = builder

    def construct_insurance_data(self):
        person = self._builder.get_person()
        provider = self._builder.get_insurance_provider()
        holder = self._builder.get_policy_holder()
        policy = self._builder.get_insurance_policy()
        plan = self._builder.get_insurance_plan()
        insured_person = self._builder.get_insured_person(
            person=person,
            insurance_policy=policy,
            policy_holder=holder,
            insurance_provider=provider
        )

        return {
            variables.PERSON: person,
            variables.INSURANCE_PROVIDER: provider,
            variables.POLICY_HOLDER: holder,
            variables.INSURANCE_POLICY: policy,
            variables.INSURANCE_PLAN: plan,
            variables.INSURED_PERSON: insured_person
        }