import pygame
pygame.mixer.init()

class Cursor():
    def __init__(self):
        self.window = pygame.display.get_surface()

        pygame.mouse.set_visible(False)
        self.mouse_pos = pygame.mouse.get_pos()
        self.cursor_default = pygame.image.load("assets/cursor/cursor.png").convert_alpha()
        self.cursor_hover = pygame.image.load("assets/cursor/pointer.png").convert_alpha()
        self.cursor_image = self.cursor_default

        self.click_sound = pygame.mixer.Sound("assets/audios/click.mp3")
        self.click_sound.set_volume(1.0)

    def click(self):
        self.click_sound.play()

    def change_cursor(self, state):
        if state == "hover":
            self.cursor_image = self.cursor_hover
        elif state == "default":
            self.cursor_image = self.cursor_default

    def get_mouse_pos(self):
        self.mouse_pos = pygame.mouse.get_pos()

    def update(self):
        self.get_mouse_pos()
        self.draw()

    def draw(self):
        self.window.blit(self.cursor_image, self.mouse_pos)