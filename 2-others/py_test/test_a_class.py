
# Testing a Class
#     - Testing a class is similar to testing a function, as you’ll most likely be testing your methods.

import unittest
from accountant import Accountant

class AccTestCase(unittest.TestCase):
    """Tests for the class Accountant."""

    def test_balance(self):
        # Default balance should be 0
        acc = Accountant()
        self.assertEqual(acc.balance, 0)
        
        # Test non-default balance
        acc = Accountant(100)
        self.assertEqual(acc.balance, 100)

# Using the setUp() method for making use of same object for multiple tests

class TestAccountant(unittest.TestCase):
    """Tests for the class Accountant."""
    
    def setUp(self):
        self.acc = Accountant()
    
    def test_initial_balance(self):
        # Default balance should be 0.
        self.assertEqual(self.acc.balance, 0)
        # Test non-default balance.
        acc = Accountant(100)
        self.assertEqual(acc.balance, 100)
    
    def test_deposit(self):
        # Test single deposit.
        self.acc.deposit(100)
        self.assertEqual(self.acc.balance, 100)
        # Test multiple deposits.
        self.acc.deposit(100)
        self.acc.deposit(100)
        self.assertEqual(self.acc.balance, 300)

    def test_withdrawal(self):
        # Test single withdrawal.
        self.acc.deposit(1000)
        self.acc.withdraw(100)
        self.assertEqual(self.acc.balance, 900)

unittest.main()