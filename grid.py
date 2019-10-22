import pygame
from snake import Snake


class Grid:

    def __init__(self, position, size, resolution):
        self.position = position
        self.size = size
        self.resolution = resolution

        x, y = resolution
        self.snake = Snake((x / 2, y / 2))

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.restart()
            self.snake.handle(event)

    def update(self):
        self.snake.update(self)

    def draw(self, surface):
        color = (100, 100, 100)

        x, y = self.position
        cols, rows = self.resolution
        width, height = self.size
        cellWidth, cellHeight = (width / cols, height / rows)

        for i in range(cols + 1):
            start = (x + i * cellWidth, y)
            end = (x + i * cellWidth, y + height)
            pygame.draw.line(surface, color, start, end)

        for i in range(rows + 1):
            start = (x, y + i * cellHeight)
            end = (x + width, y + i * cellHeight)
            pygame.draw.line(surface, color, start, end)

        self.snake.draw(surface, self)

    def is_inside(self, position):
        x, y = position
        width, height = self.resolution
        return x >= 0 and x < width and y >= 0 and y < height

    def restart(self):
        x, y = self.resolution
        self.snake = Snake((x / 2, y / 2))

    @property
    def cellSize(self):
        width, height = self.size
        cols, rows = self.resolution
        return (width / cols, height / rows)
