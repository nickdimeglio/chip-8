import random, time, pygame
"""Functions for decoding and executing opcode"""

# Code for decoding instructions into opcodes

def decode(instruction):
    """Given an instruction, return the function for executing its
    corresponding opcode"""

    H = (instruction & 0xF000) >> 12  # High Nibble
    L = instruction & 0x000F   # Low  Nibble

    if instruction == 0x00E0:
        return op00E0
    elif instruction == 0x00EE:
        return op00EE
    elif H == 0x1:
        return op1NNN
    elif H == 0x2:
        return op2NNN
    elif H == 0x3:
        return op3XNN
    elif H == 0x4:
        return op4XNN
    elif H == 0x5:
        return op5XY0
    elif H == 0x6:
        return op6XNN
    elif H == 0x7:
        return op7XNN
    elif H == 0x8:
        if L == 0x0:
            return op8XY0
        elif L == 0x1:
            return op8XY1
        elif L == 0x2:
            return op8XY2
        elif L == 0x3:
            return op8XY3
        elif L == 0x4:
            return op8XY4
        elif L == 0x5:
            return op8XY5
        elif L == 0x6:
            return op8XY6
        elif L == 0x7:
            return op8XY7
        elif L == 0xE:
            return op8XYE
    elif H == 0x9:
        return op9XY0
    elif H == 0xA:
        return opANNN
    elif H == 0xB:
        return opBNNN
    elif H == 0xC:
        return opCXNN
    elif H == 0xD:
        return opDXYN
    elif H == 0xE:
        if L == 0xE:
            return opEX9E
        elif L == 0x1:
            return opEXA1
    elif H == 0xF:
        if L == 0x3:
            return opFX33
        elif L == 0x5:
            D3 = (instruction & 0x00F0) >> 4
            if D3 == 0x1:
                return opFX15
            elif D3 == 0x5:
                return opFX55
            elif D3 == 0x6:
                return opFX65
        elif L == 0x7:
            return opFX07
        elif L == 0x8:
            return opFX18
        elif L == 0x9:
            return opFX29
        elif L == 0xA:
            return opFX0A
        elif L == 0xE:
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
    """Take the N-bytes of memory starting at the current index and XOR
    them onto the screen as N 1-Byte rows, starting at (VX, VY).
    If any pixels are erased, set VF = 1, otherwise set VF = 0."""

    VX = chip8.v_registers[nibble2(instruction)]
    VY = chip8.v_registers[nibble3(instruction)]
    N = nibble4(instruction)
    i = chip8.address

    """TEsting"""
    print("DRAWING!" + "VX: " + str(VX) + ", VY: " + str(VY) + ", N: " + str(N) + ", i: " + str(i))
    """Testing"""

    # Starting at i, store N bytes from memory as a binary string
    sprite = 0b0
    for byte in chip8.memory[i:i+N]:
        sprite <<= 8
        sprite |= byte

    # get relevant screen addresses, row by row
    draw_area = []
    draw_start = VX + (VY * 64)

    for row in range(N):
        start = draw_start + (row * 64)
        end = start + 8

        for address in range(start, end):
            draw_area.append(address)

    # store current state of relevant screen bits in binary
    canvas = 0b0

    for address in draw_area:
        canvas <<= 1
        canvas |= chip8.screen[address]

    # XOR the sprite across the current state of the drawing area
    drawing = canvas ^ sprite

    # Set VF to 0. Update the screen to reflect the new value, and
    # flip VF to 1 if a pixel is turned off.
    chip8.v_registers[0xF] = 0

    for address in reversed(draw_area):
        if chip8.screen[address] == 1 and (drawing & 0b1) == 0:
            chip8.v_registers[0xF] = 1
        chip8.screen[address] = drawing & 0b1
        drawing >>= 1


def opEX9E(chip8, instruction):
    VX = chip8.v_registers[nibble2(instruction)]
    if chip8.keyboard.keys[VX] == 1:
        chip8.pc += 2


def opEXA1(chip8, instruction):
    VX = chip8.v_registers[nibble2(instruction)]
    if chip8.keyboard.keys[VX] == 0:
        chip8.pc += 2


def opFX07(chip8, instruction):
    """Sets VX to the value of the delay timer"""
    X = nibble2(instruction)
    chip8.v_registers[X] = chip8.delay_timer


def opFX0A(chip8, instruction):
    """Pause program until a key is pressed"""
    key_pressed = False
    while not key_pressed:
        for key in chip8.keyboard.keys:
            if key:
                key_pressed = True

def opFX15(chip8, instruction):
    """Set delay timer to VX"""
    VX = chip8.v_registers[nibble2(instruction)]
    chip8.delay_timer = VX


def opFX18(chip8, instruction):
    """Set sound timer to VX"""
    VX = chip8.v_registers[nibble2(instruction)]
    chip8.sound_timer = VX


def opFX1E(chip8, instruction):
    """Set address to address + VX"""
    VX = chip8.v_registers[nibble2(instruction)]
    chip8.address += VX


def opFX29(chip8, instruction):
    """Set address to the location of sprite for digit VX"""
    VX = chip8.v_registers[nibble2(instruction)]
    chip8.address = VX * 5


def opFX33(chip8, instruction):
    """Take decimal value of VX, store hundreds in memory[I], tens in I+1,
       ones in I+2"""
    VX = chip8.v_registers[nibble2(instruction)]
    value = str(VX)
    address = chip8.address
    if len(value) == 3:
        chip8.memory[address] = int(value[0])
        chip8.memory[address + 1] = int(value[1])
        chip8.memory[address + 2] = int(value[2])
    elif len(value) == 2:
        chip8.memory[address] = 0
        chip8.memory[address + 1] = value[0]
        chip8.memory[address + 2] = value[1]
    elif len(value) == 1:
        chip8.memory[address] = 0
        chip8.memory[address + 1] = 0
        chip8.memory[address + 2] = value[0]


def opFX55(chip8, instruction):
    """Store registers V0 through Vx in memory starting at current
       memory address"""
    X = nibble2(instruction)
    I = chip8.address
    chip8.memory[I:(I+X+1)] = chip8.v_registers[:(X+1)]


def opFX65(chip8, instruction):
    """Fill registers V0 to Vx inclusive with the values stored in memory
       starting at current memory address"""
    X = nibble2(instruction)
    I = chip8.address
    chip8.v_registers[0:(X+1)] = chip8.memory[I:(I+X+1)]

