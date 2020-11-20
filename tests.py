"""Tests for the chip8 implementation"""
import unittest
from chip8 import *
from opcodes import *

class TestChip8(unittest.TestCase):

    def test_instantiation(self):
        chip = Chip8()
        self.assertTrue(isinstance(chip, Chip8))


class TestDecoding(unittest.TestCase):
    """Test the decode function on each opcode"""

    def test_op00E0(self):
        self.assertEqual(decode(0x00E0), op00E0)


    def test_op00EE(self):
        self.assertEqual(decode(0x00EE), op00EE)


    def test_op1NNN(self):
        self.assertEqual(decode(0x18AF), op1NNN)


    def test_op2NNN(self):
        self.assertEqual(decode(0x2A1B), op2NNN)


    def test_op3XNN(self):
        self.assertEqual(decode(0x3198), op3XNN)


    def test_op4XNN(self):
        self.assertEqual(decode(0x4FAB), op4XNN)


    def test_op5XY0(self):
        self.assertEqual(decode(0x5550), op5XY0)


    def test_op6XNN(self):
        self.assertEqual(decode(0x691F), op6XNN)


    def test_op7XNN(self):
        self.assertEqual(decode(0x7B10), op7XNN)


    def test_op8XY0(self):
        self.assertEqual(decode(0x8AB0), op8XY0)


    def test_op8XY1(self):
        self.assertEqual(decode(0x83E1), op8XY1)


    def test_op8XY2(self):
        self.assertEqual(decode(0x87C2), op8XY2)


    def test_op8XY3(self):
        self.assertEqual(decode(0x84A3), op8XY3)


    def test_op8XY4(self):
        self.assertEqual(decode(0x8994), op8XY4)


    def test_op8XY5(self):
        self.assertEqual(decode(0x8CD5), op8XY5)


    def test_op8XY6(self):
        self.assertEqual(decode(0x81A6), op8XY6)


    def test_op8XY7(self):
        self.assertEqual(decode(0x8997), op8XY7)


    def test_op8XYE(self):
        self.assertEqual(decode(0x8DFE), op8XYE)


    def test_op9XY0(self):
        self.assertEqual(decode(0x99A0), op9XY0)


    def test_opANNN(self):
        self.assertEqual(decode(0xAABC), opANNN)


    def test_opBNNN(self):
        self.assertEqual(decode(0xB543), opBNNN)


    def test_opCXNN(self):
        self.assertEqual(decode(0xC9BC), opCXNN)


    def test_opDXYN(self):
        self.assertEqual(decode(0xD12E), opDXYN)


    def test_opEX9E(self):
        self.assertEqual(decode(0xE89E), opEX9E)


    def test_opEXA1(self):
        self.assertEqual(decode(0xEEA1), opEXA1)


    def test_opFX07(self):
        self.assertEqual(decode(0xFA07), opFX07)


    def test_opFX0A(self):
        self.assertEqual(decode(0xF10A), opFX0A)


    def test_opFX15(self):
        self.assertEqual(decode(0xF015), opFX15)


    def test_opFX18(self):
        self.assertEqual(decode(0xFD18), opFX18)


    def test_opFX1E(self):
        self.assertEqual(decode(0xF81E), opFX1E)


    def test_opFX29(self):
        self.assertEqual(decode(0xF229), opFX29)


    def test_opFX33(self):
        self.assertEqual(decode(0xFA33), opFX33)


    def test_opFX55(self):
        self.assertEqual(decode(0xF655), opFX55)


    def test_opFX65(self):
        self.assertEqual(decode(0xF165), opFX65)


class TestOpCodes(unittest.TestCase):


        def test_op00E0(self):
            """Clears the screen"""
            True


        def test_op00EE(self):
            """Returns from a subroutine"""
            chip = Chip8()
            # Program is currently at 0x600
            chip.pc = 0x600
            # Call subroutine at 0x400
            op2NNN(chip, 0x2400)
            # Return to 0x600
            op00EE(chip, 0x00EE)
            self.assertEqual(chip.pc, 0x600)


        def test_op1NNN(self):
            """Jumps to address NNN"""
            chip = Chip8()
            op1NNN(chip, 0x1F90)
            self.assertEqual(chip.pc, 0xF90)


        def test_op2NNN(self):
            """Calls subroutine at NNN"""
            chip = Chip8()
            chip.pc = 0x301
            op2NNN(chip, 0x2ABC)
            self.assertEqual(chip.pc, 0xABC)
            # Move stack pointer down 1 before accessing stack value
            chip.sp -=1
            self.assertEqual(chip.stack[chip.sp], 0x301)


        def test_op3XNN(self):
            """Skips the next instruction if VX equals NN. Usually the next instruction
            is a jump to skip a code block"""
            chip = Chip8()
            chip.pc = 0x400
            chip.v_registers[0xA] = 0xFF

            # VX == NN, check for skip
            op3XNN(chip, 0x3AFF)
            self.assertEqual(chip.pc, 0x402)

            # VX != NN, check for no skip
            op3XNN(chip, 0X3ABC)
            self.assertTrue(chip.pc, 0x402)


        def test_op4XNN(self):
            """Skips the next instruction if VX doesn't equal NN. Usually the
            next instruction is a jump to skip a code block"""
            chip = Chip8()
            chip.pc = 0x400
            chip.v_registers[0x1] = 0xDD

            # VX == NN, check for no skip
            op4XNN(chip, 0x31DD)
            self.assertEqual(chip.pc, 0x400)

            # VX != NN, check for skip
            op4XNN(chip, 0X31FF)
            self.assertEqual(chip.pc, 0x402)


        def test_op5XY0(self):
            """Skips the next instruction if VX == VY"""
            chip = Chip8()
            chip.v_registers[0x0] = 0x5
            chip.v_registers[0x1] = 0x5
            chip.v_registers[0x2] = 0xF

            # VX == VF, check for skip
            op5XY0(chip, 0x5010)
            self.assertEqual(chip.pc, 0x202)

            # VX != VF, check for no skip
            op5XY0(chip, 0x5120)
            self.assertEqual(chip.pc, 0x202)


        def test_op6XNN(self):
            """Set VX = NN"""
            chip = Chip8()
            op6XNN(chip, 0x6B88)
            self.assertEqual(chip.v_registers[0xB], 0x88)


        def test_op7XNN(self):
            chip = Chip8()
            chip.v_registers[0xF] = 0xA
            op7XNN(chip, 0x7F01)
            self.assertEqual(chip.v_registers[0xF], 0xB)

        def test_op8XY0(self):
            True


        def test_op8XY1(self):
            True


        def test_op8XY2(self):
            True


        def test_op8XY3(self):
            True


        def test_op8XY4(self):
            True


        def test_op8XY5(self):
            True


        def test_op8XY6(self):
            True


        def test_op8XY7(self):
            True


        def test_op8XYE(self):
            True


        def test_op9XY0(self):
            True


        def test_opANNN(self):
            True


        def test_opBNNN(self):
            True


        def test_opCXNN(self):
            True


        def test_opDXYN(self):
            True

        def test_opEX9E(self):
            True


        def test_opEXA1(self):
            True


        def test_opFX07(self):
            True


        def test_opFX0A(self):
            True


        def test_opFX15(self):
            True


        def test_opFX18(self):
            True


        def test_opFX1E(self):
            True


        def test_opFX29(self):
            True


        def test_opFX33(self):
            True


        def test_opFX55(self):
            True


        def test_opFX65(self):
            True


if __name__ == '__main__':
    unittest.main()
