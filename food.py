import random
import pygame


class Food:
    def __init__(self, block_size, width, height):
        self.block_size = block_size
        self.width = width
        self.height = height
        self.position = self.random_position()

    def random_position(self):
        x = random.randrange(0, self.width, self.block_size)
        y = random.randrange(0, self.height, self.block_size)
        return [x, y]

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, pygame.Rect(self.position[0], self.position[1],
                                                   self.block_size, self.block_size))
                                                   