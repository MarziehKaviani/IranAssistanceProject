class KeyMapper:
    def __init__(self, mapping=None):
        """
        Initialize the KeyMapper with a dictionary mapping.
        If no mapping is provided, it will pass the original keys.

        Parameters
        ----------
        mapping : dict or None
            A dictionary where keys are the JSON keys and values are the internal names.
            If None, the original keys will be used.
        """
        self.mapping = mapping if mapping is not None else {}

    def map_to_internal(self, json_data):
        """
        Map external JSON keys to internal field names.

        Parameters
        ----------
        json_data : dict
            The JSON data with external keys.

        Returns
        -------
        dict
            The JSON data with internal field names.
        """
        if not self.mapping:  # No mapping, return the original keys
            return json_data
        return {self.mapping.get(key, key): value for key, value in json_data.items()}

    def map_to_external(self, internal_data):
        """
        Map internal field names to external JSON keys.

        Parameters
        ----------
        internal_data : dict
            The data with internal field names.

        Returns
        -------
        dict
            The data with external JSON keys.
        """
        if not self.mapping:  # No mapping, return the original keys
            return internal_data
        reverse_mapping = {v: k for k, v in self.mapping.items()}
        return {reverse_mapping.get(key, key): value for key, value in internal_data.items()}
