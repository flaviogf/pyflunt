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
        contract = Contract().requires().is_empty(value='',
                                                  field='id',
                                                  message='id invalid')

        self.assertTrue(contract.is_valid)


class IsNotEmptyMixinTests(unittest.TestCase):
    def test_should_is_valid_false_when_is_not_empty_is_called_with_value_is_empty(self):
        contract = Contract().requires().is_not_empty(value='',
                                                      field='id',
                                                      message='id invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_true_when_is_not_empty_is_called_with_value_is_not_empty(self):
        contract = Contract().requires().is_not_empty(value=uuid.uuid4(),
                                                      field='id',
                                                      message='id invalid')

        self.assertTrue(contract.is_valid)


class HasMinLenMixinTests(unittest.TestCase):
    def test_should_is_valid_true_when_has_min_len_is_called_with_value_contains_minimum_len(self):
        contract = Contract().requires().has_min_len(value='Steve',
                                                     minimum=5,
                                                     field='name',
                                                     message='name invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_has_min_len_is_called_with_value_is_none(self):
        contract = Contract().requires().has_min_len(value=None,
                                                     minimum=5,
                                                     field='name',
                                                     message='name invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_false_when_has_min_len_is_called_with_value_dont_contains_minimum_len(self):
        contract = Contract().requires().has_min_len(value='Steve',
                                                     minimum=6,
                                                     field='name',
                                                     message='name invalid')

        self.assertFalse(contract.is_valid)


class HasMaxLenMixin(unittest.TestCase):
    def test_should_is_valid_true_when_has_max_len_is_called_with_value_contains_maximum_len(self):
        contract = Contract().requires().has_max_len(value='Steve',
                                                     maximum=5,
                                                     field='name',
                                                     message='name invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_true_when_has_max_len_is_called_with_value_has_less_maximum_len(self):
        contract = Contract().requires().has_max_len(value='Steve',
                                                     maximum=10,
                                                     field='name',
                                                     message='name invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_has_max_len_is_called_with_value_has_more_maximum_len(self):
        contract = Contract().requires().has_max_len(value='Steve',
                                                     maximum=2,
                                                     field='name',
                                                     message='name invalid')

        self.assertFalse(contract.is_valid)


class HasLenMixin(unittest.TestCase):
    def test_should_is_valid_true_when_has_len_is_called_with_value_has_same_than_length(self):
        contract = Contract().requires().has_len(value='Steve',
                                                 length=5,
                                                 field='name',
                                                 message='name invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_has_len_is_called_with_value_none(self):
        contract = Contract().requires().has_len(value=None,
                                                 length=5,
                                                 field='name',
                                                 message='name invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_false_when_has_len_is_called_with_value_different_than_len(self):
        contract = Contract().requires().has_len(value=None,
                                                 length=5,
                                                 field='name',
                                                 message='name invalid')

        self.assertFalse(contract.is_valid)


class ContainsMixinTests(unittest.TestCase):
    def test_should_is_valid_true_when_contains_is_called_with_value_in_text(self):
        contract = Contract().requires().contains(value='eve',
                                                  text='Steve',
                                                  field='name',
                                                  message='name invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_contains_is_called_with_value_not_in_text(self):
        contract = Contract().requires().contains(value='Stark',
                                                  text='Steve',
                                                  field='name',
                                                  message='name invalid')

        self.assertFalse(contract.is_valid)


class IsEmailMixinTests(unittest.TestCase):
    def test_should_is_valid_true_when_is_email_is_called_with_a_valid_email(self):
        contract = Contract().requires().is_email(value='parker_spiderman2001@gmail.com.br',
                                                  field='email',
                                                  message='email invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_is_email_is_called_with_a_invalid_email(self):
        contract = Contract().requires().is_email(value='parker_spiderman2001@gmail',
                                                  field='email',
                                                  message='email invalid')

        self.assertFalse(contract.is_valid)


class IsEmailOrEmptyMixinTests(unittest.TestCase):
    def test_should_is_valid_true_when_is_email_or_empty_is_called_with_empty_value(self):
        contract = Contract().requires().is_email_or_empty(value='',
                                                           field='email',
                                                           message='email invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_true_when_is_email_or_empty_is_called_with_valid_email(self):
        contract = Contract().requires().is_email_or_empty(value='parker_spiderman2001@gmail.com.br',
                                                           field='email',
                                                           message='email invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_is_email_or_empty_is_called_with_invalid_email(self):
        contract = Contract().requires().is_email_or_empty(value='parker_spiderman2001@gmail',
                                                           field='email',
                                                           message='email invalid')

        self.assertFalse(contract.is_valid)


class IsUrlMixinTests(unittest.TestCase):
    def test_should_is_valid_true_when_is_url_is_called_with_valid_url(self):
        contract = Contract().requires().is_url(value='https://www.google.com',
                                                field='site',
                                                message='site invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_is_url_is_called_with_invalid_url(self):
        contract = Contract().requires().is_url(value='invalid url',
                                                field='site',
                                                message='site invalid')

        self.assertFalse(contract.is_valid)


class IsUrlOrEmptyMixin(unittest.TestCase):
    def test_should_is_valid_true_when_is_url_or_empty_is_called_with_empty_value(self):
        contract = Contract().requires().is_url_or_empty(value='',
                                                         field='site',
                                                         message='site invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_true_when_is_url_or_empty_is_called_with_valid_url(self):
        contract = Contract().requires().is_url_or_empty(value='https://www.google.com',
                                                         field='site',
                                                         message='site invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_is_url_or_empty_is_called_with_invalid_url(self):
        contract = Contract().requires().is_url_or_empty(value='invalid url',
                                                         field='site',
                                                         message='site invalid')

        self.assertFalse(contract.is_valid)


class MatchMixinTests(unittest.TestCase):
    def test_should_is_valid_true_when_match_is_called_with_value_match_pattern(self):
        contract = Contract().requires().match(value='Tony Stark',
                                               pattern=r".*(stark).*",
                                               field='name',
                                               message='invalid name')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_match_is_called_with_value_doesnt_match(self):
        contract = Contract().requires().match(value='Tony Stark',
                                               pattern=r".*(steve).*",
                                               field='name',
                                               message='invalid name')

        self.assertFalse(contract.is_valid)


class IsDigitMixinTests(unittest.TestCase):
    def test_should_is_valid_true_when_is_digit_is_called_with_digit_text(self):
        contract = Contract().requires().is_digit(value='2020',
                                                  field='year',
                                                  message='year invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_true_when_is_digit_is_called_with_non_digit_text(self):
        contract = Contract().requires().is_digit(value='Text',
                                                  field='year',
                                                  message='year invalid')

        self.assertFalse(contract.is_valid)


class IsNotNoneOrEmptyMixinTests(unittest.TestCase):
    def test_should_is_valid_true_when_is_not_none_or_empty_is_called_with_value_is_not_none_or_empty(self):
        contract = Contract().requires().is_not_none_or_empty(value='Anything',
                                                              field='name',
                                                              message='name invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_is_not_none_or_empty_is_called_with_value_none(self):
        contract = Contract().requires().is_not_none_or_empty(value=None,
                                                              field='name',
                                                              message='name invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_false_when_is_not_none_or_empty_is_called_with_value_empty(self):
        contract = Contract().requires().is_not_none_or_empty(value="",
                                                              field='name',
                                                              message='name invalid')

        self.assertFalse(contract.is_valid)


class IsNotNoneOrWhiteSpaceTest(unittest.TestCase):
    def test_should_is_valid_true_when_is_not_none_or_white_space_is_called_with_value_not_none_or_white_space(self):
        contract = Contract().requires().is_not_none_or_white_space(value='Anything',
                                                                    field='name',
                                                                    message='name invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_is_not_none_or_white_space_is_called_with_value_white_space(self):
        contract = Contract().requires().is_not_none_or_white_space(value='   ',
                                                                    field='name',
                                                                    message='name invalid')

        self.assertFalse(contract.is_valid)

    def test_should_is_valid_false_when_is_not_none_or_white_space_is_called_with_value_none(self):
        contract = Contract().requires().is_not_none_or_white_space(value=None,
                                                                    field='name',
                                                                    message='name invalid')

        self.assertFalse(contract.is_valid)


class IsNoneOrEmptyMixinTest(unittest.TestCase):
    def test_should_is_valid_true_when_is_none_or_empty_is_called_with_value_none(self):
        contract = Contract().requires().is_none_or_empty(value=None,
                                                          field='contact',
                                                          message='contact invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_true_when_is_none_or_empty_is_called_with_value_empty(self):
        contract = Contract().requires().is_none_or_empty(value='',
                                                          field='contact',
                                                          message='contact invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_is_none_or_empty_is_called_with_non_empty_value(self):
        contract = Contract().requires().is_none_or_empty(value='Anything',
                                                          field='contact',
                                                          message='contact invalid')

        self.assertFalse(contract.is_valid)


class HasMinLengthIfNotNoneOrEmptyMixinTests(unittest.TestCase):
    def test_should_is_valid_true_when_has_min_length_if_not_none_or_empty_is_called_with_value_none(self):
        contract = Contract().requires().has_min_length_if_not_none_or_empty(value=None,
                                                                             minimum=1,
                                                                             field='contact',
                                                                             message='contact invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_true_when_has_min_length_if_not_none_or_empty_is_called_with_value_empty(self):
        contract = Contract().requires().has_min_length_if_not_none_or_empty(value='',
                                                                             minimum=1,
                                                                             field='contact',
                                                                             message='contact invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_true_when_has_min_length_if_not_none_or_empty_is_called_with_value_contains_minimum_length(
            self):
        contract = Contract().requires().has_min_length_if_not_none_or_empty(value='Steve',
                                                                             field='contact',
                                                                             minimum=5,
                                                                             message='contact invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_false_when_has_min_length_if_not_none_or_empty_is_called_with_value_doesnt_contains_minimum_length(
            self):
        contract = Contract().requires().has_min_length_if_not_none_or_empty(value='Steve',
                                                                             field='contact',
                                                                             minimum=6,
                                                                             message='contact invalid')

        self.assertFalse(contract.is_valid)


class HasMaxLengthIfNotNoneOrEmptyMixinTests(unittest.TestCase):
    def test_should_is_valid_true_when_has_max_length_if_not_none_or_empty_is_called_with_value_none(self):
        contract = Contract().requires().has_max_length_if_not_none_or_empty(value=None,
                                                                             maximum=10,
                                                                             field='contact',
                                                                             message='contact invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_true_when_has_max_length_if_not_none_or_empty_is_called_with_value_empty(self):
        contract = Contract().requires().has_max_length_if_not_none_or_empty(value='',
                                                                             maximum=10,
                                                                             field='contact',
                                                                             message='contact invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_true_when_has_max_length_if_not_none_or_empty_is_called_with_value_contains_maximum_length(
            self):
        contract = Contract().requires().has_max_length_if_not_none_or_empty(value='Steve',
                                                                             maximum=5,
                                                                             field='contact',
                                                                             message='contact invalid')

        self.assertTrue(contract.is_valid)

    def test_should_is_valid_true_when_has_max_length_if_not_none_or_empty_is_called_with_value_exceed_maximum(self):
        contract = Contract().requires().has_max_length_if_not_none_or_empty(value='Steve',
                                                                             maximum=4,
                                                                             field='contact',
                                                                             message='contact invalid')

        self.assertFalse(contract.is_valid)
