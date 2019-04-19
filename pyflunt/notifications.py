from abc import ABC


class Notification:
    def __init__(self, field, message):
        self._field = field
        self._message = message

    @property
    def field(self):
        return self._field

    @property
    def message(self):
        return self._message


class Notifiable(ABC):
    def __init__(self):
        self._notifications = []

    @property
    def is_valid(self):
        return not self._notifications

    @property
    def notifications(self):
        return tuple(self._notifications)

    def add_notification(self, notification):
        self._notifications.append(notification)

    def add_notifications(self, *notifications):
        self._notifications += notifications
