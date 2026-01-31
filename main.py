import sys

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot
from playerlives import LivesManager



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    lives = LivesManager(lives=3, respawn_pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    shot_count = 0
    dt = 0
    

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        lives.update(dt)



    # check for collisions but give the player 3 lives
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                # ignore collisions while the player is invulnerable
                if lives.is_invulnerable():
                    continue

                log_event("player_hit")
                # register the hit; hit() returns True if player still has lives
                still_alive = lives.hit()
                if not still_alive:
                    print("Game over!")
                    print(f"Total asteroids hit: {shot_count}")
                    sys.exit()

                # player is still alive: respawn and remove the asteroid that hit them
                lives.respawn(player)
                asteroid.kill()
                # skip checking this asteroid against shots since it's removed
                continue




            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    shot_count += 1

        #fill blue
        screen.fill((255, 110, 199))

        # Draw the shot counter in the top right corner
        font = pygame.font.Font(None, 36)
        text = font.render(f"Asteroids Hit: {shot_count}", True, "black")
        screen.blit(text, (SCREEN_WIDTH - 200, 20))

        #draw the lives counter in the top left corner
        lives.render(screen, font)      

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()


    