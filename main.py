from button import Button
import pygame as pg

def loop():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_color = pg.Color(32, 32, 32)
    running = True

    button = Button(100, 10, 200, 50, screen, "This is a button")

    while running:
        clock.tick(60)
        screen.fill(bg_color)

        button.update(pg.mouse.get_pos())
        button.render()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                button.check_clicked(pg.mouse.get_pos(), event.button)
                if button.left_clicked:
                    print("Left clicked!")
                if button.right_clicked:
                    print("Right clicked!")
            if event.type == pg.MOUSEBUTTONUP:
                button.check_released(pg.mouse.get_pos(), event.button)

        pg.display.flip()

    pg.quit()

if __name__ == '__main__':
    loop()