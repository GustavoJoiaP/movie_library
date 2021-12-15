from domain.exceptions.invalide_name_exception import InvalidNameException
from dataclasses import dataclass


@dataclass
class Name:
    first: str
    last: str

    def __post_init__(self):
        self.validate()

    def validate(self):
        validation_number_character = 3
        if len(self.first) <= validation_number_character or len(self.last) <= validation_number_character:
            raise InvalidNameException()