from circleshape import *


class Asteroid(CircleShape):


    def __init__(self, x, y, radius):
        self.x = x
        self.y = y

        super().__init__(x, y, radius)  # initiates circleshape class

    def draw(self, screen):
            pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)
        
    def update(self, dt):
            
        self.position += (self.velocity * dt)