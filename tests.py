"""Tests for the chip8 implementation"""
import unittest
from chip8 import *

class TestChip8(unittest.TestCase):

    def test_instantiation(self):
        chippy = Chip8()
        self.assertTrue(isinstance(chippy, Chip8))

    def test_failure(self):
        chippy = Chip8()
        self.assertTrue(isinstance(chippy, bool))

if __name__ == '__main__':
    unittest.main()
