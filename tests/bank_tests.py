# Test-driven development (TDD)

from unittest import TestCase, main
from bank import Bank

class Bank(TestCase):

    def setUp(self) -> None:
        self.account = Bank("Mahdieh", 100_000)
    

    def test_add(self):
        self.account + (10_000)
        self.assertEqual(self.account.__balance, 110_000)

    def test_add_negetive(self):
        with self.assertRaises(ValueError):
            self.account + (-95_000)
            
    def test_transfer(self):
        self.account - (10_000)
        self.assertEqual(self.account.__balance, 90_000)

    def test_sub(self):
        self.account - (110_000)
        self.assertEqual(self.account.__balance, 10_000)
    



if __name__ == "__main__":
    main() 

