from cpu import Chip8CPU
from graphics import Chip8Graphics
import sys, time

class Interpreter:
    def __init__(self, rom):
        self.chip = Chip8CPU()
        self.chip.load_game(rom)

        self.gfx = Chip8Graphics()
        self.screen, self.canvas = self.gfx.setup_io(self.chip)

    def run(self):
        self.screen.mainloop()
        emulator_running = True

        while emulator_running:
            time.sleep(1/60)
            self.chip.handle_keys()
            self.chip.sound_timer.beep()
            self.chip.emulate_cycle()

            if self.chip.draw_flag:
               self.gfx.display() 
                
            # Update timers
            if chip.delay_timer > 0:
                chip.delay_timer -= 1
            if chip.sound_timer > 0:
                chip.sound_timer -= 1

if __name__ == '__main__':  
    interpreter = Interpreter(sys.argv[1])
    interpreter.run()

