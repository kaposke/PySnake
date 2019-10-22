import pygame
from grid import Grid


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.width, self.height = (1280, 720)
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.running = True

        self.grid = Grid((self.width - self.height, 0),
                         (self.height, self.height), (20, 20))

    def loop(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.grid.handle(event)

            self.grid.update()
            self.grid.draw(self.screen)

            pygame.display.update()

    def end(self):
        pygame.quit()
