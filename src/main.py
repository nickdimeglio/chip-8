from cpu import Chip8CPU
from graphics import Chip8Graphics
import sys, time

class Interpreter:
    def __init__(self, rom):
        self.chip = Chip8CPU()
        self.chip.load_game(rom)

    def loop(self):
        self.chip.emulate_cycle()
        self.chip.sound_timer.beep()

        if self.chip.draw_flag:
           self.gfx.display() 
                
        self.window.after(1 / 60 * 1000, loop) 

    def run(self):
        graphics = Chip8Graphics()
        self.window = graphics.setup_graphics(self.chip.screen)
        graphics.setup_input(self.chip.keyboard)

        self.loop()
        self.window.mainloop()


if __name__ == '__main__':  
    interpreter = Interpreter(sys.argv[1])
    interpreter.run()

