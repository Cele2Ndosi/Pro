import pygame
import random
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE =(0, 0, 255)

# Game Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Dodge Game')

# Use clock to control the frame rate
clock = pygame.time.Clock()

# Player and the Enermy
class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.speed = 5

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

    def move(self, dx):
        self.x += dx
        if self.x < 0:
            self.x = 0
        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width

class FallingObject:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.y = -self.height
        self.speed = random.randint(3, 6)

    def update(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = -self.height
            self.x = random.randint(0, SCREEN_WIDTH - self.width)

    def draw(self):
        pygame.draw.rect(screen,RED, (self.x, self.y, self.width, self.height))

# Main Game Loop
def game_loop():
    player = Player()
    falling_objects = [FallingObject() for _ in range(5)]
    score = 0

    running = True
    while running:
        screen.fill(WHITE)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-player.speed)
        if keys[pygame.K_RIGHT]:
            player.move(player.speed)

        # Update falling objects
        for obj in falling_objects:
            obj.update()
            obj.draw()

        # Check for collision
        if player.x < obj.x + obj.width and player.x + player.width > obj.x and player.y < obj.y + obj.height and player.height + player.y > obj.y:
            print(f'Game Over! Score: {score}')
            running = False

        # Draw the player
        player.draw()

        # Update score
        score += 1
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(text, (10, 10))

        # Update the display
        pygame.display.flip()

        # Frame rate
        clock.tick(60)

game_loop()
pygame.quit()
        
