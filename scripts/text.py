import pygame


class Text:
    def __init__(self, font, size, text, color, pos):
        self.window = pygame.display.get_surface()

        self.color = color
        self.font = pygame.font.Font(font, size)
        self.message = text
        self.position = pos

        self.text_surface = self.font.render(self.message, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=pos)

    def draw(self):
        self.window.blit(self.text_surface, self.position)

    def draw_center(self):
        self.window.blit(self.text_surface, self.text_rect)

    def set_text(self, new_text):
        self.message = new_text
        self.text_surface = self.font.render(self.message, True, self.color)

    def update_text(self, text, color):
        self.message = text
        self.color = color
        self.text_surface = self.font.render(self.message, True, self.color)
