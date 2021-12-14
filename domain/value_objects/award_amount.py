from domain.exceptions.invalid_award_amount import InvalidAwardAmountException


class AwardAmount:
    value: int

    def __init__(self, value:int):
        self.value = value
        self.validate()

    def validate(self):
        validation_award_amount = 1
        if self.value <= validation_award_amount:
            raise InvalidAwardAmountException()
