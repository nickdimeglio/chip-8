from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import floor



"""Font Set"""
font_set = ['F'] * 80

def setup_graphics():
    return 0


def setup_input():
    return 0


def draw_graphics():
    """The graphics system: The chip 8 has one instruction that draws sprite to the screen.
    Drawing is done in XOR mode and if a pixel is turned off as a result of drawing,
    the VF register is set. This is used for collision detection."""
    return 0

# """Provides graphics"""
#
# WIDTH, HEIGHT = 64, 32
# gfx = [0] * (WIDTH * HEIGHT)
#
#
# # Generate bitmap
# bits = '\n#define'
# for p in gfx:
#     bits += (str(p) + ', ')
# bits += '};"""'
#
#
#
#
#
#
# for square in gfx:
#     position = gfx.index((square))
#     row = floor()
#     column = gfx.index(square) % 64
#
# window = Tk()
# screen = Canvas(window, width=WIDTH, height=HEIGHT, bg="#00000F")
# screen.pack(fill="both", expand=True)
#
# mainloop()
