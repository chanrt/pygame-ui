import pygame as pg

class Toggle:
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
        self.border_width = 5

        # colors
        self.off_color = pg.Color("gray")
        self.on_color = pg.Color("blue")
        self.square_color = pg.Color("white")

        self.make_rects()

    def check_clicked(self, mouse_pos):
        if self.display:
            if self.inside_rect(mouse_pos):
                self.state = not self.state
                self.make_rects()

    def inside_rect(self, pos):
        mouse_x, mouse_y = pos
        if mouse_x > self.x - self.size and mouse_x < self.x + self.size and mouse_y > self.y - self.size // 2 and mouse_y < self.y + self.size // 2:
            return True
        else:
            return False

    def make_rects(self):
        if self.state == False:
            self.square_rect = pg.Rect(self.x - self.size, self.y - self.size // 2, self.size, self.size)
            self.color = self.off_color
        else:
            self.square_rect = pg.Rect(self.x, self.y - self.size // 2, self.size, self.size)
            self.color = self.on_color
        self.bg_rect = pg.Rect(self.x - self.size, self.y - self.size // 2, 2 * self.size, self.size)

    def render(self):
        if self.display:
            pg.draw.rect(self.screen, self.color, self.bg_rect)
            pg.draw.rect(self.screen, self.square_color, self.square_rect)
            pg.draw.rect(self.screen, self.color, self.bg_rect, self.border_width)