import pygame
import sys

# Импортируем наши модули
from snake import Snake
from food import Food
import config


pygame.init()
font = pygame.font.SysFont('Arial', 25)
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Змейка")

clock = pygame.time.Clock()

# Создаём объекты
snake = Snake(config.BLOCK_SIZE)
food = Food(config.BLOCK_SIZE, config.WIDTH, config.HEIGHT)
score = 0

# Функция для отображения счёта
def draw_score(score):
    value = font.render(f"Счёт: {score}", True, config.WHITE)
    screen.blit(value, [10, 10])

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            snake.change_direction(event.key)

    # Двигаем змейку
    snake.move()

    # Проверяем столкновения
    if snake.check_collision_with_walls(config.WIDTH, config.HEIGHT) or snake.check_collision_with_self():
        print("Игра окончена!")
        running = False

    # Проверяем, съела ли змейка еду
    if snake.eat_food(food.position):
        food.position = food.random_position()
        score += 1

    # Рисуем всё
    screen.fill(config.BLACK)
    draw_score(score)
    snake.draw(screen, config.GREEN)
    food.draw(screen, config.WHITE)

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
sys.exit()
