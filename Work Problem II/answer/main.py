from File import File
from Person import Person
from Contact import Contact
from Stat import Stat
from Account import Account

source = "C:\\Users\\kpark\\Downloads\\MOCK_DATA.csv"
destination = "C:\\Users\\kpark\\Downloads\\"

file = File(source, destination)
accounts = list()
for record in file.get_accounts():
    person = Person(record)
    stat = Stat(record)
    contact = Contact(record)
    account = Account(record, person, contact, stat)
    accounts.append(account)
file.write_accounts(accounts)

