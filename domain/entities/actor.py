from domain.value_objects.age import Age
from domain.value_objects.award_amount import AwardAmount
from domain.value_objects.name import Name


class Actor:
    name: Name
    age: Age
    award_amount: AwardAmount

    def __init__(self, name: Name, age: Age, award_amount: AwardAmount):
        self.name = name
        self.age = age
        self.award_amount = award_amount
