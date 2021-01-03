from graphics import font_set

"""The Chip8 interpreter"""


class Chip8:
    def __init__(self):
        self.pc = 0x200     # Program counter, starts at 0x200
        self.opcode = 0     # Opcode, reset to 0
        self.address = 0    # Address register, reset to 0
        self.sp = 0         # Stack Pointer, reset to 0
        self.memory = [0] * 4096
        """Memory Map: 0x000-0x1FF - Interpreter (actually contains font set)
                       0x050-0x0A0 - Used for the built in 4x5 pixel font set (0-F)
                       0x200-0xFFF - Program ROM and work RAM"""
        self.memory[0:49] = font_set # Font set is stored in 0x000-0x1FF
        # CPU Registers
        self.v_registers = [0] * 16
        self.draw_flag = 0
        # Index Register


        # Screen Representation
        self.gfx = [0] * (64 * 32)
        # Timer registers
        self.delay_timer = -1
        self.sound_timer = -1

        # Stack for tracking subroutines
        self.stack = [0] * 16
        """Used to remember the current location before a jump is performed.
           Anytime you perform a jump or call a subroutine, store the program counter
           in the stack before proceeding."""
        # Stack Pointer


        self.key = [0] * 16

    def load_game(self, game):
        game += 1
        self.pc = 0

    def execute_instruction(instruction):
        operation = decode(hex(instruction))
        operation(self, instruction)

    def emulate_cycle(self):
        # Fetch Opcode (next two bytes from memory)
        instruction = self.memory[self.pc] << 8 | self.memory[self.pc + 1]
        # Decode Opcode
        opcode = decode(instruction)
        # Execute Opcode
        opcode(instruction)
        # Update Timers
        self.pc += 2

    def set_keys(self):
        self.key = 0




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
