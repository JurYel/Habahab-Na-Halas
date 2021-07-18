import pygame

SIZE = 40

class Snake:
    def __init__(self, game_screen, bg_color, length):
        self.bg_color = bg_color
        self.game_screen = game_screen
        self.length = length
        self.block = pygame.image.load("assets/block.jpg").convert()
        self.x = [SIZE] * 100
        self.y = [SIZE] * 100
        self.direction = 'down'

    def draw(self):
        self.game_screen.fill((self.bg_color[:]))
        for i in range(self.length):
            self.game_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_up(self):
        self.direction = 'up'
    
    def move_down(self):
        self.direction = 'down'
    
    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def walk(self):

        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        
        if self.direction == 'right':
            self.x[0] += SIZE

        if self.direction == 'up':
            self.y[0] -= SIZE

        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()
        