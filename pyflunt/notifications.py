from abc import ABC


class Notification:
    def __init__(self, field: 'str', message: 'str'):
        self._field = field
        self._message = message

    @property
    def field(self) -> 'str':
        return self._field

    @property
    def message(self) -> 'str':
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

    def add_notifications_from_notifiable(self, notifiable):
        self._notifications += notifiable.notifications
