import pygame


class Snake:
    def __init__(self, block_size):
        self.block_size = block_size
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = 'RIGHT'

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == 'UP':
            head_y -= self.block_size
        elif self.direction == 'DOWN':
            head_y += self.block_size
        elif self.direction == 'LEFT':
            head_x -= self.block_size
        elif self.direction == 'RIGHT':
            head_x += self.block_size

        new_head = [head_x, head_y]
        self.body.insert(0, new_head)

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != 'DOWN':
            self.direction = 'UP'
        elif key == pygame.K_DOWN and self.direction != 'UP':
            self.direction = 'DOWN'
        elif key == pygame.K_LEFT and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif key == pygame.K_RIGHT and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def eat_food(self, food_pos):
        if self.body[0] == food_pos:
            return True
        else:
            self.body.pop()
            return False

    def draw(self, screen, color):
        for segment in self.body:
            pygame.draw.rect(screen, color, pygame.Rect(segment[0], segment[1],
                                                       self.block_size, self.block_size))

    def check_collision_with_self(self):
        # Проверяем столкновение головы с телом
        head = self.body[0]
        for segment in self.body[1:]:
            if segment == head:
                return True
        return False

    def check_collision_with_walls(self, width, height):
        head_x, head_y = self.body[0]
        return (
            head_x < 0 or head_x >= width or
            head_y < 0 or head_y >= height
        )
        