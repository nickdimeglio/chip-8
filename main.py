from chip8 import Chip8
from graphics import setup_graphics, setup_input, draw_graphics

# Set up render system and register input callbacks
screen, canvas = setup_graphics()
screen.mainloop()
setup_input()

# Initialize the Chip8 system and load the game into the memory
chip8 = Chip8()
chip8.load_game("pong")

# Emulation loop
while True:
    """TODO:
        Besides executing opcodes, the Chip 8 also has two timers
        you will need to implement. As mentioned above, both timers
        count down to zero if they have been set to a value larger
        than zero. Since these timers count down at 60 Hz, you might
        want to implement something that slows down your emulation
        cycle (Execute 60 opcodes in one second)"""
    # Emulate one cycle
    chip8.emulate_cycle()

    # If draw flag is set, update the screen
    if chip8.draw_flag:
        draw_graphics(chip8.gfx, canvas)

    # Store key press state (Press and Release)
    chip8.set_keys
