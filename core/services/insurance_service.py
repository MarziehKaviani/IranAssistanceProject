from .builders import InsuranseDataDirector, InsuranseDataBuilder
from core.mapper import KeyMapper


class InsuranseService:
    def __init__(self, json_data, key_mapping=None):
        self.json_data = json_data
        self.key_mapping = key_mapping

    def process_insurance_data(self):
        mapper = KeyMapper(self.key_mapping)
        builder = InsuranseDataBuilder(self.json_data, mapper)
        director = InsuranseDataDirector(builder)
        insurance_data = director.construct_insurance_data()
        return insurance_data