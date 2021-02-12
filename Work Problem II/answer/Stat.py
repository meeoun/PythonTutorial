class Stat:
    def __init__(self, record: dict):
        self.positive_contacts = int(record['positive_contacts'])
        self.negative_contacts = int(record['negative_contacts'])
        self.payment_count = int(record['payment_count'])
        self.contact = int(record['contact'])

    def get_score(self):
        return - (self.negative_contacts * 100) \
               + (self.contact * 10) \
               + (self.payment_count * 100) \
               + self.promise_pay()

    def promise_pay(self):
        if self.payment_count < 1 and self.positive_contacts > 3:
            return -self.positive_contacts * 100
        else:
            return self.positive_contacts * 100



