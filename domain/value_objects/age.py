from domain.exceptions.invalid_age_exception import InvalidAgeException


class Age:
    value: int

    def __init__(self, value):
        self.value = value
        self.validate()

    def validate(self):
        validation_number_age = 0
        if self.value <= validation_number_age:
            raise InvalidAgeException()