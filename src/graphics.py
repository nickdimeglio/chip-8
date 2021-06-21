import pygame, random

class Chip8Graphics:
    """Configures and implements input/output for the CHIP8 emulator"""
    def __init__(self):
        self.width = 1280
        self.height = 640
        self.pixel_width = self.width // 64
        self.pixel_height = self.height // 32
        self.bg_color = (12, 15, 10)
        self.pixel_color = (249, 251, 242) 
        self.colors = [self.bg_color, self.pixel_color]
        self.display_pixels = []

    def init_screen(self, screen, chip8_screen):
        """Initializes the graphical representation of the CHIP8 screen"""
        for index, pixel in enumerate(chip8_screen):
            column = index%64
            row = index//64
            x = self.pixel_width * column
            y = self.pixel_height * row
            display_pixel = pygame.draw.rect(screen, self.colors[0], 
                pygame.Rect(x, y, self.pixel_width, self.pixel_height))

            self.display_pixels.append(display_pixel)

    def draw_screen(self, screen, chip8_screen):
        """Draws the current CHIP8 pixels to the screen"""
        for index, value in enumerate(chip8_screen):
            dp = self.display_pixels[index]
            color = self.colors[value]
            screen.fill(color, dp)            

    def random_screen(self, screen):
        """Draws the pixels on the screen at random"""
        for dp in self.display_pixels:
            color = self.colors[random.randrange(2)]
            screen.fill(color, dp)

font_set = [
0xF0, 0x90, 0x90, 0x90, 0xF0, # 0 (Starts at address 0)
0x20, 0x60, 0x20, 0x20, 0x70, # 1 (Starts at 5)
0xF0, 0x10, 0xF0, 0x80, 0xF0, # 2 (10)
0xF0, 0x10, 0xF0, 0x10, 0xF0, # 3 (15)
0x90, 0x90, 0xF0, 0x10, 0x10, # 4 (20)
0xF0, 0x80, 0xF0, 0x10, 0xF0, # 5 (25)
0xF0, 0x80, 0xF0, 0x90, 0xF0, # 6 (30)
0xF0, 0x10, 0x20, 0x40, 0x40, # 7 (35) 
0xF0, 0x90, 0xF0, 0x90, 0xF0, # 8 (40)
0xF0, 0x90, 0xF0, 0x10, 0xF0, # 9 (45)
0xF0, 0x90, 0xF0, 0x90, 0x90, # A (50)
0xE0, 0x90, 0xE0, 0x90, 0xE0, # B (55)
0xF0, 0x80, 0x80, 0x80, 0xF0, # C (60) 
0xE0, 0x90, 0x90, 0x90, 0xE0, # D (65)
0xF0, 0x80, 0xF0, 0x80, 0xF0, # E (70)
0xF0, 0x80, 0xF0, 0x80, 0x80, # F (75)
]
