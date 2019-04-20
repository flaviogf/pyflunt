import unittest

from pyflunt.notifications import Notifiable, Notification


class Name(Notifiable):
    pass


class Customer(Notifiable):
    pass


class NotifiableTests(unittest.TestCase):
    def setUp(self):
        self._name = Name()

    def test_should_is_valid_false_when_add_notification(self):
        self._name.add_notification(
            Notification(field='first_name', message='first name invalid'))

        self.assertFalse(self._name.is_valid)

    def test_should_has_a_notification_when_add_notification(self):
        self._name.add_notification(
            Notification(field='first_name', message='first name invalid'))

        self.assertEqual(1, len(self._name.notifications))

    def test_should_is_valid_false_when_add_notifications(self):
        self._name.add_notifications(
            Notification(field='first name', message='first name invalid'),
            Notification(field='last name', message='last name invalid'),
        )

        self.assertFalse(self._name.is_valid)

    def test_should_has_two_notifications_when_add_notifications(self):
        self._name.add_notifications(
            Notification(field='first name', message='first name invalid'),
            Notification(field='last name', message='last name invalid'),
        )

        self.assertEqual(2, len(self._name.notifications))

    def test_should_is_valid_false_when_add_notifications_from_notifiable(
            self):
        self._name.add_notification(
            Notification(field='first_name', message='first name invalid'))

        steve = Customer()

        steve.add_notifications_from_notifiable(notifiable=self._name)

        self.assertFalse(steve.is_valid)

    def test_should_has_a_notification_when_add_notifications_from_notifiable(
            self):
        self._name.add_notification(
            Notification(field='first_name', message='first name invalid'))

        steve = Customer()

        steve.add_notifications_from_notifiable(notifiable=self._name)

        self.assertEqual(1, len(steve.notifications))
