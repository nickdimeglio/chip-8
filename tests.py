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

    def test_op00E0(instruction):
        self.AssertEqual(decode("00E0"), op00E0)


    def tes_op00EE(instruction):
        self.AssertEqual(decode("00EE"), op00EE)

    #
    # def op1NNN(instruction):
    #     return 0
    #
    #
    # def op2NNN(instruction):
    #     return 0
    #
    #
    # def op3XNN(instruction):
    #     return 0
    #
    #
    # def op4XNN(instruction):
    #     return 0


    # def op5XY0(instruction):
    #     return 0
    #
    #
    # def op6XNN(instruction):
    #     return 0
    #
    #
    # def op7XNN(instruction):
    #     return 0
    #
    #
    # def op8XY0(instruction):
    #     return 0
    #
    #
    # def op8XY1(instruction):
    #     return 0
    #
    #
    # def op8XY2(instruction):
    #     return 0
    #
    #
    # def op8XY3(instruction):
    #     return 0
    #
    #
    # def op8XY4(instruction):
    #     return 0
    #
    #
    # def op8XY5(instruction):
    #     return 0
    #
    #
    # def op8XY6(instruction):
    #     return 0
    #
    #
    # def op8XY7(instruction):
    #     return 0
    #
    #
    # def op8XYE(instruction):
    #     return 0
    #
    #
    # def op9XY0(instruction):
    #     return 0
    #
    #
    # def opANNN(instruction):
    #     return 0
    #
    #
    # def opBNNN(instruction):
    #     return 0
    #
    #
    # def opCXNN(instruction):
    #     return 0
    #
    #
    # def opDXYN(instruction):
    #     return 0
    #
    #
    # def opEX9E(instruction):
    #     return 0
    #
    #
    # def opEXA1(instruction):
    #     return 0
    #
    #
    # def opFX07(instruction):
    #     return 0
    #
    #
    # def opFX0A(instruction):
    #     return 0
    #
    #
    # def opFX15(instruction):
    #     return 0
    #
    #
    # def opFX18(instruction):
    #     return 0
    #
    #
    # def opFX1E(instruction):
    #     return 0
    #
    #
    # def opFX29(instruction):
    #     return 0
    #
    #
    # def opFX33(instruction):
    #     return 0
    #
    #
    # def opFX55(instruction):
    #     return 0
    #
    #
    # def opFX65(instruction):
    #     return 0

# class TestOpCodes(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
