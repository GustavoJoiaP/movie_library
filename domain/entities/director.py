from domain.value_objects.age import Age
from domain.value_objects.award_amount import AwardAmount
from domain.value_objects.name import Name
from domain.value_objects.person_genre import PersonGenre


class Director:
    name: Name
    age: Age
    award_amount: AwardAmount
    director_genre: PersonGenre

    def __init__(self, name: Name, age: Age, award_amount: AwardAmount, director_genre: PersonGenre):
        self.name = name
        self.age = age
        self.award_amount = award_amount
        self.director_genre = director_genre