import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updateable, drawable)
  Shot.containers = (shots, updateable, drawable)
  Asteroid.containers = (asteroids, updateable, drawable)
  AsteroidField.containers = updateable

  asteroid_field = AsteroidField()
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    screen.fill("black")

    for obj in updateable:
      obj.update(dt)

    for asteroid in asteroids:
      if asteroid.collided_with(player):
        print("Game over!")
        sys.exit()


    for obj in drawable:
      obj.draw(screen)

    pygame.display.flip()
    # limit the framerate to 60 FPS
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()