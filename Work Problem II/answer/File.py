import csv
import datetime
from Account import Account


class File:
    def __init__(self, source: str, destination: str):
        self.source = source
        self.destination = f"{destination}dial{datetime.datetime.now().strftime('%Y%m%d')}.csv"

    def get_accounts(self):
        with open(self.file_path) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                yield row

    def write_accounts(self, accounts: list):
        with open(self.destination, 'w', newline='')as csv_file:
            fieldnames = ['last_name', 'first_name', 'cell', 'home', 'account#', 'score']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            account: Account
            for account in accounts:
                writer.writerow({'last_name': account.person.last_name,
                                 'first_name': account.person.first_name,
                                 'cell': account.contact.cell,
                                 'home': account.contact.home_phone,
                                 'account#': account.account_number,
                                 'score': account.stat.get_score()})
