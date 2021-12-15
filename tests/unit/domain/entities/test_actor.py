from unittest import TestCase

from domain.entities.actor import Actor
from domain.value_objects.person_genre import PersonGenre
from domain.value_objects.age import Age
from domain.value_objects.award_amount import AwardAmount
from domain.value_objects.name import Name


class TestActor(TestCase):
    def test_init_when_valid_args_then_build_actor(self):
        #Arrange
        age_value = 20
        age = Age(age_value)
        first_name = 'Gustavo'
        last_name = 'Paziani'
        name = Name(first_name, last_name)
        award_amount_value = 3
        award_amount = AwardAmount(award_amount_value)
        actor_genre_value = 'male'
        actor_genre = PersonGenre(actor_genre_value)

        #Action
        actor = Actor(name, age, award_amount, actor_genre)

        #Assert
        self.assertIsInstance(actor, Actor)