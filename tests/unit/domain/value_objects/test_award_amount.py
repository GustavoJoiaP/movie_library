from unittest import TestCase

from domain.exceptions.invalid_award_amount import InvalidAwardAmountException
from domain.value_objects.award_amount import AwardAmount


class TestAwardAmount(TestCase):
    def test_init_when_valid_args_then_build_award_amount(self):
        #Arrange
        award_amount_value = 2

        #Action
        award_amount = AwardAmount(award_amount_value)

        #Assert
        expected_value_award_amount = 2
        self.assertEqual(expected_value_award_amount, award_amount_value)

    def test_init_when_invalid_args_then_raise_invalid_award_amount_exception(self):
        # Arrange
        award_amount_value = 0

        # Assert
        with self.assertRaises(InvalidAwardAmountException):
            # Action
            award_amount = AwardAmount(award_amount_value)