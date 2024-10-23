from .builders import InsuranseDataDirector, InsuranseDataBuilder

class InsuranseService:
    def __init__(self, json_data):
        self.json_data = json_data

    def process_insurance_data(self):
        builder = InsuranseDataBuilder(self.json_data)
        director = InsuranseDataDirector(builder)
        insurance_data = director.construct_insurance_data()
        return insurance_data