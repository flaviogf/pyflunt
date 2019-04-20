from pyflunt.notifications import Notifiable, Notification


class BoolValidationContractMixin:
    def is_false(self, value, field, message):
        if value:
            self.add_notification(Notification(field, message))

        return self

    def is_true(self, value, field, message):
        return self.is_false(not value, field, message)


class Contract(BoolValidationContractMixin, Notifiable):
    def requires(self):
        return self
