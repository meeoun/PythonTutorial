from Person import Person
from Contact import Contact
from Stat import Stat


class Account:
    def __init__(self, record: dict, person: Person, contact: Contact, stat: Stat):
        self.account_number = record['account']
        self.person = person
        self.contact = contact
        self.stat = stat
