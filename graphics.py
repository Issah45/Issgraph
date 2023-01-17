import pygame

class Graphics():
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.display = pygame.display.set_mode((w, h))
        self.KEYDOWN = pygame.KEYDOWN
        self.KEYUP = pygame.KEYUP
    def shouldClose(self):
        return pygame.QUIT
    def game(self):
        return pygame.event.get()
    def paint(self, r, g, b):
        self.display.fill((r, g, b))
    def update(self):
        pygame.display.update()
    def image(self, img, x, y):
        self.display.blit(img, (x, y))
    def title(self, t):
        pygame.display.set_caption(t)

def img(i):
    return pygame.image.load(i)

KEYS = {
    "right": pygame.K_RIGHT,
    "left": pygame.K_LEFT,
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "z": pygame.K_z,
    "x": pygame.K_x,
    "a": pygame.K_a,
    "b": pygame.K_b,
    "esc": pygame.K_ESCAPE,
    "enter": pygame.K_RETURN,
    "lshift": pygame.K_LSHIFT,
    "rshift": pygame.K_RSHIFT
}

COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}

def k(i):
    n = pygame.key.get_pressed()
    return n[i]