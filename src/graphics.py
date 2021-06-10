from tkinter import Tk, Canvas, mainloop

class Chip8Graphics:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 640
        self.pixel_width = self.screen_width / 64
        self.pixel_height = self.screen_height / 32
        self.bg_color 'blanched almond'
        self.pixel_color = 'dark slate grey'
        self.outline_color = 'black'

    def display(self, pixels):
        self.canvas.delete("all")
        for index, pixel in enumerate(pixels):
            if pixel == 1:
                column = index%64
                row = floor(index/64)
                self.canvas.create_rectangle(
                self.pixel_width*column, self.pixel_height*row, self.pixel_width*(column+1),
                self.pixel_height*(row+1),fill=self.bg_color, outline=self.outline_color, width=0)

    def setup_io(self, chip):
        window = Tk()
        window.title("ESPRESSO")
        window.geometry(str(int(self.screen_width)) + "x" + str(int(self.screen_height)))
    
        canvas = Canvas(self.window)
        canvas.configure(bg=self.bg_color)
        canvas.pack(fill="both", expand=True)
    
        for index, pixel in enumerate(chip.gfx):
            column = index%64
            row = index//64
            if 4 <= row <= 27 and 8 <= column <= 55:
                if row in [4, 5, 6, 7, 24, 25, 26, 27] or column in [8, 9, 10, 11, 30, 31, 32, 33, 52, 53, 54, 55]:
                    chip.gfx[index] = 1
    
        self.display(chip.gfx, canvas)


        # Setup Input

        return window, canvas

    def setup_input(self):
        pass

if __name__ == '__main__':
    mainloop()

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
