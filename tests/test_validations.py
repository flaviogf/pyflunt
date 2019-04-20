import unittest
from datetime import datetime, timedelta

from pyflunt.validations import Contract


class BoolValidationContractMixinTests(unittest.TestCase):
    def test_should_is_valid_false_when_is_false_called_with_value_true(self):
        contract = Contract().requires().is_false(value=True,
                                                  field='active',
                                                  message='active invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_false_called_with_value_false(self):
        contract = Contract().requires().is_false(value=False,
                                                  field='active',
                                                  message='active invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_is_true_called_with_value_false(self):
        contract = Contract().requires().is_true(value=False,
                                                 field='active',
                                                 message='active invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_true_called_with_value_true(self):
        contract = Contract().requires().is_true(value=True,
                                                 field='active',
                                                 message='active invalid')

        self.assertTrue(contract.is_valid)


class DateTimeContractValidationTests(unittest.TestCase):
    def test_should_is_valid_false_when_is_greater_than_is_called_with_value_lower_than_comparer(
            self):
        value = datetime.now() - timedelta(days=2)
        comparer = datetime.now() - timedelta(days=1)

        contract = Contract().requires().is_greater_than(
            value=value,
            comparer=comparer,
            field='begin date',
            message='begin date invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_ture_when_is_greater_than_is_called_with_value_greater_than_comparer(
            self):
        value = datetime.now()
        comparer = datetime.now() - timedelta(days=1)

        contract = Contract().requires().is_greater_than(
            value=value,
            comparer=comparer,
            field='begin date',
            message='begin date invalid')

        self.assertTrue(contract.is_valid)
