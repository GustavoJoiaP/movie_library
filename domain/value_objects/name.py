from domain.exceptions.invalide_name_exception import InvalidNameException


class Name:
    first: str
    last: str

    def __init__(self, first:str, last:str):
        self.first = first
        self.last = last
        self.validate()

    def validate(self):
        validation_number_character = 3
        if len(self.first) <= validation_number_character or len(self.last) <= validation_number_character:
            raise InvalidNameException()