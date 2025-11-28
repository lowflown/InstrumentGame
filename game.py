import pygame
import sys
import os
import time

# -- Screen & Variables--
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("InstrumentGame")
music_playback = pygame.mixer.music.load(
    os.path.join("assets/sound/music/DokiDoki.mp3")
)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.15)
clock = pygame.time.Clock()


# -- Classes --
class Instrument(pygame.sprite.Sprite):  # trqbva da dobavq animacii
    def __init__(self, image_path, sound_path, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join(image_path)).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = pygame.mixer.Sound(sound_path)

        self.last = 0
        self.cooldown = 180

    # -- Clicked By Mouse --
    def clicked_bymouse(self):
        if self.rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                now = pygame.time.get_ticks()
                if now - self.last > self.cooldown:
                    self.sound.play()
                    self.last = now


class Tiles(pygame.sprite.Sprite):
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
    "assets/sprites/cymbal_up.png", "assets/sound/sfx/cymbal_crash.mp3", 213, 760
)
cymbal_left = Instrument(
    "assets/sprites/cymbal_up.png", "assets/sound/sfx/cymbal2.mp3", 213 * 5, 760
)
drum = Instrument(
    "assets/sprites/drum_up.png", "assets/sound/sfx/drum.mp3", 213 * 2, 780
)
drum_left = Instrument(
    "assets/sprites/drum_up.png", "assets/sound/sfx/drum2.mp3", 213 * 4, 780
)
big_drum = Instrument(
    "assets/sprites/bigdrum.png", "assets/sound/sfx/bass_drumsfx.mp3", 213 * 3, 800
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

    # -- Keys & Mouse Variables
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # -- Mouse --
    for instrument in instrument_group:
        instrument.clicked_bymouse()

    # -- Tiles --
    tile_group.update()

    # drum.clicked_bymouse()
    # big_drum.clicked_bymouse()
    # drum_left.clicked_bymouse()

    # -- Keyboard Presses --
    # if keys[pygame.K_z]:
    # cymbal.sound.play()
    # pygame.time.delay(180)

    # if keys[pygame.K_x]:
    #     drum.sound.play()
    #     pygame.time.delay(180)

    # if keys[pygame.K_c]:
    #     big_drum.sound.play()
    #     pygame.time.delay(180)

    # if keys[pygame.K_v] and cooldown == False:
    #     drum_left.sound.play()

    # -- Updating (End of loop) --
    pygame.display.update()
    clock.tick(60)
