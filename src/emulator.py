from cpu import Chip8CPU
from graphics import Chip8Graphics
import pygame, sys, time, random

class Emulator:
    def __init__(self, rom):
        self.chip = Chip8CPU()
        self.graphics = Chip8Graphics()
        self.chip.load_game(rom)
        
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.graphics.width, self.graphics.height))
        self.graphics.init_screen(self.screen, self.chip.screen)

        while True: 

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    self.chip.keyboard.handle_key(event)

            self.chip.emulate_cycle()
            self.graphics.draw_screen(self.screen, self.chip.screen)

            pygame.display.update()
            print(self.chip.keyboard.keys)


if __name__ == '__main__':  
    emulator = Emulator(sys.argv[1])
    emulator.run()


