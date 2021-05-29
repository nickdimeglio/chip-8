from chip8 import Chip8CPU
from graphics import setup_graphics, setup_input, draw_graphics
import multiprocessing, time, math


class Interpreter:
    def __init__(self, chip):
        self.screen, self.canvas = setup_graphics(chip)
        setup_input()

    chip = Chip8CPU()
    chip.load_game("pong")

    def emulate(self, chip, screen, canvas):
    # Emulation loop

        home_screen = [0] * 2048
        for index, pixel in enumerate(home_screen):
            row = index // 64
            column = index % 64
            if 4 <= row <= 27 and 8 <= column <= 55:
                if row in [4, 5, 6, 7, 24, 25, 26, 27]:
                    home_screen[index] = 1
                elif column in [8, 9, 10, 11, 30, 31, 32, 33, 52, 53, 54, 55]:
                    home_screen[index] = 1
        draw_graphics(home_screen, canvas)

        emulator_running = True
        while emulator_running:
            """TODO:
                Besides executing opcodes, the Chip 8 also has two timers
                you will need to implement. As mentioned above, both timers
                count down to zero if they have been set to a value larger
                than zero. Since these timers count down at 60 Hz, you might
                want to implement something that slows down your emulation
                cycle (Execute 60 opcodes in one second)"""
            # Emulate one cycle
            chip.emulate_cycle()

            # If draw flag is set, update the screen
            if chip.draw_flag:
                draw_graphics(chip.gfx, canvas)
                screen.update()

            # Store key press state (Press and Release)
            chip8.set_keys


if __name__ == '__main__':
    initialize_emulator()
