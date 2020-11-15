"""Tests for the chip8 implementation"""
import unittest
from chip8 import *
from opcodes import *

class TestChip8(unittest.TestCase):

    def test_instantiation(self):
        chippy = Chip8()
        self.assertTrue(isinstance(chippy, Chip8))


class TestDecoding(unittest.TestCase):
    """Test the decode function on each opcode"""

    def test_op00E0(self):
        self.assertEqual(decode("00E0"), op00E0)


    def test_op00EE(self):
        self.assertEqual(decode("00EE"), op00EE)


    def test_op1NNN(self):
        self.assertEqual(decode("18AF"), op1NNN)


    def test_op2NNN(self):
        self.assertEqual(decode("2A1B"), op2NNN)


    def test_op3XNN(self):
        self.assertEqual(decode("3198"), op3XNN)


    def test_op4XNN(self):
        self.assertEqual(decode("4FAB"), op4XNN)


    def test_op5XY0(self):
        self.assertEqual(decode("5550"), op5XY0)


    def test_op6XNN(self):
        self.assertEqual(decode("691F"), op6XNN)


    def test_op7XNN(self):
        self.assertEqual(decode("7B10"), op7XNN)


    def test_op8XY0(self):
        self.assertEqual(decode("8AB0"), op8XY0)


    def test_op8XY1(self):
        self.assertEqual(decode("83E1"), op8XY1)


    def test_op8XY2(self):
        self.assertEqual(decode("87C2"), op8XY2)


    def test_op8XY3(self):
        self.assertEqual(decode("84A3"), op8XY3)


    def test_op8XY4(self):
        self.assertEqual(decode("8994"), op8XY4)


    def test_op8XY5(self):
        self.assertEqual(decode("8CD5"), op8XY5)


    def test_op8XY6(self):
        self.assertEqual(decode("81A6"), op8XY6)


    def test_op8XY7(self):
        self.assertEqual(decode("8997"), op8XY7)


    def test_op8XYE(self):
        self.assertEqual(decode("8DFE"), op8XYE)


    def test_op9XY0(self):
        self.assertEqual(decode("99A0"), op9XY0)


    def test_opANNN(self):
        self.assertEqual(decode("AABC"), opANNN)


    def test_opBNNN(self):
        self.assertEqual(decode("B543"), opBNNN)


    def test_opCXNN(self):
        self.assertEqual(decode("C9BC"), opCXNN)


    def test_opDXYN(self):
        self.assertEqual(decode("D12E"), opDXYN)


    def test_opEX9E(self):
        self.assertEqual(decode("E89E"), opEX9E)


    def test_opEXA1(self):
        self.assertEqual(decode("EEA1"), opEXA1)


    def test_opFX07(self):
        self.assertEqual(decode("FA07"), opFX07)


    def test_opFX0A(self):
        self.assertEqual(decode("F10A"), opFX0A)


    def test_opFX15(self):
        self.assertEqual(decode("F015"), opFX15)


    def test_opFX18(self):
        self.assertEqual(decode("FD18"), opFX18)


    def test_opFX1E(self):
        self.assertEqual(decode("F81E"), opFX1E)


    def test_opFX29(self):
        self.assertEqual(decode("F229"), opFX29)


    def test_opFX33(self):
        self.assertEqual(decode("FA33"), opFX33)


    def test_opFX55(self):
        self.assertEqual(decode("F655"), opFX55)


    def test_opFX65(self):
        self.assertEqual(decode("F165"), opFX65)

class TestOpCodes(unittest.TestCase):
        def test_op00E0(self):
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
