# PySDL2 Testing
import sys
import sdl2
import sdl2.ext

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 640
PIXEL_WIDTH = SCREEN_WIDTH / 64
PIXEL_HEIGHT = SCREEN_HEIGHT / 32

WHITE = sdl2.ext.Color(255, 255, 255)

class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
        def __init__(self, window):
            super(SoftwareRenderer, self).__init__(window)

        def render(self, components):
            sdl2.ext.fill(self.surface, sdl2.ext.Color(0, 0, 0))
            super(SoftwareRenderer, self).render(components)


class Player(sdl2.ext.Entity):
        def __init__(self, world, sprite, posx=0, posy=0):
            self.sprite = sprite
            self.sprite.position = posx, posy


class Platform:
    def __init__(title, width, height, texture_width, texture_height):
        sdl2.ext.init()
        window = sdl2.ext.Window("ESPRESSO", size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        window.show()
        renderer = sdl2.ext.Renderer(window)
        texture = sdl2.ext.Texture(renderer, 
        


def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("ESPRESSO", size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    window.show()

    # get window's surface to draw on
    windowsurface = window.get_surface()

    # world = sdl2.ext.World()
    # spriterenderer = SoftwareRenderer(window)
    # world.add_system(spriterenderer)


    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sp_paddle1 = factory.from_color(WHITE, size=(20, 100))
    sp_paddle2 = factory.from_color(WHITE, size=(20, 100))

    player1 = Player(world, sp_paddle1, 0, 250)
    player2 = Player(world, sp_paddle2, 890, 250)

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDKL_UP:
                    pass
            elif event.type == sdl2.SDL_KEYUP:
                if event.key.keysym.sym in (sdl2.SDLK_UP, sdl2.SDKL_DOWN):
                    pass
            sdl2.SDL_Delay(10)
            world.process()

if __name__ == "__main__":
    sys.exit(run())

def setup_graphics(chip):
    pass

def draw_graphics(pixels, canvas):
    pass


def setup_input():
    pass


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
