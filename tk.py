from tkinter import *
from tkinter import ttk
import math

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 640
PIXEL_WIDTH = SCREEN_WIDTH / 64
PIXEL_HEIGHT = SCREEN_HEIGHT / 32

gfx = [0] * (64 * 32)
for index, p in enumerate(gfx):
    if (math.floor(index/64)) % 2 == 0:
        gfx[index] = 1

window = Tk()
window.title("ESPRESSO")
window.geometry(str(int(SCREEN_WIDTH)) + "x" + str(int(SCREEN_HEIGHT)))

canvas = Canvas(window)
canvas.configure(bg='blanched almond')
canvas.pack(fill="both", expand=True)

def create_screen():
    window =

def draw_screen(pixels, canvas):
    canvas.delete("all")
    for index, pixel in enumerate(pixels):
        if pixel == 1:
            column = index%64
            row = math.floor(index/64)

            canvas.create_rectangle(
            PIXEL_WIDTH*column, PIXEL_HEIGHT*row, PIXEL_WIDTH*(column+1),
            PIXEL_HEIGHT*(row+1),fill="dark slate grey", outline='black', width=0)



draw_screen(gfx, canvas)
window.mainloop()
