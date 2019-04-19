import unittest

from pyflunt.notifications import Notifiable, Notification


class NotifiableTests(unittest.TestCase):
    def test_add_notification_is_valid(self):
        name = Name()

        name.add_notification(
            Notification(field='first_name', message='first name invalid'))

        self.assertFalse(name.is_valid)

    def test_add_notification_len_notifications(self):
        name = Name()

        name.add_notification(
            Notification(field='first_name', message='first name invalid'))

        self.assertEqual(1, len(name.notifications))

    def test_add_notifications_is_valid(self):
        name = Name()

        name.add_notifications(
            Notification(field='first name', message='first name invalid'),
            Notification(field='last name', message='last name invalid'),
        )

        self.assertFalse(name.is_valid)

    def test_add_notifications_len_notifications(self):
        name = Name()

        name.add_notifications(
            Notification(field='first name', message='first name invalid'),
            Notification(field='last name', message='last name invalid'),
        )

        self.assertEqual(2, len(name.notifications))


class Name(Notifiable):
    pass
