import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            first_asteroid_movement = self.velocity.rotate(angle)
            second_asteroid_movement = self.velocity.rotate(-angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0], self.position[1], radius)
            asteroid2 = Asteroid(self.position[0], self.position[1], radius)
            asteroid1.velocity = first_asteroid_movement * 1.2
            asteroid2.velocity = second_asteroid_movement * 1.2