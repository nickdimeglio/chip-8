"""Functions for decoding and executing opcode"""


def op_0x0fff(chip8):
    chip8.index = chip8.opcode & 0x0FFF
    print("0X0FFF called!")


"""TODO: """
opcodes = {0x0FFF: op_0x0fff}
