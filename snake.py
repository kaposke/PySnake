import pygame
import numpy


class Snake:
    def __init__(self, position):
        self.position = position
        self.alive = True

        self.direction = (1, 0)
        self.counter = 0

        self.length = 1
        self.body = []

        self.alive = True

    def handle(self, event):
        dirX, dirY = self.direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and dirX != -1:
                self.direction = (1, 0)
            elif event.key == pygame.K_LEFT and dirX != 1:
                self.direction = (-1, 0)
            elif event.key == pygame.K_UP and dirY != 1:
                self.direction = (0, -1)
            elif event.key == pygame.K_DOWN and dirY != -1:
                self.direction = (0, 1)

            if event.key == pygame.K_a:
                self.length += 1
                print(self.length)

    def update(self, grid):
        if not self.alive:
            return

        self.counter += 1

        if self.counter == 60:
            self.counter = 0

            x, y = self.position
            dirX, dirY = self.direction
            new_pos = (x + dirX, y + dirY)

            if grid.is_inside(new_pos):
                self.move(new_pos)
            else:
                self.alive = False

    def move(self, position):
        self.body.append(self.position)
        if len(self.body) > self.length:
            self.body.pop(0)

        self.position = position
        print(self.position)

    def draw(self, surface, grid):
        color = (255, 255, 255)
        xOffset, yOffset = grid.position
        width, height = grid.cellSize

        for part in self.body:
            x, y = part
            rect = (x * width + xOffset, y * height + yOffset, width, height)

            pygame.draw.rect(surface, color, rect)
