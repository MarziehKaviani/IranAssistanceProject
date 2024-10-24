from rest_framework import serializers
from Person.models import Person
from core import variables
from core.validators import BirthDateValidator
from .validators import PhoneNumberValidator, identity_number_validator


class PersonSerializer(serializers.Serializer):
    """
    Serializer for the Person model.
    
    Validates:
    - Phone number format
    - Birth date (not in the future)
    - Identity number format
    """
    phone_number = serializers.CharField(max_length=11)
    email = serializers.EmailField()
    name = serializers.CharField(max_length=32)
    last_name = serializers.CharField(max_length=32)
    identity_number = serializers.CharField(max_length=11)
    birth_date = serializers.DateField(allow_null=True, required=False)
    father_name = serializers.CharField(max_length=255, allow_null=True, required=False)
    place_of_issue = serializers.CharField(max_length=255, allow_null=True, required=False)

    def validate(self, attrs):
        if not PhoneNumberValidator(phone_number=attrs[variables.PHONE_NUMBER]).validate():
            raise serializers.ValidationError({variables.PHONE_NUMBER: variables.INVALID_PHONE_NUMBER})
        if not BirthDateValidator().validate(attrs[variables.BIRTH_DATE]):
            raise serializers.ValidationError({variables.BIRTH_DATE: variables.INVALID_BIRTH_DATE})
        if not identity_number_validator(attrs[variables.IDENTITY_NUMBER]):
            raise serializers.ValidationError({variables.IDENTITY_NUMBER: variables.INVALID_IDENTITY_NUMBER})
        return super().validate(attrs)

