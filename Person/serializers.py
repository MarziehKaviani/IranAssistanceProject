from rest_framework import serializers

from Person.models import Person
from core import variables
from core.validators import BirthDateValidator
from .validators import PhoneNumberValidator, identity_number_validator


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            variables.PHONE_NUMBER,
            variables.EMAIL,
            variables.NAME,
            variables.LAST_NAME,
            variables.IDENTITY_NUMBER,
            variables.BIRTH_DATE,
            variables.FATHER_NAME,
            variables.PLACE_OF_ISSUE,
        ]
    def validate(self, attrs):
        if not PhoneNumberValidator(phone_number=attrs[variables.PHONE_NUMBER]).validate():
            raise serializers.ValidationError({variables.PHONE_NUMBER: variables.INVALID_PHONE_NUMBER})
        if not BirthDateValidator().validate(attrs[variables.BIRTH_DATE]):
            raise serializers.ValidationError({variables.BIRTH_DATE: variables.INVALID_BIRTH_DATE})
        if not identity_number_validator(attrs[variables.IDENTITY_NUMBER]):
            raise serializers.ValidationError({variables.IDENTITY_NUMBER: variables.INVALID_IDENTITY_NUMBER})
        return super().validate(attrs)

