# Pyflunt

[![Build Status](https://travis-ci.org/flaviogf/pyflunt.svg?branch=master)](https://travis-ci.org/flaviogf/pyflunt)
![GitHub](https://img.shields.io/github/license/flaviogf/pyflunt.svg)
![PyPI](https://img.shields.io/pypi/v/pyflunt.svg)

## Install

### Requirements

- python3.7

### Installation

```bash
pip install pyflunt
```

## How to use

### Notifiable

```python
from pyflunt.notifications import Notifiable, Notification

class Name(Notifiable):
    def __init__(self, name):
        super().__init__()
        
        if len(name) > 3:
            self.add_notification(Notification(field='name', message='invalid name'))

        self._name = name
```

### Contract
```python
from pyflunt.notifications import Notifiable
from pyflunt.validations import Contract

class Email(Notifiable):
    def __init__(self, email):
        super().__init__()

        self._email = email

        contract = (Contract().requires()
                              .has_max_len(value=email,
                                           maximum=50,
                                           message='invalid email')
                              .is_email(value=email,
                                        field='email',
                                        message='invalid email'))

        self.add_notifications(contract)
```

### Validations
is_false(self, value, field, message)

is_true(self, value, field, message)

is_greater_than(self, value, comparer, field, message)

is_greater_or_equals_than(self, value, comparer, field, message)

is_lower_than(self, value, comparer, field, message)

is_lower_or_equals_than(self, value, comparer, field, message)

is_between(self, value, of, to, field, message)

is_none(self, value, field, message)

are_equals(self, value, comparer, field, message)

are_not_equals(self, value, comparer, field, message)

is_empty(self, value, field, message)

is_not_empty(self, value, field, message)

has_min_len(self, value, minimum, field, message)

has_max_len(self, value, maximum, field, message)

has_len(self, value, length, field, message)

contains(self, value, text, field, message)

is_email(self, value, field, message)

is_email_or_empty(self, value, field, message)

is_url(self, value, field, message)
    
is_url_or_empty(self, value, field, message)

match(self, value, pattern, field, message)

is_digit(self, value, field, message)

is_not_none_or_empty(self, value, field, message)

is_not_none_or_white_space(self, value, field, message)

is_none_or_empty(self, value, field, message)

has_min_length_if_not_none_or_empty(self, value, minimum, field, message)

has_max_length_if_not_none_or_empty(self, value, maximum, field, message)

has_exact_length_if_not_none_or_empty(self, value, length, field, message)
