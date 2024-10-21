import pygame

from define import *


# Tạo lớp Ball (Bóng)
class Ball(pygame.sprite.Sprite):
    def __init__(self, size, speed_x, speed_y, color):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - size // 2
        self.rect.y = HEIGHT // 2 - size // 2
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.size = size

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Va chạm với cạnh trên và dưới màn hình
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

        # Kiểm tra nếu bóng chạm vào vùng khung thành bên trái
        if self.rect.left <= 0:
            if (
                HEIGHT // 2 - GOAL_HEIGHT // 2
                <= self.rect.centery
                <= HEIGHT // 2 + GOAL_HEIGHT // 2
            ):
                return (
                    "player2"  # Người chơi 2 ghi điểm nếu bóng chạm vào "khung thành"
                )
            else:
                self.speed_x *= -1  # Bóng bật lại nếu không vào khung thành
        # Kiểm tra nếu bóng chạm vào vùng "khung thành" bên phải
        elif self.rect.right >= WIDTH:
            if (
                HEIGHT // 2 - GOAL_HEIGHT // 2
                <= self.rect.centery
                <= HEIGHT // 2 + GOAL_HEIGHT // 2
            ):
                return (
                    "player1"  # Người chơi 1 ghi điểm nếu bóng chạm vào "khung thành"
                )
            else:
                self.speed_x *= -1  # Bóng bật lại nếu không vào khung thành
        return None

    def reset(self):
        # Đặt lại bóng ở giữa màn hình và đảo hướng di chuyển
        self.rect.x = WIDTH // 2 - self.size // 2
        self.rect.y = HEIGHT // 2 - self.size // 2
        self.speed_x *= -1
