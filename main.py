import pygame
import sys

from settings import *
from game.textures import load_textures
from game.world import World


def main():
    pygame.init()

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    pygame.display.set_caption(GAME_TITLE)

    clock = pygame.time.Clock()

    textures = load_textures()
    world = World(textures)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        world.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()