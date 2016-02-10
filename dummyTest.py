#! /bin/python

import unittest

class LearningCase(unittest.TestCase):
    def test_starting_out(self):
        self.assertEqual(2,2)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
