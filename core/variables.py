from django.utils.translation import gettext_lazy as _

# verbose names
PHONE_NUMBER_VERBOSE_NAME = _("Phone number")
CREATED_AT_VERBOSE_NAME = _("Created at")
UPDATED_AT_VERBOSE_NAME = _("Updated at")
IS_ACTIVE_VERBOSE_NAME = _("Is active")
IS_STAFF_VERBOSE_NAME = _("Is staff")
NAME_VERBOSE_NAME = _("Name")
LAST_VERBOSE_NAME = _("Last name")
IDENTITY_NUMBER_VERBOSE_NAME = _("Identity Number")
BIRTH_DATE_VERBOSE_NAME = _("Birth date")
FATHER_NAME_VERBOSE_NAME = _("Father name")
PLACE_OF_ISSUE_VERBOSE_NAME = _("Place of issue")
INSURANCE_PROVIDER_VERBOSE_NAME= _("Insurance provider")
UNIQUE_IDENTIFIER_VERBOSE_NAME = _("Unique identifier")
START_DATE_VERBOSE_NAME = _("Start date")
END_DATE_VERBOSE_NAME = _("End date")
CONFIRMATION_DATE_VERBOSE_NAME = _("Confirmation date")
INSURED_PERSONS_VERBOSE_NAME = _("Insured persons")
INSURANCE_POLICY_NUMBER_VERBOSE_NAME = _("Insurance policy number")
POLICY_HOLDER_VERBOSE_NAME = _("Policy holder")
INSURANCE_PROVIDER_VERBOSE_NAME = _("Insurance Provider")
PLAN_VERBOSE_NAME = _("Plan")
EMAIL_VERBOSE_ENAME = _("Email")
INSURANCE_POLICY_VERBOSE_NAME = _("Insurance Policy")
PERSON_VERBOSE_NAME = _("Person")

# keys
IS_STAFF = "is_staff"
IS_ACTIVE = "is_active"
IS_SUPERUSER = "is_superuser"
POST_METHOD = 'POST'
GET_METHOD = 'GET'
INSURED_PERSON = 'insured_person'
PERSON = "person"
INSURANCE_PROVIDER = 'insurance_provider'
POLICY_HOLDER = 'policy_holder'
POLICY_NUMBER = 'insurance_policy_number'
INSURANCE_PLAN = 'insurance_plan'
INSURANCE_POLICY = 'insurance_policy'
UNIQUE_IDENTIFIER = 'unique_identifier'
DETAILS = 'details'
ID = 'id'
NAME = 'name'
START_DATE = "start_date"
END_DATE = "end_date"
CONFIRMATION_DATE = "confirmation_date"
INSURANCE_POLICY_NUMBER = 'insurance_policy_number'
PHONE_NUMBER = "phone_number"
EMAIL = "email"
LAST_NAME = "last_name"
IDENTITY_NUMBER = "identity_number"
BIRTH_DATE = "birth_date"
FATHER_NAME = "father_name"
PLACE_OF_ISSUE = "place_of_issue"

# messages & errors 
PHONE_NUMBER_REQUIRED = _("The Phone number field must be set")
INVALID_PHONE_NUMBER = _("Invalid phone number")
INVALID_INPUT_DATA = _("Invalid input data")
INSURD_PERSON_ALREADY_EXISTS_IN_POLICY = _("This person is already insured under this policy.")
SOMETHING_WENT_WRONG = _("Something went wrong.")
INVALID_PHONE_NUMBER = _("Invalid phone number. the phone number should be in 09XX XXX XXXX pattern")
INVALID_BIRTH_DATE = _("Your birth date cannot be in the future.")
INVALID_IDENTITY_NUMBER = _("Invalid identity number")

# status code
class BusinessStatusCodes:
    """
    3000-3999 for validation errors
    4000-4999 for system errors
    """
    
    # General Success
    SUCCESS = 200
    
    # Validation errors
    INVALID_INPUT_DATA = 3001

    # System errors 
    UNEXPECTED_ERROR = 4000
    
