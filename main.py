import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        for item in drawable:
            item.draw(screen)
        for info in updatable:
            info.update(dt)
        for object in asteroids:
            if player.collide(object):
                print("Game Over!")
                return
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        
if __name__ == "__main__":
    main()         
    

         