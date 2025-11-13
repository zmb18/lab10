import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World from Zora Banbouk!")


if __name__ == "__main__":
    unittest.main()
