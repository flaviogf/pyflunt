<h1 align="center">
  Pyflunt
  <br>
  <img src="https://img.shields.io/github/license/flaviogf/pyflunt.svg" />
  <img src="https://img.shields.io/pypi/v/pyflunt.svg" />
  <img src="https://travis-ci.org/flaviogf/pyflunt.svg?branch=master" />
</h1>

<p align="center">
  <a href="#rocket-project">Project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#computer-techs">Techs</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#thinking-how-to-use">How to use</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-license">License</a>
</p>

## :rocket: Project

:wolf: Python implementation of Domain Notification Pattern based in Flunt(.NET), JFlunt(Java) developed by @andrebaltieri, @carlosbritojun

## :computer: Techs

- [Python3.7](https://www.python.org/)

## :thinking: How to use

### Installation

````bash
pip install pyflunt
````

### Notifiable

````python
from pyflunt.notifications import Notifiable, Notification

class Name(Notifiable):
    def __init__(self, name):
        super().__init__()
        
        if len(name) > 3:
            self.add_notification(Notification(field='name', message='invalid name'))

        self._name = name
````

### Contract
````python
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
````

## :memo: License

This project contains the MIT license. See the file [LICENSE](LICENSE).
