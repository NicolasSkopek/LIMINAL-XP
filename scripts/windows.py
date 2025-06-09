import datetime

import pygame

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

        pygame.mouse.set_visible(False)
        self.cursor_image = pygame.image.load("assets/ui/cursor.png").convert_alpha()

    def events(self, event):
        pass

    def update(self):
        self.all_sprites.update()

    def update_clock(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        self.clock.set_text(current_time)

    def update(self):
        self.all_sprites.update()
        self.clock.draw()
        self.update_clock()



