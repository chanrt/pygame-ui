import pygame as pg

class CheckBox:
    def __init__(self, x, y, size, screen):
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen

        # display
        self.display = True

        # state
        self.state = False

        # border
        self.border_width = self.size // 4

        # colors
        self.bg_color = "blue"
        self.checked_color = "yellow"

        self.make_rects()

    def make_rects(self):
        self.bg_rect = pg.Rect(self.x - self.size // 2, self.y - self.size // 2, self.size, self.size)

        if self.state == True:
            offset = -self.size // 2 + self.border_width
            length = self.size - 2 * self.border_width
            self.checked_rect = pg.Rect(self.x + offset, self.y + offset, length, length)

    def inside_rect(self, pos):
        mouse_x, mouse_y = pos
        if (self.x - self.size // 2 < mouse_x < self.x + self.size // 2) and (self.y - self.size // 2 < mouse_y < self.y + self.size // 2):
            return True
        else:
            return False

    def check_clicked(self, pos):
        if self.display:
            if self.inside_rect(pos):
                self.state = not self.state
                self.make_rects()

    def render(self):
        if self.display:
            pg.draw.rect(self.screen, self.bg_color, self.bg_rect)
            if self.state == True:
                pg.draw.rect(self.screen, self.checked_color, self.checked_rect)