import re


class PhoneNumberValidator:
    """
    Validator for phone numbers.

    Args:
        phone_number (str): The phone number to validate.
        country_code (str): The country code, default is '98'.
        valid_digits (list): List of valid starting digits for the phone number.
        format (str): Expected phone number format, default is '9xx xxx xxxx'.
    """
    valid_digits = [
        920, 921, 922, 910, 911, 912, 913, 914,
        915, 916, 917, 918, 919, 990, 991, 992,
        993, 994, 931, 932, 933, 934, 901, 902,
        903, 904, 905, 930, 933, 935, 936, 937,
        938, 939,
    ]

    def __init__(self, phone_number: str, country_code: str = "98", format: str = "9xx xxx xxxx") -> None:
        self.phone_number = phone_number.strip()
        self.country_code = country_code
        self.format = format

    def validate(self):
        """
        Validate the phone number format.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not str(self.phone_number).strip().isdigit():
            return False
        if int(self.phone_number.strip()[1:4]) not in self.valid_digits or len(self.phone_number.strip()) != 11:
            return False
        pattern = r"^0(?:9[0-9][0-9]|9[0-5]|9[013-9]|99|93)[0-9]{7}$"
        if not re.match(pattern, self.phone_number):
            return False
        return True



def identity_number_validator(identity_number):
    """
    Validate the national code.

    Parameters
    ----------
    identity_number : str
        The national code to validate.

    Returns
    -------
    bool
        True if the national code is valid, False otherwise.
    """
    # Ensure the national code is a string
    if not isinstance(identity_number, str):
        return False

    # Check if the string contains only digits and has the correct length (e.g., 10 digits)
    if not identity_number.isdigit() or len(identity_number) != 10:
        return False

    return True