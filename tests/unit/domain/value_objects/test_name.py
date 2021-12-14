from unittest import TestCase

from domain.exceptions.invalide_name_exception import InvalidNameException
from domain.value_objects.name import Name

class TestName(TestCase):
    def test_init_when_valid_args_return_then_build_name(self):
        #Arrange
        first_name = "Gustavo"
        last_name = "Paziani"

        #Action
        name = Name(first_name, last_name)

        #Assert
        expect_first_name = "Gustavo"
        expect_last_name = "Paziani"
        self.assertEqual(expect_first_name, first_name)
        self.assertEqual(expect_last_name, last_name)

    def test_init_when_invalid_args_then_raise_invalid_name_exception(self):
        #Arrange
        first_name = "Gu"
        last_name = "Jo"

        #Assert
        with self.assertRaises(InvalidNameException):
            # Action
            name = Name(first_name, last_name)