import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # Initialize the game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game clock
    clock = pygame.time.Clock()
    dt = 0.0

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Initiate the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create AsteroidField object
    field = AsteroidField()

    # Draw the game to the screen
    while True:
        dt = clock.tick(60) / 1000

        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")

        # Draw player
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)

        # Check for collisions
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.display.flip()


if __name__ == "__main__":
    main()
