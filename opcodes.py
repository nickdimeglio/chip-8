import random
"""Functions for decoding and executing opcode"""

# Code for decoding instructions into opcodes

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


# Code for taking parts from an instruction

def nibble1(instruction):
    return (instruction & 0xF000) >> 12


def nibble2(instruction):
    return (instruction & 0x0F00) >> 8


def nibble3(instruction):
    return (instruction & 0x00F0) >> 4


def nibble4(instruction):
    return instruction & 0x000F



# Code for executing opcodes

def op00E0(chip8, instruction):
    """Clear the screen"""
    chip8.gfx = [0] * (64 * 32)


def op00EE(chip8, instruction):
    """Returns from a subroutine"""
    # Move stack pointer down 1 before accessing a stack value
    chip8.sp -= 1
    chip8.pc = chip8.stack[chip8.sp]
    chip8.stack[chip8.sp] = 0


def op1NNN(chip8, instruction):
    """Jumps to address NNN"""
    # May need to change this to jump to NNN - 0x2 bc pc += 2 after
    chip8.pc = instruction & 0x0FFF


def op2NNN(chip8, instruction):
    """Calls subroutine at NNN"""
    chip8.stack[chip8.sp] = chip8.pc
    chip8.sp += 1
    chip8.pc = instruction & 0x0FFF


def op3XNN(chip8, instruction):
    """Skips the next instruction if VX == NN"""
    X = nibble2(instruction)
    VX = chip8.v_registers[X]
    NN = instruction & 0x00FF
    if VX == NN:
        chip8.pc += 2


def op4XNN(chip8, instruction):
    """Skips the next instruction if VX != NN"""
    X = nibble2(instruction)
    VX = chip8.v_registers[X]
    NN = instruction & 0x00FF
    if VX != NN:
        chip8.pc += 2


def op5XY0(chip8, instruction):
    """Skips the next instruction if VX == VY"""
    X = nibble2(instruction)
    Y = nibble3(instruction)
    VX = chip8.v_registers[X]
    VY = chip8.v_registers[Y]
    if VX == VY:
        chip8.pc +=2


def op6XNN(chip8, instruction):
    """Sets VX = NN"""
    X = nibble2(instruction)
    NN = instruction & 0x00FF
    chip8.v_registers[X] = NN


def op7XNN(chip8, instruction):
    """Sets VX += NN"""
    X = nibble2(instruction)
    NN = instruction & 0x00FF
    chip8.v_registers[X] += NN

    # Check for wraps
    chip8.v_registers[X] %= 0x100


def op8XY0(chip8, instruction):
    """Sets VX = VY"""
    X = nibble2(instruction)
    Y = nibble3(instruction)
    chip8.v_registers[X] = chip8.v_registers[Y]


def op8XY1(chip8, instruction):
    """Sets VX = (VX or VY)"""
    X = nibble2(instruction)
    Y = nibble3(instruction)
    chip8.v_registers[X] = chip8.v_registers[X] | chip8.v_registers[Y]


def op8XY2(chip8, instruction):
    """Sets VX = (VX and VY)"""
    X = nibble2(instruction)
    Y = nibble3(instruction)
    chip8.v_registers[X] = chip8.v_registers[X] & chip8.v_registers[Y]


def op8XY3(chip8, instruction):
    """Sets VX = (VX xor VY)"""
    X = nibble2(instruction)
    Y = nibble3(instruction)
    chip8.v_registers[X] = chip8.v_registers[X] ^ chip8.v_registers[Y]


def op8XY4(chip8, instruction):
    """Sets VX += VY, Sets VF = carry"""
    X = nibble2(instruction)
    Y = nibble3(instruction)
    chip8.v_registers[X] += chip8.v_registers[Y]

    # Check for carry
    if chip8.v_registers[X] > 0xFF:
        chip8.v_registers[0xF] = 0x1
        chip8.v_registers[X] %= 0x100


