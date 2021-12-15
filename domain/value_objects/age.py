from domain.exceptions.invalid_age_exception import InvalidAgeException
from dataclasses import dataclass


@dataclass
class Age:
    value: int

    def __post_init__(self):
        self.validate()

    def validate(self):
        validation_number_age = 0
        if self.value <= validation_number_age:
            raise InvalidAgeException()
