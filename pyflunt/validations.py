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


class IsGreaterThanOrEqualsMixin:
    def is_greater_than_or_equals(self, value, comparer, field, message):
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


class RequiresMixin:
    def requires(self):
        return self


class Contract(IsFalseMixin,
               IsTrueMixin,
               IsGreaterThanMixin,
               IsGreaterThanOrEqualsMixin,
               IsLowerThanMixin,
               IsLowerOrEqualsMixin,
               RequiresMixin,
               Notifiable):
    pass
