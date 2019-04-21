from pyflunt.notifications import Notifiable, Notification


class IsFalseMixin:
    def is_false(self, value, field, message):
        if value:
            self.add_notification(Notification(field, message))

        return self


class IsTrueMixin:
    def is_true(self, value, field, message):
        return self.is_false(not value, field, message)


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
               RequiresMixin,
               Notifiable):
    pass
