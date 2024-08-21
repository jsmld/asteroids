import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      random_angle = random.uniform(20, 50)
      a = self.velocity.rotate(random_angle)
      b = self.velocity.rotate(-random_angle)
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      # creates two new asteroids and sets the velocity at the same time
      Asteroid(self.position.x, self.position.y, new_radius).velocity = a * 1.2
      Asteroid(self.position.x, self.position.y, new_radius).velocity = b * 1.2