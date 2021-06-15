from cpu import Chip8CPU
from graphics import Chip8Graphics
import sys, time, random

class Interpreter:
    def __init__(self, rom):
        self.chip = Chip8CPU()
        self.chip.load_game(rom)
        self.graphics = Chip8Graphics(self.chip)

    def loop(self):
        time.sleep(1/60)
        for i in range(len(self.chip.screen)):
            self.chip.screen[i] = random.randint(0, 1)
        self.graphics.display(self.chip.screen)
        self.loop()

    def run(self):
        running = True
        while running:
            self.chip.emulate_cycle()

            # if drawflag
            self.graphics.window.update_idletasks()
            self.graphics.display(self.chip.screen)

            time.sleep(1/60)


if __name__ == '__main__':  
    interpreter = Interpreter(sys.argv[1])
    interpreter.run()

