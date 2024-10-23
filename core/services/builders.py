from django.forms.models import model_to_dict

from Person.models import Person
from core.models import (
    InsuranceProvider,
    PolicyHolder,
    InsurancePolicy,
    InsurancePlan,
    InsuredPerson
)
from core import variables
from core.mapper import KeyMapper


class InsuranseDataBuilder:

    def __init__(self, json_data, mapper: KeyMapper):
        self.json_data = mapper.map_to_internal(json_data) 

    def get_person(self):
        print(self.json_data, 777777777777777777777777777777777)
        person_data = self.json_data[variables.INSURED_PERSON]
        person, created = Person.objects.get_or_create(**person_data)
        return person

    def get_insurance_provider(self):
        provider_data = self.json_data[variables.INSURANCE_PROVIDER]
        provider, created = InsuranceProvider.objects.get_or_create(**provider_data)
        return provider

    def get_insurance_plan(self, insurance_policy):
        plan_data = self.json_data[variables.INSURANCE_PLAN]
        plan_data[variables.INSURANCE_POLICY] = insurance_policy
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
            unique_identifier=policy_data[variables.UNIQUE_IDENTIFIER],
            defaults=policy_data
        )
        return policy
    
    def get_insured_person(self, person, insurance_policy, policy_holder, insurance_provider):
        insured_person_data = {
            variables.INSURANCE_POLICY: insurance_policy,
            variables.POLICY_HOLDER: policy_holder,
            variables.INSURANCE_PROVIDER: insurance_provider,
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
        plan = self._builder.get_insurance_plan(policy)
        insured_person = self._builder.get_insured_person(
            person=person,
            insurance_policy=policy,
            policy_holder=holder,
            insurance_provider=provider
        )

        return {
            variables.PERSON: model_to_dict(person),
            variables.INSURANCE_PROVIDER: model_to_dict(provider),
            variables.POLICY_HOLDER: model_to_dict(holder),
            variables.INSURANCE_POLICY: model_to_dict(policy),
            variables.INSURANCE_PLAN: model_to_dict(plan),
            variables.INSURED_PERSON: model_to_dict(insured_person)
        }