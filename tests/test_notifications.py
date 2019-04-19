import unittest

from pyflunt.notifications import Notifiable


class NotifiableTests(unittest.TestCase):
    def test_add_notification_property_and_message_is_valid(self):
        name = Name()

        self.assertFalse(name.is_valid)

    def test_add_notification_property_and_message_len_notifications(self):
        name = Name()

        self.assertEqual(1, len(name.notifications))


class Name(Notifiable):
    def __init__(self):
        super().__init__()

        self.add_notification(field='first_name', message='name invalid')
