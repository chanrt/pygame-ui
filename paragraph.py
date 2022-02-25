import pygame as pg


class Paragraph:
    def __init__(self, x, y, text, max_width, screen):
        self.x = x
        self.y = y
        self.max_width = max_width
        self.screen = screen

        # display state
        self.display = True

        # text
        self._text = text
        self._text_color = pg.Color("white")
        self._font = pg.font.SysFont("arial", 20)

    def render(self):
        if self.display:
            words = [word.split(' ') for word in self._text.splitlines()]
            space = self._font.size(' ')[0] 

            x, y = self.x, self.y
            for line in words:
                for word in line:
                    word_surface = self._font.render(word, 0, self._text_color)
                    word_width, word_height = word_surface.get_size()
                    if x + word_width >= self.x + self.max_width:
                        x = self.x
                        y += word_height
                    self.screen.blit(word_surface, (x, y))
                    x += word_width + space
                x = self.x
                y += word_height