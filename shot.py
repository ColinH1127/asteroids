from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, direction):
        super().__init__(x, y, radius) 
        self.velocity = pygame.Vector2(0, 1).rotate(direction)
        self.velocity *= PLAYER_SHOT_SPEED
        
        
        
    def draw(self, screen):
            pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        
        self.position += (self.velocity * dt)  
        
        

