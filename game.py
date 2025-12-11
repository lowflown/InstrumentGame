import pygame
import sys
import os
import time
import random

# -- Screen & Variables--
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("InstrumentGame")
# music_playback = pygame.mixer.music.load(
#     os.path.join("assets/sound/music/DokiDoki.mp3")
# )
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.15)
clock = pygame.time.Clock()


# -- Classes --
class Instrument(pygame.sprite.Sprite):  # trqbva da dobavq animacii
    def __init__(self, image_path, sound_path, x, y, keybind):
        super().__init__()
        self.image = pygame.image.load(os.path.join(image_path)).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = pygame.mixer.Sound(sound_path)

        self.last = 0
        self.cooldown = 180
        self.keybind = keybind

    def update(self):
        self.key_press()

    def key_press(self):
        if pygame.key.get_pressed()[self.keybind]:
            now = pygame.time.get_ticks()
            if now - self.last > self.cooldown:
                self.sound.play()
                self.last = now
            if tile_default.collide_line:
                print("yes")
                tile_default.rect.y = 0
                tile_default.collide_line = False

class Tiles(pygame.sprite.Sprite):
    collide_line = False
    def __init__(self, x, y, gravity, offset):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join("assets/sprites/tile.png")
        ).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.gravity = gravity
        self.offset = offset

    def update(self):
        self.rect.y += self.gravity
        self.rect.x += self.offset
        self.colliding_with_line()

    def colliding_with_line(self):
        if pygame.sprite.spritecollide(self, noteline_group, False):
            self.collide_line = True
        else:
            self.collide_line = False


class Grid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join("assets/sprites/gird.png")
        ).convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))


class NoteLine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join("assets/sprites/note_line.png")
        ).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))


# -- Instrument Group --
instrument_group = pygame.sprite.Group()

cymbal = Instrument(
    "assets/sprites/cymbal_up.png",
    "assets/sound/sfx/cymbal_crash.mp3",
    213,
    760,
    pygame.K_z,
)

drum = Instrument(
    "assets/sprites/drum_up.png", "assets/sound/sfx/drum.mp3", 213 * 2, 780, pygame.K_c
)

big_drum = Instrument(
    "assets/sprites/bigdrum.png",
    "assets/sound/sfx/bass_drumsfx.mp3",
    213 * 3,
    800,
    pygame.K_b,
)

drum_left = Instrument(
    "assets/sprites/drum_up.png", "assets/sound/sfx/drum2.mp3", 213 * 4, 780, pygame.K_v
)

cymbal_left = Instrument(
    "assets/sprites/cymbal_up.png",
    "assets/sound/sfx/cymbal2.mp3",
    213 * 5,
    760,
    pygame.K_x,
)

instrument_group.add(cymbal, drum, big_drum, drum_left, cymbal_left)

# -- Tile Group --
tile_group = pygame.sprite.Group()
tile_default = Tiles(320, 20, 2, 0)
tile_group.add(tile_default)

# -- Grid Group --
grid_group = pygame.sprite.Group()
grid_default = Grid(300, 50)
grid_group.add(grid_default)

# -- Note Line Group --
noteline_group = pygame.sprite.Group()
noteline_default = NoteLine(320, 650)
noteline_default.add(noteline_group)

# -- Background --
background_static = pygame.image.load(
    "assets/backgrounds/background1.png"
).convert_alpha()

# == Loop ==
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # -- Drawing --
    screen.blit(background_static, (0, 0))
    instrument_group.draw(screen)
    tile_group.draw(screen)
    grid_group.draw(screen)
    noteline_group.draw(screen)

    # -- Mouse --
    mouse_pos = pygame.mouse.get_pos()

    # -- Tiles --
    tile_group.update()
    # -- Instruments --
    instrument_group.update()

    # -- Updating (End of loop) --
    pygame.display.update()
    clock.tick(60)