def op8XY5(chip8, instruction):
    """Sets VX -= VY. Sets VF = NOT borrow"""
    X = nibble2(instruction)
    Y = nibble3(instruction)

    # check for borrow
    if chip8.v_registers[X] > chip8.v_registers[Y]:
        chip8.v_registers[0xF] = 1
    else:
        chip8.v_registers[0xF] = 0
        chip8.v_registers[X] += 0x100

    chip8.v_registers[X] -= chip8.v_registers[Y]


def op8XY6(chip8, instruction):
    """Stores LSB of VX in VF then shifts VX to the right by 1"""
    X = nibble2(instruction)
    chip8.v_registers[0xF] = chip8.v_registers[X] & 0x1
    chip8.v_registers[X] = chip8.v_registers[X] >> 1


def op8XY7(chip8, instruction):
    """Sets VX = VY - VX. Sets VF = NOT borrow"""
    X = nibble2(instruction)
    Y = nibble3(instruction)

    # check for borrow
    if chip8.v_registers[Y] > chip8.v_registers[X]:
        chip8.v_registers[0xF] = 1
    else:
        chip8.v_registers[0xF] = 0
        chip8.v_registers[Y] += 0x100

    chip8.v_registers[X] = (chip8.v_registers[Y] - chip8.v_registers[X])


def op8XYE(chip8, instruction):
    """Stores MSB of VX in VF then shifts VX to the left by 1"""
    X = nibble2(instruction)
    chip8.v_registers[0xF] = (chip8.v_registers[X] & 0b10000000) >> 7
    chip8.v_registers[X] = ((chip8.v_registers[X] << 1) & 0xFF)


def op9XY0(chip8, instruction):
    """Skips the next instruction if VX != VY"""
    X = nibble2(instruction)
    Y = nibble3(instruction)

    if chip8.v_registers[X] != chip8.v_registers[Y]:
        chip8.pc +=2


def opANNN(chip8, instruction):
    """Sets address = NNN"""
    chip8.address = (0x0FFF & instruction)


def opBNNN(chip8, instruction):
    """Jumps to instruction V[0] + NNN"""
    V0 = chip8.v_registers[0x0]
    NNN = 0x0FFF & instruction
    chip8.pc = V0 + NNN


def opCXNN(chip8, instruction):
    """Sets VX = NN & a random number"""
    rando = random.randint(0, 255)
    print(rando)
    NN = 0xFF & instruction
    X = nibble2(instruction)
    chip8.v_registers[X] = NN & rando


def opDXYN(chip8, instruction):
    """Draws a sprite at coordinate (VX, VY) that has a width of 8 pixels and
    a height of N+1 pixels. Each row of 8 pixels is read as bit-coded starting
    from memory location I; I value doesn’t change after the execution of this
    instruction. As described above, VF is set to 1 if any screen pixels are
    flipped from set to unset when the sprite is drawn, and to 0 if that
    doesn’t happen"""

    """
    X = nibble2(instruction)
    Y = nibble3(instruction)
    N = nibble4(instruction)

    # get N bytes from memory, starting at i
    bits = chip.memory[i:i+(N*8)]

    """



    # store screen indices in list
    # screen indices at (x, y):(x, y)+8,
    #                   (x, y-1):(x, y-1)+8,
    #                   ...,
    #                   (x, y-n):(x, y-n)+8
    """
    pixel_addresses = []
    start = X + (64*Y)
    for i in range(0, N):
        pixel_addresses[start+i:start+i+8]
        """

    # loop through provided bits and screen inidices, updating each
    # set VF=1 if any bit is changed from 1 to 0

    # Screen is 64 columns, 32 rows
    # Coordinate (60, 0) = gfx[60]
    # Coordinate (5, 10) = gfx[63 * 10 + 5] = gfx[635]

    return 0


def opEX9E(chip8, instruction):
    return 0


def opEXA1(chip8, instruction):
    return 0


def opFX07(chip8, instruction):
    """Sets VX to the value of the delay timer"""
    X = nibble2(instruction)
    chip8.v_registers[X] = chip8.delay_timer


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
