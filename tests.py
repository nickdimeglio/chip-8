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
        chip = Chip8()
        chip.gfx[10] = 1
        chip.gfx[892] = 1
        self.assertEqual(chip.gfx[10], 1)
        self.assertEqual(chip.gfx[892], 1)
        self.assertTrue(chip.gfx != ([0] * (64 * 32)))
        op00E0(chip, 0x00E0)
        self.assertEqual(chip.gfx[10], 0)
        self.assertEqual(chip.gfx[892], 0)
        self.assertEqual(chip.gfx, ([0] * (64 * 32)))

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
        """Sets VX += NN"""
        chip = Chip8()

        # Normal Case
        chip.v_registers[0xF] = 0xA
        op7XNN(chip, 0x7F01)
        self.assertEqual(chip.v_registers[0xF], 0xB)

        # Wraparound Case
        chip.v_registers[0xA] = 0xFF
        op7XNN(chip, 0x7AAB)
        self.assertEqual(chip.v_registers[0xA], 0xAA)

    def test_op8XY0(self):
        """Sets VX = VY"""
        chip = Chip8()
        chip.v_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xFF,
                            0xAA]
        op8XY0(chip, 0x8EF0)
        self.assertEqual(0xAA, chip.v_registers[0xE])

    def test_op8XY1(self):
        """Sets VX = (VX or VY)"""
        chip = Chip8()
        chip.v_registers[0x0] = 0b10001001
        chip.v_registers[0x1] = 0b00000010
        op8XY1(chip, 0x8011)
        self.assertEqual(chip.v_registers[0x0], 0b10001011)

    def test_op8XY2(self):
        """Sets VX = (VX and VY)"""
        chip = Chip8()
        chip.v_registers[0x0] = 0b10001001
        chip.v_registers[0x1] = 0b00000010
        op8XY2(chip, 0x8011)
        self.assertEqual(chip.v_registers[0x0], 0b0000000)

    def test_op8XY3(self):
        """Sets VX = (VX xor VY)"""
        chip = Chip8()
        chip.v_registers[0x0] = 0b11010101
        chip.v_registers[0x1] = 0b11101010
        op8XY3(chip, 0x8011)
        self.assertEqual(chip.v_registers[0x0], 0b00111111)

    def test_op8XY4(self):
        """Sets VX += VY"""
        chip = Chip8()

        # Normal Case
        chip.v_registers[0xA] = 0xF0
        chip.v_registers[0xB] = 0x0F
        op8XY4(chip, 0x8AB4)
        self.assertEqual(chip.v_registers[0xA], 0xFF)
        self.assertEqual(chip.v_registers[0xF], 0x0)

        # Wraparound case
        chip.v_registers[0x1] = 0xEE
        chip.v_registers[0x2] = 0x1C
        op8XY4(chip, 0x8124)
        self.assertEqual(chip.v_registers[0x1], 0xA)
        self.assertEqual(chip.v_registers[0xF], 0x1)

    def test_op8XY5(self):
        """Sets VX -= VY"""
        chip = Chip8()

        # Test no carry
        chip.v_registers[0x1] = 0xFF
        chip.v_registers[0x2] = 0x0F
        op8XY5(chip, 0x8125)
        self.assertEqual(chip.v_registers[0x1], 0xF0)
        self.assertEqual(chip.v_registers[0xF], 1)

        # Test carry
        chip.v_registers[0xA] = 0xE
        chip.v_registers[0xB] = 0xF
        op8XY5(chip, 0x8AB5)
        self.assertEqual(chip.v_registers[0xA], 0xFF)
        self.assertEqual(chip.v_registers[0xF], 0)

    def test_op8XY6(self):
        """Stores LSB of VX in VF then shifts VX to the right by 1"""
        chip = Chip8()
        chip.v_registers[0x5] = 0b10101011

        self.assertEqual(chip.v_registers[0xF], 0)

        op8XY6(chip, 0x8506)

        self.assertEqual(chip.v_registers[0xF], 1)
        self.assertEqual(chip.v_registers[0x5], 0b1010101)

    def test_op8XY7(self):
        chip = Chip8()

        # Test no carry
        chip.v_registers[0x1] = 0x5
        chip.v_registers[0x2] = 0x6

        self.assertEqual(chip.v_registers[0xF], 0x0)

        op8XY7(chip, 0x8127)

        self.assertEqual(chip.v_registers[0x1], 0x1)
        self.assertEqual(chip.v_registers[0xF], 0x1)

        # Test carry
        chip.v_registers[0x3] = 0xA
        chip.v_registers[0x4] = 0x2

        op8XY7(chip, 0x8347)

        self.assertEqual(chip.v_registers[0x3], 0xF8)
        self.assertEqual(chip.v_registers[0xF], 0x0)

    def test_op8XYE(self):
        """Stores MSB of VX in VF then shifts VX to the left by 1"""
        chip = Chip8()
        chip.v_registers[0xC] = 0b10101010

        self.assertEqual(chip.v_registers[0xF], 0)

        op8XYE(chip, 0x8CAE)

        self.assertEqual(chip.v_registers[0xC], 0b1010100)
        self.assertEqual(chip.v_registers[0xF], 0x1)

    def test_op9XY0(self):
        chip = Chip8()
        chip.pc = 0x400

        # Test equal registers
        chip.v_registers[0x1] = 0xFF
        chip.v_registers[0x2] = 0xFF

        op9XY0(chip, 0x9120)
        self.assertEqual(chip.pc, 0x400)

        # Test unequal registers
        chip.v_registers[0xA] = 0xFF
        chip.v_registers[0xB] = 0X11

        op9XY0(chip, 0x9AB0)
        self.assertEqual(chip.pc, 0x402)

    def test_opANNN(self):
        """"Sets address = NNN"""
        chip = Chip8()
        self.assertEqual(chip.address, 0x0)
        opANNN(chip, 0xA5FF)
        self.assertEqual(chip.address, 0x5FF)

    def test_opBNNN(self):
        """Jumps to instruction V0 + NNN"""
        chip = Chip8()
        chip.v_registers[0] = 0x3FE
        self.assertEqual(chip.pc, 0x200)

        opBNNN(chip, 0xB200)

        self.assertEqual(chip.pc, 0x5FE)

    def test_opCXNN(self):
        """Tested manually"""
        True

    def test_opDXYN(self):
        chip = Chip8()
        chip.memory[0x200:0x500] = [0xFF] * 0x300
        chip.address = 0x200

        chip.v_registers[0xA] = 28
        chip.v_registers[0xB] = 10
        self.assertEqual(chip.v_registers[0xF], 0x0)
        # chip.printscreen()
        # chip.gfx = [1]*2048
        chip.printscreen()
        opDXYN(chip, 0xDABA)

        self.assertEqual(chip.v_registers[0xF], 0x0)
        chip.printscreen()

    def test_opEX9E(self):
        True

    def test_opEXA1(self):
        True

    def test_opFX07(self):
        """Sets VX to the value of the delay timer"""
        chip = Chip8()
        chip.delay_timer = 0x300

        self.assertEqual(chip.v_registers[0xE], 0)
        opFX07(chip, 0xFE07)
        self.assertEqual(chip.v_registers[0xE], 0x300)

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
