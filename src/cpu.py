from graphics import font_set
from opcodes import *


class Chip8CPU:
    def __init__(self):
        self.pc = 0x200     # Program counter, starts at 0x200
        self.opcode = 0     # Opcode, reset to 0
        self.address = 0    # Address register, reset to 0
        self.sp = 0         # Stack Pointer, reset to 0

        self.memory = [0] * 4096
        self.memory[0:49] = font_set # Font set is stored in 0x000-0x1FF

        # CPU Registers
        self.v_registers = [0] * 16
        self.draw_flag = 0

        # Screen Representation
        self.screen = [0] * (64 * 32)
        
        # Timer registers
        self.delay_timer = -1
        self.sound_timer = -1

        # Stack for tracking subroutines
        self.stack = [0] * 16

        # Stack Pointer
        self.sp = 0
        self.keyboard = [0] * 16

    def load_game(self, rom):
        """Read the file provided on the command line and store the ROM
        into memory starting at 0x200"""
        f = open(rom, 'rb')
        d = f.read()
        i = 0x200
        for b in d:
            self.memory[i] = b
            i += 1

    def execute(instruction):
        operation = decode(hex(instruction))
        operation(self, instruction)

    def emulate_cycle(self):
        # Fetch
        instruction = self.memory[self.pc] << 8 | self.memory[self.pc + 1]

        # Decode
        opcode = decode(instruction)
        print("\nEmulation Cycle! PC: " + str(self.pc) + ", Opcode: " + opcode.__name__)
        # Execute
        opcode(self, instruction)
        

        # Update Program Counter 
        self.pc += 2

        # Update Timers
        if self.delay_timer > 0:
            chip.delay_timer -= 1
        if self.sound_timer > 0:
            chip.sound_timer -= 1

    # Functions for Testing
    def printscreen(self):
        print("\n")
        row = 0
        print(" " + "-" * 64)
        while row <= 31:
            c_row = self.gfx[(row*64):(row*64+64)]
            p_row = ""
            for b in c_row:
                if b == 1:
                    p_row+="X"
                else:
                    p_row+=" "
            print("|" + p_row + "|")
            row+=1
        print(" " + "-" * 64)
