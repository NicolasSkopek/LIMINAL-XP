import datetime

import pygame

from scripts.cursor import Cursor
from scripts.obj import Obj, StartButton, File
from scripts.scene import Scene
from scripts.text import Text
from scripts.window import Window


class Windows(Scene):

    def __init__(self):
        super().__init__()

        self.window = pygame.display.get_surface()


        self.bg = Obj("assets/bg/background.png", [0, 0], self.all_sprites)
        self.taskbar = Obj("assets/bg/taskbar.png", [0, 660], self.all_sprites)
        self.windows_button = StartButton("assets/bg/windowsbutton.png",[0, 660],self.all_sprites,hover_path="assets/bg/windowsbuttonselected.png")
        self.clock = Text("assets/font/tahoma.ttf", 15, "clock", (255,255,255), (1210, 665))

        self.open_windows = []
        self.desktop_files = [File("LIMINAL", "root", (20, 20))]

        self.cursor = Cursor()

    def events(self, event):
        self.cursor.handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.cursor.click()
            mouse_pos = pygame.mouse.get_pos()

            for win in reversed(self.open_windows):
                clicked = win.handle_click(mouse_pos)

                if clicked == "close":
                    self.open_windows.remove(win)
                    break

                if isinstance(clicked, File):
                    new_window = Window(clicked.title_text, (win.rect.x + 30, win.rect.y + 30),
                                        clicked.content_id)
                    self.open_windows.append(new_window)
                    break

            for f in self.desktop_files:
                if f.was_clicked(mouse_pos):
                    self.open_windows.append(Window(f.title_text, (200, 200), f.content_id))

    def update(self):
        self.all_sprites.update()

    def update_clock(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        self.clock.set_text(current_time)

    def check_mouse_collide(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.windows_button.rect.collidepoint(mouse_pos):
            self.cursor.change_cursor("hover")
            return

        for win in self.open_windows:
            if win.get_close_button_rect().collidepoint(mouse_pos):
                self.cursor.change_cursor("hover")
                return

        for f in self.desktop_files:
            if f.was_clicked(mouse_pos):
                self.cursor.change_cursor("hover")
                return

        self.cursor.change_cursor("default")

    def update(self):
        self.all_sprites.update()

        for file in self.desktop_files:
            file.draw(self.window)

        for win in self.open_windows:
            win.update(self.window)

        self.check_mouse_collide()
        self.cursor.update()
        self.clock.draw()
        self.update_clock()







