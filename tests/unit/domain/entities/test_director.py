from unittest import TestCase

from domain.entities.director import Director
from domain.value_objects.age import Age
from domain.value_objects.award_amount import AwardAmount
from domain.value_objects.name import Name
from domain.value_objects.person_genre import PersonGenre


class TestDirector(TestCase):
    def test_init_when_valid_arg_then_build_director(self):
        #Arrange
        age_value = 50
        age = Age(age_value)
        first_name = 'Euclerio'
        last_name = 'Ornellas'
        name = Name(first_name, last_name)
        award_amount_value = 2
        award_amount = AwardAmount(award_amount_value)
        director_genre_value = 'female'
        director_genre = PersonGenre(director_genre_value)

        #Action
        director = Director(name, age, award_amount, director_genre)

        #Assert
        self.assertIsInstance(director, Director)


