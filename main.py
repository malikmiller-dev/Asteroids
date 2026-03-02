import sys
import pygame

from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    """ Main function to run Asteroids game """
    x = (SCREEN_WIDTH / 2)
    y = (SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    player = Player(x, y)
    asteroid_field = AsteroidField()
    shot = Shot(x, y)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    while True:
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                main()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_kill")
                    print("Asteroid Destroyed")
                    asteroid.split()
                    log_event("asteroid_split")
                    shot.kill()
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
