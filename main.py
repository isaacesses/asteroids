import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # Initialize the game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Draw the game to the screen
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.display.flip()


if __name__ == "__main__":
    main()
