import datetime

import pygame

from scripts.cursor import Cursor
from scripts.obj import Obj, StartButton
from scripts.scene import Scene
from scripts.text import Text


class Windows(Scene):

    def __init__(self):
        super().__init__()

        self.window = pygame.display.get_surface()


        self.bg = Obj("assets/bg/background.png", [0, 0], self.all_sprites)
        self.taskbar = Obj("assets/bg/taskbar.png", [0, 660], self.all_sprites)
        self.windows_button = StartButton("assets/bg/windowsbutton.png",[0, 660],self.all_sprites,hover_path="assets/bg/windowsbuttonselected.png")
        self.clock = Text("assets/font/tahoma.ttf", 15, "clock", (255,255,255), (1210, 665))



        self.cursor = Cursor()


    def events(self, event):
        self.cursor.handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.cursor.click()

    def update(self):
        self.all_sprites.update()

    def update_clock(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        self.clock.set_text(current_time)

    def check_mouse_collide(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.windows_button.rect.collidepoint(mouse_pos):
            self.cursor.change_cursor("hover")
        else:
            self.cursor.change_cursor("default")

    def update(self):
        self.all_sprites.update()
        self.check_mouse_collide()
        self.cursor.update()
        self.clock.draw()
        self.update_clock()





