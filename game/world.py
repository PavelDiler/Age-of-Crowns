
import pygame

from settings import TILE_SIZE, MAP_WIDTH, MAP_HEIGHT


class World:

    def __init__(self, textures):

        self.textures = textures

        
        self.map = [
            [0 for x in range(MAP_WIDTH)]
            for y in range(MAP_HEIGHT)
        ]

    def draw(self, screen):

        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):

                tile = self.map[y][x]

                # Получаем текстуру клетки
                if tile == 0:
                    texture = self.textures["grass"]

                if texture:
                    screen.blit(
                        texture,
                        (x * TILE_SIZE, y * TILE_SIZE)
                    )
