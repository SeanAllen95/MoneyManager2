class Transaction:

    def __init__(self, amount, merchant_id, tag_id, id = None):
        self.amount = amount
        self.merchant_id = merchant_id
        self.tag_id = tag_id
        self.id = id