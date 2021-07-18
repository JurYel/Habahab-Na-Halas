import pygame
import random

SIZE = 40

class Apple:
    def __init__(self, game_screen):
        self.image = pygame.image.load("assets/apple.png").convert_alpha()
        self.game_screen = game_screen
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.game_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 19) * SIZE
        self.y = random.randint(0, 14) * SIZE