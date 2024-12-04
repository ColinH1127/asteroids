import pygame
from constants import *

def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0), rect = (SCREEN_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_WIDTH))
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000
        
    

if __name__ == "__main__":
    main()          