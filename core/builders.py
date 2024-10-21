from .factories import (
    InsurancePlanFactory, 
    PolicyholderFactory, 
    InsurancePolicyFactory, 
    InsuranceProviderFactory,
    PersonFactory
)


class DataBuilder:
    def __init__(self, json_data):
        self.json_data = json_data

    def build(self):
        person = PersonFactory.create(self.json_data['person'])
        provider = InsuranceProviderFactory.create(self.json_data['insurance_provider'])
        policyholder = PolicyholderFactory.create(self.json_data['policyholder'])
        policy = InsurancePolicyFactory.create(self.json_data['insurance_policy'])
        plan = InsurancePlanFactory.create(self.json_data['insurance_plan'])

        return {
            "person": person,
            "provider": provider,
            "policyholder": policyholder,
            "policy": policy,
            "plan": plan
        }