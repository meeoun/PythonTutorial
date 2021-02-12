class Person:
    def __init__(self, record: dict):
        self.first_name = record['first_name']
        self.last_name = record['last_name']
