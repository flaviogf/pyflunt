import re

from pyflunt.notifications import Notifiable, Notification


class IsFalseMixin:
    def is_false(self, value, field, message):
        if value:
            self.add_notification(Notification(field, message))

        return self


class IsTrueMixin:
    def is_true(self, value, field, message):
        if not value:
            self.add_notification(Notification(field, message))

        return self


class IsGreaterThanMixin:
    def is_greater_than(self, value, comparer, field, message):
        if value <= comparer:
            self.add_notification(Notification(field, message))

        return self


class IsGreaterOrEqualsMixin:
    def is_greater_or_equals_than(self, value, comparer, field, message):
        if value < comparer:
            self.add_notification(Notification(field, message))

        return self


class IsLowerThanMixin:
    def is_lower_than(self, value, comparer, field, message):
        if value >= comparer:
            self.add_notification(Notification(field, message))

        return self


class IsLowerOrEqualsMixin:
    def is_lower_or_equals_than(self, value, comparer, field, message):
        if value > comparer:
            self.add_notification(Notification(field, message))

        return self


class IsBetweenMixin:
    def is_between(self, value, of, to, field, message):
        if not (of < value < to):
            self.add_notification(Notification(field, message))

        return self


class IsNoneMixin:
    def is_none(self, value, field, message):
        if value is not None:
            self.add_notification(Notification(field, message))

        return self


class AreEqualsMixin:
    def are_equals(self, value, comparer, field, message):
        if value != comparer:
            self.add_notification(Notification(field, message))

        return self


class AreNotEqualsMixin:
    def are_not_equals(self, value, comparer, field, message):
        if value == comparer:
            self.add_notification(Notification(field, message))

        return self


class IsEmptyMixin:
    def is_empty(self, value, field, message):
        if value:
            self.add_notification(Notification(field, message))

        return self


class IsNotEmptyMixin:
    def is_not_empty(self, value, field, message):
        if not value:
            self.add_notification(Notification(field, message))

        return self


class HasMinLenMixin:
    def has_min_len(self, value, minimum, field, message):
        if not value or len(value) < minimum:
            self.add_notification(Notification(field, message))

        return self


class HasMaxLenMixin:
    def has_max_len(self, value, maximum, field, message):
        if not value or len(value) > maximum:
            self.add_notification(Notification(field, message))

        return self


class HasLenMixin:
    def has_len(self, value, length, field, message):
        if not value or len(value) != length:
            self.add_notification(Notification(field, message))

        return self


class ContainsMixin:
    def contains(self, value, text, field, message):
        if value not in text:
            self.add_notification(Notification(field, message))

        return self


class IsEmailMixin:
    def is_email(self, value, field, message):
        if not _valid_email(value):
            self.add_notification(Notification(field, message))

        return self


class IsEmailOrEmptyMixin:
    def is_email_or_empty(self, value, field, message):
        if not value or _valid_email(value):
            return self

        self.add_notification(Notification(field, message))

        return self


class IsUrlMixin:
    def is_url(self, value, field, message):
        if not _valid_url(value):
            self.add_notification(Notification(field, message))

        return self


class IsUrlOrEmptyMixin:
    def is_url_or_empty(self, value, field, message):
        if not value or _valid_url(value):
            return self

        self.add_notification(Notification(field, message))

        return self


class MatchMixin:
    def match(self, value, pattern, field, message):
        if not re.match(pattern, value, re.IGNORECASE):
            self.add_notification(Notification(field, message))

        return self


class IsDigitMixin:
    def is_digit(self, value, field, message):
        if not value.isdigit():
            self.add_notification(Notification(field, message))

        return self


class IsNotNoneOrEmptyMixin:
    def is_not_none_or_empty(self, value, field, message):
        if not value:
            self.add_notification(Notification(field, message))

        return self


class IsNotNoneOrWhiteSpaceMixin:
    def is_not_none_or_white_space(self, value, field, message):
        if not value or str(value).isspace():
            self.add_notification(Notification(field, message))

        return self


class IsNoneOrEmptyMixin:
    def is_none_or_empty(self, value, field, message):
        if value:
            self.add_notification(Notification(field, message))

        return self


class HasMinLengthIfNotNoneOrEmptyMixin:
    def has_min_length_if_not_none_or_empty(self, value, minimum, field, message):
        if value and len(value) < minimum:
            self.add_notification(Notification(field, message))

        return self


class HasMaxLengthIfNotNoneOrEmptyMixin:
    def has_max_length_if_not_none_or_empty(self, value, maximum, field, message):
        if value and len(value) > maximum:
            self.add_notification(Notification(field, message))

        return self


class HasExactLengthIfNotNoneOrEmptyMixin:
    def has_exact_length_if_not_none_or_empty(self, value, length, field, message):
        if value and len(value) != length:
            self.add_notification(Notification(field, message))

        return self


def _valid_email(value):
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value, re.IGNORECASE)


def _valid_url(value):
    pattern = r"^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"
    return re.match(pattern, value)


class RequiresMixin:
    def requires(self):
        return self


class Contract(IsFalseMixin,
               IsTrueMixin,
               IsGreaterThanMixin,
               IsGreaterOrEqualsMixin,
               IsLowerThanMixin,
               IsLowerOrEqualsMixin,
               IsBetweenMixin,
               IsNoneMixin,
               AreEqualsMixin,
               AreNotEqualsMixin,
               IsEmptyMixin,
               IsNotEmptyMixin,
               HasMinLenMixin,
               HasMaxLenMixin,
               HasLenMixin,
               ContainsMixin,
               IsEmailMixin,
               IsEmailOrEmptyMixin,
               IsUrlMixin,
               IsUrlOrEmptyMixin,
               MatchMixin,
               IsDigitMixin,
               IsNotNoneOrEmptyMixin,
               IsNotNoneOrWhiteSpaceMixin,
               IsNoneOrEmptyMixin,
               HasMinLengthIfNotNoneOrEmptyMixin,
               HasMaxLengthIfNotNoneOrEmptyMixin,
               HasExactLengthIfNotNoneOrEmptyMixin,
               RequiresMixin,
               Notifiable):
    pass
