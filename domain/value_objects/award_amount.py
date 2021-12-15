from domain.exceptions.invalid_award_amount import InvalidAwardAmountException
from dataclasses import dataclass


@dataclass
class AwardAmount:
    value: int

    def __post_init__(self):
        self.validate()

    def validate(self):
        validation_award_amount = 1
        if self.value <= validation_award_amount:
            raise InvalidAwardAmountException()
