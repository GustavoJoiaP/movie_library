from unittest import TestCase

from domain.exceptions.invalid_age_exception import InvalidAgeException
from domain.value_objects.age import Age

class TestAge(TestCase):
    def test_init_when_valid_args_then_build_age(self):
        #Arrange
        age_value = 23

        #Action
        age = Age(age_value)

        #Assert
        expected_age_value = 23
        self.assertEqual(expected_age_value, age_value)

    def test_init_when_invalid_args_then_raise_invalid_age_exception(self):
        #Arrange
        age_value = -1

        #Assert
        with self.assertRaises(InvalidAgeException):
            # Action
            age = Age(age_value)