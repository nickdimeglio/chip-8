from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import floor

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 640
PIXEL_WIDTH = SCREEN_WIDTH / 64
PIXEL_HEIGHT = SCREEN_HEIGHT / 32

home_screen = [0] * 2048
for index, pixel in enumerate(home_screen):
    row = floor(index/64)
    column = index%64
    if 4 <= row <= 27 and 8 <= column <= 55:
        if row in [4, 5, 6, 7, 24, 25, 26, 27]:
            home_screen[index] = 1
        elif column in [8, 9, 10, 11, 30, 31, 32, 33, 52, 53, 54, 55]:
            home_screen[index] = 1


def setup_graphics():
    window = Tk()
    window.title("ESPRESSO")
    window.geometry(str(int(SCREEN_WIDTH)) + "x" + str(int(SCREEN_HEIGHT)))

    canvas = Canvas(window)
    canvas.configure(bg='blanched almond')
    canvas.pack(fill="both", expand=True)

    for index, pixel in enumerate(home_screen):
        if pixel == 1:
            column = index%64
            row = floor(index/64)

            canvas.create_rectangle(
            PIXEL_WIDTH*column, PIXEL_HEIGHT*row, PIXEL_WIDTH*(column+1),
            PIXEL_HEIGHT*(row+1),fill="dark slate grey", outline='black', width=0)

    return window, canvas

def draw_graphics(pixels, canvas):
    for index, pixel in enumerate(pixels):
        if pixel == 1:
            column = index%64
            row = floor(index/64)

            canvas.create_rectangle(
            PIXEL_WIDTH*column, PIXEL_HEIGHT*row, PIXEL_WIDTH*(column+1),
            PIXEL_HEIGHT*(row+1),fill="dark slate grey", outline='black', width=0)


def setup_input():
    return 0




"""Font Set"""
font_set = [
# 0 (Starts at address 0)
0xF0, 0x90, 0x90, 0x90, 0xF0,
# 1 (Starts at 5)
0x20, 0x60, 0x20, 0x20, 0x70,
# 2 (10)
0xF0, 0x10, 0xF0, 0x80, 0xF0,
# 3 (15)
0xF0, 0x10, 0xF0, 0x10, 0xF0,
# 4 (20)
0x90, 0x90, 0xF0, 0x10, 0x10,
# 5 (25)
0xF0, 0x80, 0xF0, 0x10, 0xF0,
# 6 (30)
0xF0, 0x80, 0xF0, 0x90, 0xF0,
# 7 (35)
0xF0, 0x10, 0x20, 0x40, 0x40,
# 8 (40)
0xF0, 0x90, 0xF0, 0x90, 0xF0,
# 9 (45)
0xF0, 0x90, 0xF0, 0x10, 0xF0,
# A (50)
0xF0, 0x90, 0xF0, 0x90, 0x90,
# B (55)
0xE0, 0x90, 0xE0, 0x90, 0xE0,
# C (60)
0xF0, 0x80, 0x80, 0x80, 0xF0,
# D (65)
0xE0, 0x90, 0x90, 0x90, 0xE0,
# E (70)
0xF0, 0x80, 0xF0, 0x80, 0xF0,
# F (75)
0xF0, 0x80, 0xF0, 0x80, 0x80,
]
