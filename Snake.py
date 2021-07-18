import pygame

class Snake:
    def __init__(self, game_screen, bg_color):
        self.bg_color = bg_color
        self.game_screen = game_screen
        self.block = pygame.image.load("assets/block.jpg").convert()
        self.x = 100
        self.y = 100
        self.direction = 'down'

    def draw(self):
        self.game_screen.fill((self.bg_color[:]))
        self.game_screen.blit(self.block, (self.x, self.y))
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
        if self.direction == 'left':
            self.x -= 20
        
        if self.direction == 'right':
            self.x += 20

        if self.direction == 'up':
            self.y -= 20

        if self.direction == 'down':
            self.y += 20

        self.draw()
        