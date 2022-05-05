from text import Text
import pygame as pg


class InputField:
    def __init__(self, x, y, length, thickness, screen):
        self.x = x
        self.y = y
        self.length = length
        self.thickness = thickness
        self.screen = screen

        self.display = True

        self.selected = True

        self.border_width = 5

        self.bg_color = pg.Color("white")
        self.selected_color = pg.Color("blue")

        self.text = "Testing"
        self.text_object = Text(self.x, self.y - self.thickness // 3, self.text, self.screen)
        self.text_object.set_text_color(pg.Color("black"))

        self.make_rects()

    def add_text(self, text):
        self.text += text
        self.text_object.set_text(self.text)

    def backspace_text(self):
        if len(self.text) > 0:
            self.text = self.text[:-1]
            self.text_object.set_text(self.text)

    def delete_text(self):
        self.text = ""
        self.text_object.set_text(self.text)

    def inside_rect(self, pos):
        mouse_x, mouse_y = pos
        if (self.x - self.length // 2 < mouse_x < self.x + self.length // 2) and (self.y - self.thickness // 2 < mouse_y < self.y + self.thickness // 2):
            return True
        else:
            return False

    def check_clicked(self, pos):
        if self.inside_rect(pos):
            self.selected = not self.selected
        else:
            self.selected = False
        
    def make_rects(self):
        self.bg_rect = pg.Rect(self.x - self.length // 2, self.y - self.thickness // 2, self.length, self.thickness)
        self.selected_rect = pg.Rect(self.x - self.length // 2, self.y - self.thickness // 2, self.length, self.thickness)

    def render(self):
        if self.display:
            pg.draw.rect(self.screen, self.bg_color, self.bg_rect)
            self.text_object.render()
            if self.selected:
                pg.draw.rect(self.screen, self.selected_color, self.selected_rect, self.border_width)