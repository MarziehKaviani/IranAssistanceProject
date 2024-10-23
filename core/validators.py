import datetime
from django.core.exceptions import ValidationError


class BirthDateValidator:
    """
    Validator for checking if a given date is valid.

    This validator checks if the provided date is less than or equal to the current date.
    """

    @staticmethod
    def current_date():
        """
        Get the current date.

        Returns
        -------
        datetime.date
            The current date.
        """
        return datetime.date.today()

    @staticmethod
    def validate(date):
        """
        Validate that the given date is less than or equal to the current date.

        Parameters
        ----------
        value : datetime.date
            The date to validate.

        Returns
        -------
        bool

        Raises
        ------
        ValidationError
            If the date is in the future.
        """
        if not isinstance(date, datetime.date):
            raise ValidationError("Invalid date format. Please provide a valid date.")
        current = BirthDateValidator.current_date()
        if date > current:
            return False
        else:
            return True
