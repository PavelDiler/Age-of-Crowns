
import random

from settings import TILE_SIZE, MAP_WIDTH, MAP_HEIGHT


GRASS = 0
WATER = 1
STONE = 2


class World:

    def __init__(self, textures):
        self.textures = textures

        random.seed(10)

        self.map = [
            [GRASS for x in range(MAP_WIDTH)]
            for y in range(MAP_HEIGHT)
        ]

        self.create_area(WATER, 12, 10, 6, 4)

        self.create_area(STONE, 27, 19, 5, 4)

        self.create_area(STONE, 7, 23, 2, 2)
        self.create_area(STONE, 35, 7, 2, 2)

    def create_area(self, tile_type, center_x, center_y, radius_x, radius_y):

        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):

                
                dx = (x - center_x) / radius_x
                dy = (y - center_y) / radius_y

                distance = dx * dx + dy * dy

                
                border = random.uniform(0.75, 1.25)

                if distance < border:
                    self.map[y][x] = tile_type

    def draw(self, screen):

        map_pixel_width = MAP_WIDTH * TILE_SIZE
        map_pixel_height = MAP_HEIGHT * TILE_SIZE

        offset_x = (screen.get_width() - map_pixel_width) // 2
        offset_y = (screen.get_height() - map_pixel_height) // 2

        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):

                tile = self.map[y][x]

                if tile == GRASS:
                    texture = self.textures.get("grass")
                elif tile == WATER:
                    texture = self.textures.get("water")
                elif tile == STONE:
                    texture = self.textures.get("stone")
                else:
                    texture = None

                if texture is not None:
                    screen.blit(
                        texture,
                        (
                            offset_x + x * TILE_SIZE,
                            offset_y + y * TILE_SIZE
                        )
                    )
