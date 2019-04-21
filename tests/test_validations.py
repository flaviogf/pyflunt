import unittest

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
    def test_should_is_valid_false_when_is_greater_than_or_equals_is_called_with_value_lower_than_comparer(self):
        contract = Contract().requires().is_greater_than_or_equals(value=10,
                                                                   comparer=100.99,
                                                                   field='initial value',
                                                                   message='initial value invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_greater_than_or_equals_is_called_with_value_equal_than_comparer(self):
        contract = Contract().requires().is_greater_than_or_equals(value=100.99,
                                                                   comparer=100.99,
                                                                   field='initial value',
                                                                   message='initial value invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_true_when_is_greater_than_or_equals_is_called_with_value_greater_than_comparer(self):
        contract = Contract().requires().is_greater_than_or_equals(value=100.99,
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
