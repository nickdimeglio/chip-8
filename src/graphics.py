from tkinter import Tk, Canvas, mainloop

class Chip8Graphics:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 640
        self.pixel_width = self.screen_width / 64
        self.pixel_height = self.screen_height / 32
        self.bg_color = 'blanched almond'
        self.pixel_color = 'dark slate grey'
        self.outline_color = 'black'

    def display(self, screen):
        self.canvas.delete("all")
        for index, pixel in enumerate(screen):
            if pixel == 1:
                column = index%64
                row = index//64
                self.canvas.create_rectangle(
                self.pixel_width*column, self.pixel_height*row, self.pixel_width*(column+1),
                self.pixel_height*(row+1),fill=self.bg_color, outline=self.outline_color, width=0)

    def setup_graphics(self, screen):
        self.window = Tk()
        self.window.title("ESPRESSO")
        self.window.geometry(str(int(self.screen_width)) + "x" + str(int(self.screen_height)))
        self.canvas = Canvas(self.window)
        self.canvas.configure(bg=self.bg_color)
        self.canvas.pack(fill="both", expand=True)
    
        for index, pixel in enumerate(screen):
            column = index%64
            row = index//64
            if 4 <= row <= 27 and 8 <= column <= 55:
                if row in [4, 5, 6, 7, 24, 25, 26, 27] or column in [8, 9, 10, 11, 30, 31, 32, 33, 52, 53, 54, 55]:
                    screen[index] = 1
    
        self.display(screen)
        return self.window

    def key_down(self, event, keyboard):
        key = event.keysym.upper()
        if key in key_mapping:
            mapping = key_mapping[key]
            keyboard[mapping] = 1
            
    def key_up(self, event, keyboard):
        key = event.keysym.upper()
        if key in key_mapping:
            mapping = key_mapping[key]
            keyboard[mapping] = 0

    def setup_input(self, keyboard):
        # Setup Input
        self.window.bind_all('<KeyPress>', lambda event: self.key_down(event, keyboard))
        self.window.bind_all('<KeyRelease>', lambda event: self.key_up(event, keyboard))

if __name__ == '__main__':
    mainloop()


"""Key Mapping"""
key_mapping = {
'1': 0x1, '2': 0x2, '3': 0x3, '4': 0xC,
'Q': 0x4, 'W': 0x5, 'E': 0x6, 'R': 0xD,
'A': 0x7, 'S': 0x8, 'D': 0x9, 'F': 0xE,
'Z': 0xA, 'X': 0x0, 'C': 0xB, 'V': 0xF,
}

"""Font Set"""
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
