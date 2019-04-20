import unittest
from datetime import datetime, timedelta
from decimal import Decimal

from pyflunt.notifications import Notifiable
from pyflunt.validations import (BoolValidationContractMixin,
                                 DateTimeValidationContractMixin,
                                 NumberValidationContractMixin, RequiresMixin)


class BoolValidationContractMixinTests(unittest.TestCase):
    def setUp(self):
        class Contract(BoolValidationContractMixin, RequiresMixin, Notifiable):
            pass

        self._contract = Contract()

    def test_should_is_valid_false_when_is_false_called_with_value_true(self):
        contract = self._contract.requires().is_false(value=True,
                                                      field='active',
                                                      message='active invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_false_called_with_value_false(self):
        contract = self._contract.requires().is_false(value=False,
                                                      field='active',
                                                      message='active invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_is_true_called_with_value_false(self):
        contract = self._contract.requires().is_true(value=False,
                                                     field='active',
                                                     message='active invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_true_called_with_value_true(self):
        contract = self._contract.requires().is_true(value=True,
                                                     field='active',
                                                     message='active invalid')

        self.assertTrue(contract.is_valid)


class DateTimeValidationContractMixinTests(unittest.TestCase):
    def setUp(self):
        class Contract(DateTimeValidationContractMixin, RequiresMixin,
                       Notifiable):
            pass

        self._contract = Contract()

    def test_should_is_valid_false_when_is_greater_than_is_called_with_value_lower_than_comparer(
            self):
        value = datetime.now() - timedelta(days=2)
        comparer = datetime.now() - timedelta(days=1)

        contract = self._contract.requires().is_greater_than(
            value=value,
            comparer=comparer,
            field='begin date',
            message='begin date invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_greater_than_is_called_with_value_greater_than_comparer(
            self):
        value = datetime.now()
        comparer = datetime.now() - timedelta(days=1)

        contract = self._contract.requires().is_greater_than(
            value=value,
            comparer=comparer,
            field='begin date',
            message='begin date invalid')

        self.assertTrue(contract.is_valid)


class NumberContractValidationTests(unittest.TestCase):
    def setUp(self):
        class Contract(NumberValidationContractMixin, RequiresMixin,
                       Notifiable):
            pass

        self._contract = Contract()

    def test_should_is_valid_false_when_is_greater_than_is_called_with_value_lower_than_comparer(
            self):
        value = 100
        comparer = 200

        contract = self._contract.requires().is_greater_than(
            value=value,
            comparer=comparer,
            field='initial value',
            message='initial value invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_greater_than_is_called_with_value_greater_than_comparer(
            self):
        value = Decimal(200.99)
        comparer = Decimal(100.99)

        contract = self._contract.requires().is_greater_than(
            value=value,
            comparer=comparer,
            field='begin date',
            message='begin date invalid')

        self.assertTrue(contract.is_valid)
