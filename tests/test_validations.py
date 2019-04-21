import unittest
import uuid
from datetime import datetime

from pyflunt.validations import Contract


class IsFalseMixinTests(unittest.TestCase):
    def test_should_is_valid_false_when_is_false_is_called_with_value_true(self):
        contract = Contract().requires().is_false(value=True,
                                                  field='active',
                                                  message='active invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_false_is_called_with_value_false(self):
        contract = Contract().requires().is_false(value=False,
                                                  field='active',
                                                  message='active invalid')

        self.assertTrue(contract.is_valid)


class IsTrueMixinTests(unittest.TestCase):
    def test_should_is_valid_false_when_is_true_is_called_with_value_false(self):
        contract = Contract().requires().is_true(value=False,
                                                 field='active',
                                                 message='active invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_true_is_called_with_value_true(self):
        contract = Contract().requires().is_true(value=True,
                                                 field='active',
                                                 message='active invalid')

        self.assertTrue(contract.is_valid)


class IsGreaterThanMixinTests(unittest.TestCase):
    def test_should_is_valid_false_when_is_greater_than_is_called_with_value_lower_than_comparer(self):
        contract = Contract().requires().is_greater_than(value=10,
                                                         comparer=100,
                                                         field='initial value',
                                                         message='initial value invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_false_when_is_greater_than_is_called_with_value_equal_than_comparer(self):
        contract = Contract().requires().is_greater_than(value=100.99,
                                                         comparer=100.99,
                                                         field='initial value',
                                                         message='initial value invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_greater_than_is_called_with_value_greater_than_comparer(self):
        contract = Contract().requires().is_greater_than(value=100.99,
                                                         comparer=100.89,
                                                         field='initial value',
                                                         message='initial value invalid')

        self.assertTrue(contract.is_valid)


class IsGreaterOrEqualsThanMixinTests(unittest.TestCase):
    def test_should_is_valid_false_when_is_greater_or_equals_than_is_called_with_value_lower_than_comparer(self):
        contract = Contract().requires().is_greater_or_equals_than(value=10,
                                                                   comparer=100.99,
                                                                   field='initial value',
                                                                   message='initial value invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_greater_or_equals_than_is_called_with_value_equal_than_comparer(self):
        contract = Contract().requires().is_greater_or_equals_than(value=100.99,
                                                                   comparer=100.99,
                                                                   field='initial value',
                                                                   message='initial value invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_true_when_is_greater_or_equals_than_is_called_with_value_greater_than_comparer(self):
        contract = Contract().requires().is_greater_or_equals_than(value=100.99,
                                                                   comparer=100.99,
                                                                   field='initial value',
                                                                   message='initial value invalid')

        self.assertTrue(contract.is_valid)


class IsLowerThanMixinTests(unittest.TestCase):
    def test_should_is_valid_false_when_is_lower_than_is_called_with_value_greater_than_comparer(self):
        contract = Contract().requires().is_lower_than(value=100.99,
                                                       comparer=100.98,
                                                       field='initial value',
                                                       message='initial value invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_false_when_is_lower_than_is_called_with_value_equal_to_comparer(self):
        contract = Contract().requires().is_lower_than(value=100,
                                                       comparer=100,
                                                       field='initial value',
                                                       message='initial value invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_lower_than_is_called_with_value_lower_than_comparer(self):
        contract = Contract().requires().is_lower_than(value=10,
                                                       comparer=100,
                                                       field='initial value',
                                                       message='initial value invalid')

        self.assertTrue(contract.is_valid)


class IsLowerThanOrEqualsMixinTests(unittest.TestCase):
    def test_should_is_valid_false_when_is_lower_or_equals_than_is_called_with_value_greater_than_comparer(self):
        contract = Contract().requires().is_lower_or_equals_than(value=100,
                                                                 comparer=10,
                                                                 field='initial value',
                                                                 message='initial value invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_lower_or_equals_than_is_called_with_value_equal_to_comparer(self):
        contract = Contract().requires().is_lower_or_equals_than(value=10,
                                                                 comparer=10,
                                                                 field='initial value',
                                                                 message='initial value invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_true_when_is_lower_or_equals_than_is_called_with_value_lower_than_comparer(self):
        contract = Contract().requires().is_lower_or_equals_than(value=9,
                                                                 comparer=10,
                                                                 field='initial value',
                                                                 message='initial value invalid')

        self.assertTrue(contract.is_valid)


class IsBetweenMixinTests(unittest.TestCase):
    def test_should_is_valid_false_when_is_between_is_called_with_value_is_not_in_range_of_to(self):
        begin_date = datetime(year=2019, month=1, day=1)
        end_data = datetime(year=2019, month=1, day=30)
        today = datetime(year=2019, month=2, day=1)

        contract = Contract().requires().is_between(value=today,
                                                    of=begin_date,
                                                    to=end_data,
                                                    field="birthday",
                                                    message='birthday invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_between_is_called_with_value_in_range_of_to(self):
        begin_date = datetime(year=2019, month=1, day=1)
        end_date = datetime(year=2019, month=1, day=30)
        today = datetime(year=2019, month=1, day=15)

        contract = Contract().requires().is_between(value=today,
                                                    of=begin_date,
                                                    to=end_date,
                                                    field='birthday',
                                                    message='birthday invalid')

        self.assertTrue(contract.is_valid)


class IsNoneMixinTests(unittest.TestCase):
    def test_should_is_valid_false_when_is_none_is_called_with_value_not_none(self):
        contract = Contract().requires().is_none(value='anything',
                                                 field='name',
                                                 message='name invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_none_is_called_with_value_none(self):
        contract = Contract().requires().is_none(value=None,
                                                 field='anything',
                                                 message='anything')

        self.assertTrue(contract.is_valid)


class AreEqualsMixinTests(unittest.TestCase):
    def test_should_is_valid_false_when_are_equals_is_called_with_value_is_not_equal_comparer(self):
        contract = Contract().requires().are_equals(value=10,
                                                    comparer=100,
                                                    field='wallet',
                                                    message='wallet invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_are_equals_is_called_with_value_is_equal_comparer(self):
        contract = Contract().requires().are_equals(value=100,
                                                    comparer=100,
                                                    field='wallet',
                                                    message='wallet invalid')

        self.assertTrue(contract.is_valid)


class AreNotEqualsMixin(unittest.TestCase):
    def test_should_is_valid_false_when_are_not_equals_is_called_with_value_are_equal_to_comparer(self):
        contract = Contract().requires().are_not_equals(value=10,
                                                        comparer=10,
                                                        field='wallet',
                                                        message='wallet invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_are_not_equals_is_called_with_value_are_not_equal_to_comparer(self):
        contract = Contract().requires().are_not_equals(value=11,
                                                        comparer=10,
                                                        field='wallet',
                                                        message='wallet invalid')

        self.assertTrue(contract.is_valid)


class IsEmptyMixinTests(unittest.TestCase):
    def test_should_is_valid_false_when_is_empty_is_called_with_value_is_not_empty(self):
        contract = Contract().requires().is_empty(value=uuid.uuid4(),
                                                  field='id',
                                                  message='id invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_empty_is_called_with_value_is_empty(self):
        contract = Contract().requires().is_empty(value="",
                                                  field='id',
                                                  message='id invalid')

        self.assertTrue(contract.is_valid)
