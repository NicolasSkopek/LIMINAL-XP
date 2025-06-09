import pygame

class Obj(pygame.sprite.Sprite):

    def __init__(self, img, pos, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.frame = 0
        self.tick = 0

    def animation(self, speed, frames, path, file_type):
        self.tick += 1
        if self.tick > speed:
            self.tick = 0
            self.frame += 1
            if self.frame > frames - 1:
                self.frame = 0
            self.image = pygame.image.load(path + str(self.frame) + "." + file_type)

class File(Obj):
    def __init__(self, title, *groups):
        super().__init__(title, *groups)

        self.image = pygame.image.load("file.png")

    def update(self):
        pass


class StartButton(Obj):
    def __init__(self, image_path, pos, group, hover_path):
        super().__init__(image_path, pos, group)
        self.image_default = pygame.image.load(image_path).convert_alpha()
        self.image_hover = pygame.image.load(hover_path).convert_alpha() if hover_path else self.image_default

        self.image = self.image_default
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.image_hover
        else:
            self.image = self.image_default