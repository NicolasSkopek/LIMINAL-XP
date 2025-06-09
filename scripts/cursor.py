import pygame

class Cursor:
    def __init__(self):
        self.window = pygame.display.get_surface()
        pygame.mouse.set_visible(False)

        self.mouse_pos = pygame.mouse.get_pos()
        self.cursor_default = pygame.image.load("assets/cursor/cursor.png").convert_alpha()
        self.cursor_hover = pygame.image.load("assets/cursor/pointer.png").convert_alpha()
        self.cursor_image = self.cursor_default

        self.click_sound = pygame.mixer.Sound("assets/audios/click.mp3")
        self.click_sound.set_volume(1.0)

        self.selecting = False
        self.select_start = (0, 0)
        self.select_end = (0, 0)

    def click(self):
        self.click_sound.play()

    def change_cursor(self, state):
        if state == "hover":
            self.cursor_image = self.cursor_hover
        elif state == "default":
            self.cursor_image = self.cursor_default

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.selecting = True
            self.select_start = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.selecting = False

    def get_mouse_pos(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if self.selecting:
            self.select_end = self.mouse_pos

    def draw_selection_rectangle(self):
        if self.selecting:
            x1, y1 = self.select_start
            x2, y2 = self.select_end
            rect_x = min(x1, x2)
            rect_y = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)

            selection_surf = pygame.Surface((width, height), pygame.SRCALPHA)
            selection_surf.fill((0, 120, 215, 80))

            self.window.blit(selection_surf, (rect_x, rect_y))
            pygame.draw.rect(self.window, (0, 120, 215), (rect_x, rect_y, width, height), 1)

    def update(self):
        self.get_mouse_pos()
        self.draw_selection_rectangle()
        self.draw()

    def draw(self):
        self.window.blit(self.cursor_image, self.mouse_pos)
