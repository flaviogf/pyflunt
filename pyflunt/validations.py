from pyflunt.notifications import Notifiable, Notification


class IsFalseMixin:
    def is_false(self, value, field, message):
        if value:
            self.add_notification(Notification(field, message))

        return self


class IsTrueMixin:
    def is_true(self, value, field, message):
        return self.is_false(not value, field, message)


class IsGreaterThan:
    def is_greater_than(self, value, comparer, field, message):
        if value <= comparer:
            self.add_notification(Notification(field, message))

        return self


class RequiresMixin:
    def requires(self):
        return self


class Contract(IsFalseMixin,
               IsTrueMixin,
               IsGreaterThan,
               RequiresMixin,
               Notifiable):
    pass