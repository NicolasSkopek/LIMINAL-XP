import pygame, sys

from scripts.settings import *
from scripts.windows import *

class StartGame:
    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.window = pygame.display.set_mode([WIDTH, HEIGHT])

        pygame.display.set_caption(TITLE)

        icon = pygame.image.load("assets/bg/icon.png")
        icon = pygame.transform.scale(icon, (32, 32))
        pygame.display.set_icon(icon)

        self.scene = "windows"
        self.current_scene = Windows()

        self.fps = pygame.time.Clock()

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.current_scene.events(event)


            self.fps.tick(60)
            self.window.fill("black")
            self.current_scene.draw()
            self.current_scene.update()
            pygame.display.flip()