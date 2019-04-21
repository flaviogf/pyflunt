import unittest

from pyflunt.notifications import Notifiable, Notification


class Name(Notifiable):
    pass


class Customer(Notifiable):
    pass


class NotifiableTests(unittest.TestCase):
    def setUp(self):
        self._name = Name()

    def test_should_is_valid_false_when_add_notification_is_called_with_a_notification(self):
        self._name.add_notification(
            Notification(field='first_name', message='first name invalid'))

        self.assertFalse(self._name.is_valid)

    def test_should_has_a_notification_when_add_notification_is_called_with_a_notification(self):
        self._name.add_notification(
            Notification(field='first_name', message='first name invalid'))

        self.assertEqual(1, len(self._name.notifications))

    def test_should_is_valid_false_when_add_notifications_is_called_with_two_notifications(self):
        self._name.add_notifications(
            Notification(field='first name', message='first name invalid'),
            Notification(field='last name', message='last name invalid'),
        )

        self.assertFalse(self._name.is_valid)

    def test_should_has_two_notifications_when_add_notifications_is_called_with_two_notifications(self):
        self._name.add_notifications(
            Notification(field='first name', message='first name invalid'),
            Notification(field='last name', message='last name invalid'),
        )

        self.assertEqual(2, len(self._name.notifications))

    def test_should_is_valid_false_when_add_notifications_is_called_with_a_invalid_notifiable(self):
        customer = Customer()

        self._name.add_notification(Notification(field='first name', message='first name invalid'))

        customer.add_notifications(self._name)

        self.assertFalse(customer.is_valid)

    def test_should_ensure_all_notifications_is_instance_of_notification_when_add_notifications(self):
        customer = Customer()

        self._name.add_notification(Notification(field='first name', message='first name invalid'))

        customer.add_notifications(self._name)

        self.assertTrue(all(isinstance(it, Notification) for it in customer.notifications))
