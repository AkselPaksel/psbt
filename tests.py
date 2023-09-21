"""
This file runs relevant tests for this project
"""
import unittest
from multisig import create_private_keys
import bitcoin

class TestSequenceFunctions(unittest.TestCase):

    def test_create_wallets(self):
        # Test with different numbers of keys
        for num_keys in [1, 5, 10]:
            private_keys = create_private_keys(num_keys)
            self.assertEqual(len(private_keys), num_keys)

        # Test with an invalid number of keys (e.g., negative)
        with self.assertRaises(ValueError):
            create_private_keys(-1)

if __name__ == '__main__':
    unittest.main()