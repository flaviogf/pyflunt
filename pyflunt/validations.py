from datetime import datetime
from decimal import Decimal
from typing import Union

from pyflunt.notifications import Notification


class BoolValidationContractMixin:
    def is_false(self, value: 'bool', field: 'str',
                 message: 'str') -> '__class__':
        if value:
            self.add_notification(Notification(field, message))

        return self

    def is_true(self, value: 'bool', field: 'str',
                message: 'str') -> '__class__':
        return self.is_false(not value, field, message)


class DateTimeValidationContractMixin:
    def is_greater_than(self, value: 'datetime', comparer: 'datetime',
                        field: 'str', message: 'str') -> '__class__':
        if value < comparer:
            self.add_notification(Notification(field, message))

        return self


class NumberValidationContractMixin:
    def is_greater_than(self, value: 'Union[int, float, complex, Decimal]',
                        comparer: 'Union[int, float, complex, Decimal]',
                        field: 'str', message: 'str') -> '__class__':
        if value < comparer:
            self.add_notification(Notification(field, message))

        return self


class RequiresMixin:
    def requires(self):
        return self
