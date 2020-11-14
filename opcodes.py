"""Functions for decoding and executing opcode"""





def decode(instruction):
    """Given an instruction, return the function for executing its
    corresponding opcode"""

    d1 = instruction[0]
    d2 = instruction[1]
    d3 = instruction[2]
    d4 = instruction[3]

    if d1 == '0': # 00E0 or 00EE
        return opcodes[instruction]
    if d1 in ['1', '2']: # 1NNN or 2NNN
        return opcodes[d1 + "NNN"]
    if d1 in ['3', '4', '6', '7']: # 3XNN, 4XNN, 6XNN, or 7XNN
        return opcodes[d1 + "XNN"]
    if d1 == "5": # 5XY0
        return op5XY0
    if d1 == '8': # 8XY0->8XY7 and 8XYE
        return opcodes['8' + "XY" + d4]
    if d1 == '9':
        return op9XY0
    if d1 in ['A', 'B']: # ANNN or BNNN
        return opcodes[d1 + "NNN"]
    if d1 == 'C': # CXNN
        return opCXNN
    if d1 == 'D': # DXYN
        return opDXYN
    if d1 == 'E': # EX9E or EXA1
        if d4 == 'E':
            return opEX9E
        return opEXA1
    if d1 == 'F': # FX07, FX0A, FX15, FX18, FX1E, FX29, FX33, FX55, FX65
        return opcodes["FX" + d3 + d4]


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


opcodes = {"0NNN": op0NNN, "00E0": op00E0, "00EE": op00EE, "1NNN": op1NNN, "2NNN": op2NNN,
        "3XNNN": op3XNN, "4XNN": op4XNN, "5XYO": op5XY0, "6XNN": op6XNN, "7XNN": op7XNN,
        "8XY0": op8XY0, "8XY1": op8XY1, "8XY2": op8XY2, "8XY3": op8XY3, "8XY4": op8XY4,
        "8XY5": op8XY5, "8XY6": op8XY6, "8XY7": op8XY7, "8XYE": op8XYE, "9XY0": op9XY0,
        "ANNN": opANNN, "BNNN": opBNNN, "CXNN": opCXNN, "DXYN": opDXYN, "EX9E": opEX9E,
        "EXA1": opEXA1, "FX07": opFX07, "FX0A": opFX0A, "FX15": opFX15, "FX18": opFX18,
        "FX1E": opFX1E, "FX29": opFX29, "FX33": opFX33, "FX55": opFX55, "FX65": opFX65}
