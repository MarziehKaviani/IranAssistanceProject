import datetime

from django.core.validators import MaxValueValidator


class YearValidator:
    """
    Validator for checking if a given year is valid.

    This validator checks if a given year is less than or equal to the current year.
    """
    @staticmethod
    def current_year():
        """
        Get the current year.

        Returns
        -------
        int
            The current year.
        """
        return datetime.date.today().year

    @staticmethod
    def max_year_validator(value):
        """
        Validate that the given year is less than or equal to the current year.

        Parameters
        ----------
        value : int
            The year value to validate.

        Returns
        -------
        None

        Raises
        ------
        ValidationError
            If the value is greater than the current year.
        """
        MaxValueValidator(YearValidator.current_year())(value)