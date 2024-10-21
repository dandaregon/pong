import pygame


from define import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.image.fill(color)
        self.rect.x = x
        self.rect.y = y
        self.speed_y = 0
        self.speed = speed

    def update(self):
        self.rect.y += self.speed_y

        # Giới hạn thanh không di chuyển ra khỏi màn hình
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
