
import pygame
import os

ASSETS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "assets"
)


def load_texture(folder, name):
    path = os.path.join(
        ASSETS_PATH,
        folder,
        name + ".png"
    )

    try:
        image = pygame.image.load(path).convert_alpha()
        return image

    except (pygame.error, FileNotFoundError):
        print(f"Ошибка загрузки текстуры: {path}")
        return None


def load_textures():

    textures = {}

    textures["grass"] = load_texture("terrain", "grass")
    textures["water"] = load_texture("terrain", "water")
    textures["stone"] = load_texture("terrain", "stone")

    return textures
