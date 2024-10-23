from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from core.models import Person, InsuranceProvider, PolicyHolder, InsurancePolicy, InsurancePlan, InsuredPerson

class CreateInsuredPersonViewTest(APITestCase):
    def setUp(self):
        self.valid_json_data = {
            "insured_person": {
                "phone_number": "09120000000",
                "email": "example@example.com",
                "name": "fd",
                "last_name": "dd",
                "identity_number": "1234567896",
                "birth_date": "2000-01-01",
                "father_name": "Father Name",
                "place_of_issue": "Place"
            },
            "insurance_provider": {
                "unique_identifier": "provider123",
                "name": "Provider Name"
            },
            "policy_holder": {
                "unique_identifier": "holder123",
                "name": "Holder Name"
            },
            "insurance_policy": {
                "unique_identifier": "policy123",
                "start_date": "2024-01-01",
                "end_date": "2025-01-01",
                "confirmation_date": "2024-01-02"
            },
            "insurance_plan": {
                "unique_identifier": "plan123",
                "name": "Plan Name",
                "insurance_policy_number": "policy123"
            }
        }
        self.invalid_json_data = {
            # Missing required fields
            "hfksjfesjfl": {
                "phone_number": "invalid phone",
                "email": "not-an-email",
                "name": "John"
            }
        }
        self.url ='http://127.0.0.1:8000/api/insurance-policy/'  

    def test_create_insured_person_with_valid_data(self):
        """
        Test that the API creates an insured person with valid data.
        """
        response = self.client.post(self.url, data=self.valid_json_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Insurance policy unique identifier', response.data['data'])

        # Ensure all related objects are created
        self.assertTrue(Person.objects.filter(phone_number='09120000000').exists())
        self.assertTrue(InsuranceProvider.objects.filter(unique_identifier='provider123').exists())
        self.assertTrue(PolicyHolder.objects.filter(unique_identifier='holder123').exists())
        self.assertTrue(InsurancePolicy.objects.filter(unique_identifier='policy123').exists())
        self.assertTrue(InsurancePlan.objects.filter(unique_identifier='plan123').exists())
        self.assertTrue(InsuredPerson.objects.exists())

    def test_create_insured_person_with_invalid_data(self):
        """
        Test that the API returns a 400 response when data is invalid.
        """
        response = self.client.post(self.url, data=self.invalid_json_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('details', response.data['data'])

    def test_create_insured_person_with_missing_key_mapping(self):
        """
        Test behavior when no key mapping is provided.
        """
        response = self.client.post(self.url, data=self.valid_json_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


