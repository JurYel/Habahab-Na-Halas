import pygame
from pygame.locals import *
from Snake import Snake 
from Apple import Apple
import time
import neat

SIZE = 40

class Game:
    def __init__(self, player_screen=(800, 600)):
        pygame.init()
        self.player_screen = player_screen
        self.screen_bg = (110, 110, 5)
        self.surface = pygame.display.set_mode((player_screen[:]))
        self.surface.fill((self.screen_bg[:]))
        self.snake = Snake(self.surface, self.screen_bg, length=2)
        self.snake.draw() 
        self.apple = Apple(self.surface)
        self.apple.draw()

    def check_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + (SIZE - 2):
            if y1 >= y2 and y1 <= y2 + (SIZE - 5 ):
                return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()

        if self.check_collision(self.snake.x[0], self.snake.y[0], \
                            self.apple.x, self.apple.y):
                self.apple.move()


    def run(self): 
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                    
                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()
                    
                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(.2)

if __name__ == '__main__':
    snakeGame = Game()
    snakeGame.run()
