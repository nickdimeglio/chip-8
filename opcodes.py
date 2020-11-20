"""Functions for decoding and executing opcode"""

def decode(instruction):
    """Given an instruction, return the function for executing its
    corresponding opcode"""

    H = (instruction & 0xF000) >> 12  # High Nibble
    L = instruction & 0x000F   # Low  Nibble

    if instruction == 0x00E0:
        return op00E0
    if instruction == 0x00EE:
        return op00EE
    if H == 0x1:
        return op1NNN
    if H == 0x2:
        return op2NNN
    if H == 0x3:
        return op3XNN
    if H == 0x4:
        return op4XNN
    if H == 0x5:
        return op5XY0
    if H == 0x6:
        return op6XNN
    if H == 0x7:
        return op7XNN
    if H == 0x8:
        if L == 0x0:
            return op8XY0
        if L == 0x1:
            return op8XY1
        if L == 0x2:
            return op8XY2
        if L == 0x3:
            return op8XY3
        if L == 0x4:
            return op8XY4
        if L == 0x5:
            return op8XY5
        if L == 0x6:
            return op8XY6
        if L == 0x7:
            return op8XY7
        if L == 0xE:
            return op8XYE
    if H == 0x9:
        return op9XY0
    if H == 0xA:
        return opANNN
    if H == 0xB:
        return opBNNN
    if H == 0xC:
        return opCXNN
    if H == 0xD:
        return opDXYN
    if H == 0xE:
        if L == 0xE:
            return opEX9E
        if L == 0x1:
            return opEXA1
    if H == 0xF:
        if L == 0x3:
            return opFX33
        if L == 0x5:
            D3 = (instruction & 0x00F0) >> 4
            if D3 == 0x1:
                return opFX15
            if D3 == 0x5:
                return opFX55
            if D3 == 0x6:
                return opFX65
        if L == 0x7:
            return opFX07
        if L == 0x8:
            return opFX18
        if L == 0x9:
            return opFX29
        if L == 0xA:
            return opFX0A
        if L == 0xE:
            return opFX1E









def op0NNN(chip8, instruction):
    chip8.address = chip8.opcode & 0x0FFF


def op00E0(chip8, instruction):
    return 0


def op00EE(chip8, instruction):
    return 0


def op1NNN(chip, instruction):
    return 0


def op2NNN(chip, instruction):
    return 0


def op3XNN(chip, instruction):
    return 0


def op4XNN(chip, instruction):
    return 0


def op5XY0(chip, instruction):
    return 0


def op6XNN(chip, instruction):
    return 0


def op7XNN(chip, instruction):
    return 0


def op8XY0(chip, instruction):
    return 0


def op8XY1(chip, instruction):
    return 0


def op8XY2(chip, instruction):
    return 0


def op8XY3(chip, instruction):
    return 0


def op8XY4(chip, instruction):
    return 0


def op8XY5(chip, instruction):
    return 0


def op8XY6(chip, instruction):
    return 0


def op8XY7(chip, instruction):
    return 0


def op8XYE(chip, instruction):
    return 0


def op9XY0(chip, instruction):
    return 0


def opANNN(chip, instruction):
    return 0


def opBNNN(chip, instruction):
    return 0


def opCXNN(chip, instruction):
    return 0


def opDXYN(chip, instruction):
    return 0


def opEX9E(chip, instruction):
    return 0


def opEXA1(chip, instruction):
    return 0


def opFX07(chip, instruction):
    return 0


def opFX0A(chip, instruction):
    return 0


def opFX15(chip, instruction):
    return 0


def opFX18(chip, instruction):
    return 0


def opFX1E(chip, instruction):
    return 0


def opFX29(chip, instruction):
    return 0


def opFX33(chip, instruction):
    return 0


def opFX55(chip, instruction):
    return 0


def opFX65(chip, instruction):
    return 0


# def string_decode(instruction):
#     """Given an instruction, return the function for executing its
#     corresponding opcode"""
#
#     d1 = instruction[2]
#     d2 = instruction[3]
#     d3 = instruction[4]
#     d4 = instruction[5]
#
#     if d1 == '0': # 00E0 or 00EE
#         opcode = d1 + d2 + d3 + d4
#         return opcodes[opcode]
#     if d1 in ['1', '2']: # 1NNN or 2NNN
#         return opcodes[d1 + "NNN"]
#     if d1 in ['3', '4', '6', '7']: # 3XNN, 4XNN, 6XNN, or 7XNN
#         return opcodes[d1 + "XNN"]
#     if d1 == "5": # 5XY0
#         return op5XY0yo
#     if d1 == '8': # 8XY0->8XY7 and 8XYE
#         return opcodes['8' + "XY" + d4]
#     if d1 == '9':
#         return op9XY0
#     if d1 in ['A', 'B']: # ANNN or BNNN
#         return opcodes[d1 + "NNN"]
#     if d1 == 'C': # CXNN
#         return opCXNN
#     if d1 == 'D': # DXYN
#         return opDXYN
#     if d1 == 'E': # EX9E or EXA1
#         if d4 == 'E':
#             return opEX9E
#         return opEXA1
#     if d1 == 'F': # FX07, FX0A, FX15, FX18, FX1E, FX29, FX33, FX55, FX65
#         return opcodes["FX" + d3 + d4]
