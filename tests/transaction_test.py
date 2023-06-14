import unittest

from models.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction = Transaction(100, 1, 2)

    def test_transaction_has_amount(self):
        self.assertEqual(100, self.transaction.amount)

    def test_transaction_has_merchant_id(self):
        self.assertEqual(1, self.transaction.merchant_id)

    def test_transaction_has_tag_id(self):
        self.assertEqual(2, self.transaction.tag_id)
    