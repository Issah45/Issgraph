import pygame, math

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

class Img():
    def scale(i, w, h):
        return pygame.transform.scale(i, (w, h))
    def img(i):
        return pygame.image.load(i)

class Mouse():
    def get_pos():
        return pygame.mouse.get_pos()
    def get_pressed():
        return pygame.mouse.get_pressed()

class Utils():
    def init():
        pygame.init()
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
    def keys(i):
        n = pygame.key.get_pressed()
        return n[i]
    def collide(x1, y1, x2, y2, s):
        if abs(x1 - x2) < s:
            if abs(y1 - y2) < s:
                return True
            else:
                return False
    def font(s, siz):
        return pygame.font.Font(s, siz)