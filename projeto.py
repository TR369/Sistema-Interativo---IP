import pygame
from hunger import Hunger
from Classe_player import Player
from score import Score
from food import Food

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 684
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Castle")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)

player = Player(BLACK, SCREEN_WIDTH, SCREEN_HEIGHT)
score = Score(gameDisplay, 0, SCREEN_WIDTH - 20, 20)
hunger = Hunger(gameDisplay)

indoor_hirule = pygame.image.load("hirule.png")


DEAD = False

while not DEAD:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DEAD = True

    gameDisplay.blit(indoor_hirule, (0, 0))
    player.update()
    score.update(0)
    hunger.update(dt)
    pygame.display.update()


pygame.quit()
quit()
