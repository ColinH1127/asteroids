from circleshape import *
from constants import *
import random 

class Asteroid(CircleShape):


    def __init__(self, x, y, radius):
        self.x = x
        self.y = y

        super().__init__(x, y, radius)  # initiates circleshape class

    def draw(self, screen):
            pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)
        
    def update(self, dt):
            
        self.position += (self.velocity * dt)
    
    def split(self):
         
         if self.radius <= ASTEROID_MIN_RADIUS:
              self.kill()
              return
         else:

            random_angle = random.uniform(20, 51)
            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius) 
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity = vector2 * 1.2
            self.kill()
