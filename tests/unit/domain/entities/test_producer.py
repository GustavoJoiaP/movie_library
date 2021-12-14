from unittest import TestCase

from domain.entities.producer import Producer
from domain.value_objects.age import Age
from domain.value_objects.award_amount import AwardAmount
from domain.value_objects.name import Name


class TestProducer(TestCase):
    def test_init_when_valid_args_then_build_producer(self):
        #Arrage
        age_value = 30
        age = Age(age_value)
        first_name = 'Universal'
        last_name = 'Studios'
        name = Name(first_name, last_name)
        award_amount_value = 57
        award_amount = AwardAmount(award_amount_value)

        #Action
        producer = Producer(name, age, award_amount)

        #Assert
        self.assertIsInstance(producer, Producer)
