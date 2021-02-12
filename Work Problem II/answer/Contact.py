class Contact:
    def __init__(self, record: dict):

        self.state = record['state']
        self.address = record['address']
        self.zip = record['zip']
        self.cell = record['cell']
        self.home_phone = record['home_phone']
