# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    # initialize pygame and create a window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    
    # setup the display
    pygame.display.set_caption("Asteroids")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")

    # main game loop
    while True:
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()    
    
if __name__ == "__main__":
    main()
