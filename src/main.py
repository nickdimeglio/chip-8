from cpu import Chip8CPU
from graphics import Chip8Graphics
import sys, time

class Interpreter:
    def __init__(self, rom):
        self.chip = Chip8CPU()
        self.chip.load_game(rom)

    def loop(self):
        # self.chip.emulate_cycle()
        print(self.chip.keyboard)
        if self.chip.draw_flag:
           self.gfx.display() 
                
        self.window.after(16, self.loop)

    def run(self):
        graphics = Chip8Graphics()
        self.window = graphics.setup_graphics(self.chip.screen)
        graphics.setup_input(self.chip)

        self.loop()
        self.window.mainloop()


if __name__ == '__main__':  
    interpreter = Interpreter(sys.argv[1])
    interpreter.run()

