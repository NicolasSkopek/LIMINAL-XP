import pygame

from scripts.obj import File


class Window:
    def __init__(self, title, pos, content_id):
        self.rect = pygame.Rect(pos[0], pos[1], 350, 200)
        self.title = title
        self.content_id = content_id
        self.files = []

        self.title_bar_img = pygame.image.load("assets/bg/blue.png").convert_alpha()
        self.title_bar_height = self.title_bar_img.get_height()

        self.close_button = pygame.image.load("assets/bg/close.png").convert_alpha()
        self.close_button = pygame.transform.scale(self.close_button, (20,20))

        self.font = pygame.font.Font("assets/font/tahoma.ttf", 14)

        self.load_content()

    def load_content(self):
        file_map = {
            "root": [("Level 0", "0"), ("Level 4", "4")],
        }

        content = file_map.get(self.content_id, [])
        for i, (name, cid) in enumerate(content):
            pos = (self.rect.x + 10 + (i * 60), self.rect.y + 40)
            self.files.append(File(name, cid, pos))

    def update(self, surface):
        pygame.draw.rect(surface, (240, 240, 240), self.rect)

        surface.blit(self.title_bar_img, (self.rect.x, self.rect.y))
        surface.blit(self.close_button, (self.rect.right - 20, self.rect.y))

        text_surface = self.font.render(self.title, True, (255, 255, 255))
        surface.blit(text_surface, (self.rect.x + 10, self.rect.y + 4))

        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)

        for f in self.files:
            f.draw(surface)

    def get_close_button_rect(self):
        return pygame.Rect(self.rect.right - 25, self.rect.y - 2, 28, 24)

    def handle_click(self, mouse_pos):
        if self.get_close_button_rect().collidepoint(mouse_pos):
            return "close"

        for f in self.files:
            if f.was_clicked(mouse_pos):
                return f
        return None