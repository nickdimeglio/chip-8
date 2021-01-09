# PySDL2 Testing
import sys
import sdl2
import sdl2.ext

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 640
PIXEL_WIDTH = SCREEN_WIDTH / 64
PIXEL_HEIGHT = SCREEN_HEIGHT / 32

WHITE = sdl2.ext.Color(255, 255, 255)

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("ESPRESSO", size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    window.show()

    # get window's surface to draw on
    windowsurface = window.get_surface()

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            window.refresh()
    return 0

if __name__ == "__main__":
    sys.exit(run())
