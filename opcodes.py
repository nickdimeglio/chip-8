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


def op00E0(chip8, instruction):
    return 0


def op00EE(chip8, instruction):
    """Returns from a subroutine"""
    # Move stack pointer down 1 before accessing a stack value
    chip8.sp -= 1
    chip8.pc = chip8.stack[chip8.sp]
    chip8.stack[chip8.sp] = 0


def op1NNN(chip8, instruction):
    """Jump to address NNN"""
    # May need to change this to jump to NNN - 0x2 bc pc += 2 after
    chip8.pc = instruction & 0x0FFF


def op2NNN(chip8, instruction):
    """Calls subroutine at NNN"""
    chip8.stack[chip8.sp] = chip8.pc
    chip8.sp += 1
    chip8.pc = instruction & 0x0FFF


def op3XNN(chip8, instruction):
    """Skips the next instruction if VX == NN"""
    VX = chip8.v_registers[(instruction & 0x0F00) >> 8]
    NN = instruction & 0x00FF
    if VX == NN:
        chip8.pc += 2


def op4XNN(chip8, instruction):
    """Skips the next instruction if VX != NN"""
    VX = chip8.v_registers[(instruction & 0x0F00) >> 8]
    NN = instruction & 0x00FF
    if VX != NN:
        chip8.pc += 2


def op5XY0(chip8, instruction):
    """Skips the next instruction if VX == VY"""
    VX = chip8.v_registers[(instruction & 0x0F00) >> 8]
    VY = chip8.v_registers[(instruction & 0X00F0) >> 4]
    if VX == VY:
        chip8.pc +=2


def op6XNN(chip8, instruction):
    """Sets VX = NN"""
    X = (instruction & 0x0F00) >> 8
    NN = instruction & 0x00FF
    chip8.v_registers[X] = NN


def op7XNN(chip8, instruction):
    """Adds NN to VX"""
    X = (instruction & 0x0F00) >> 8
    NN = instruction & 0x00FF
    chip8.v_registers[X] += NN


def op8XY0(chip8, instruction):
    return 0


def op8XY1(chip8, instruction):
    return 0


def op8XY2(chip8, instruction):
    return 0


def op8XY3(chip8, instruction):
    return 0


def op8XY4(chip8, instruction):
    return 0


def op8XY5(chip8, instruction):
    return 0


def op8XY6(chip8, instruction):
    return 0


def op8XY7(chip8, instruction):
    return 0


def op8XYE(chip8, instruction):
    return 0


def op9XY0(chip8, instruction):
    return 0


def opANNN(chip8, instruction):
    return 0


def opBNNN(chip8, instruction):
    return 0


def opCXNN(chip8, instruction):
    return 0


def opDXYN(chip8, instruction):
    return 0


def opEX9E(chip8, instruction):
    return 0


def opEXA1(chip8, instruction):
    return 0


def opFX07(chip8, instruction):
    return 0


def opFX0A(chip8, instruction):
    return 0


def opFX15(chip8, instruction):
    return 0


def opFX18(chip8, instruction):
    return 0


def opFX1E(chip8, instruction):
    return 0


def opFX29(chip8, instruction):
    return 0


def opFX33(chip8, instruction):
    return 0


def opFX55(chip8, instruction):
    return 0


def opFX65(chip, instruction):
    return 0
