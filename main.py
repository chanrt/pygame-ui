from button import Button
from checkbox import CheckBox
from paragraph import Paragraph
from progress_bar import ProgressBar
from text import Text
from toggle import Toggle

import pygame as pg


def loop():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_color = pg.Color(32, 32, 32)
    running = True

    button = Button(100, 40, 200, 50, screen, "This is a button")
    text = Text(400, 100, "An eye for an eye makes the whole world blind",
                screen)
    paragraph = Paragraph(
        400, 400, "Twinkle Twinkle Little Star\n\
How I wonder what you are!\n\
Up above the world so high\n\
Like a diamond in the sky!", 500, screen)
    checkbox = CheckBox(200, 400, 50, screen)
    progress_bar = ProgressBar(200, 200, 200, 50, screen)
    toggle = Toggle(400, 40, 50, screen)

    progress_bar.set_vertical()

    while running:
        clock.tick(60)
        screen.fill(bg_color)

        button.update(pg.mouse.get_pos())

        button.render()
        text.render()
        progress_bar.render()
        toggle.render()
        paragraph.render()
        checkbox.render()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()

                button.check_clicked(mouse_pos, event.button)
                toggle.check_clicked(mouse_pos)
                checkbox.check_clicked(mouse_pos)

                if button.left_clicked:
                    progress_bar.increase_progress(0.1)
                if button.right_clicked:
                    progress_bar.increase_progress(-0.1)

                if toggle.state == False:
                    progress_bar.set_vertical()
                else:
                    progress_bar.set_horizontal()

            if event.type == pg.MOUSEBUTTONUP:
                button.check_released(pg.mouse.get_pos(), event.button)

        pg.display.flip()

    pg.quit()


if __name__ == '__main__':
    loop()