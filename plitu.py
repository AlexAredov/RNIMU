# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 500
HEIGHT = 500
FPS = 5

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self, xx, yy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (xx, yy)
        
    
    def update(self):
        print(self.rect.x, self.rect.y)
        if self.rect.x < WIDTH and self.rect.y == 0:
            self.rect.x += 50
        if self.rect.x == WIDTH - 50 and self.rect.y < HEIGHT - 50:
            self.rect.y += 50
        if self.rect.x > 0 and self.rect.y == HEIGHT - 50:
            self.rect.x -= 50
        if self.rect.x == 0 and self.rect.y > 0:
            self.rect.y -= 50
        if self.rect.x == 0 and self.rect.y == 0:
            self.rect.x = 50
            self.rect.y = 0


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
x = 25
y = 25
for i in range(10):
    x += 50
    all_sprites.add(Player(x, y))

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.draw.rect(screen, GREEN, (0, 0, 50, 50))
    pygame.draw.rect(screen, GREEN, (0, 450, 50, 50))
    pygame.draw.rect(screen, GREEN, (450, 450, 50, 50))
    pygame.draw.rect(screen, GREEN, (450, 0, 50, 50))
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()