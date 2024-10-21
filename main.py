import pygame
import sys

from define import *
from ball import Ball
from player import Player

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ping Pong")

        self.player1 = Player(30, HEIGHT // 2 - 50, 10, 100, 10, RED)
        self.player2 = Player(WIDTH - 40, HEIGHT // 2 - 50, 10, 100, 10, BLUE)
        self.ball = Ball(20, 5, 5, GREEN)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player1)
        self.all_sprites.add(self.player2)
        self.all_sprites.add(self.ball)

        self.player1_score = 0
        self.player2_score = 0

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 74)

    def Key_event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player1.speed_y = -self.player1.speed
        elif keys[pygame.K_s]:
            self.player1.speed_y = self.player1.speed
        else:
            self.player1.speed_y = 0

        if keys[pygame.K_UP]:
            self.player2.speed_y = -self.player2.speed
        elif keys[pygame.K_DOWN]:
            self.player2.speed_y = self.player2.speed
        else:
            self.player2.speed_y = 0

    def Check(self):
        if pygame.sprite.collide_rect(
            self.ball, self.player1
        ) or pygame.sprite.collide_rect(self.ball, self.player2):
            self.ball.speed_x *= -1

        result = self.ball.update()
        if result == "player1":
            self.player1_score += 1
            self.ball.reset()
        elif result == "player2":
            self.player2_score += 1
            self.ball.reset()

    def draw_scores(self):

        player1_text = self.font.render(str(self.player1_score), True, WHITE)
        self.screen.blit(player1_text, (WIDTH // 4, 20))

        player2_text = self.font.render(str(self.player2_score), True, WHITE)
        self.screen.blit(player2_text, (WIDTH * 3 // 4, 20))

    def check_winner(self):

        if self.player1_score >= WINNING_SCORE:
            return "Người chơi 1 thắng!"
        elif self.player2_score >= WINNING_SCORE:
            return "Người chơi 2 thắng!"

    def draw_goal_area(self):

        pygame.draw.rect(
            self.screen, WHITE, (0, HEIGHT // 2 - GOAL_HEIGHT // 2, 10, GOAL_HEIGHT), 2
        )
        pygame.draw.rect(
            self.screen,
            WHITE,
            (WIDTH - 10, HEIGHT // 2 - GOAL_HEIGHT // 2, 10, GOAL_HEIGHT),
            2,
        )

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.Key_event()

            self.all_sprites.update()
            self.Check()
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)

            self.draw_goal_area()

            self.draw_scores()

            winner = self.check_winner()
            if winner:
                print(winner)
                running = False 

            pygame.draw.line(
                self.screen,
                WHITE,
                (WIDTH / 2, 0),
                (WIDTH / 2, HEIGHT),
                width=LINE_WIDTH,
            )
            pygame.display.flip()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
