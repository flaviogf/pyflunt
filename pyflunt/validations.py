from pyflunt.notifications import Notifiable, Notification


class BoolValidationContractMixin:
    def is_false(self, value, field, message):
        if value:
            self.add_notification(Notification(field, message))

        return self

    def is_true(self, value, field, message):
        return self.is_false(not value, field, message)


class DateTimeValidationContractMixin:
    def is_greater_than(self, value, comparer, field, message):
        if value < comparer:
            self.add_notification(Notification(field, message))

        return self


class Contract(BoolValidationContractMixin, DateTimeValidationContractMixin,
               Notifiable):
    def requires(self):
        return self
