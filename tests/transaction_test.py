import unittest

from models.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction = Transaction(100)

    def test_transaction_has_amount(self):
        self.assertEqual(100, self.transaction.amount)
    