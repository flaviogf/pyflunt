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
        self._notifications += self._filter_and_map_notifiables(notifications)
        self._notifications += self._filter_notifications(notifications)

    def _filter_and_map_notifiables(self, notifications):
        return [notification for notifiable in notifications
                if isinstance(notifiable, Notifiable)
                for notification in notifiable.notifications]

    def _filter_notifications(self, notifications):
        return [notification for notification in notifications
                if isinstance(notification, Notification)]
