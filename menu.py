import pygame
from pygame import *
from pygame.locals import *

pygame.init()

video = 1920, 1080

Width = 810
Height = 520

bg_s = (Width, Height)

screen = pygame.display.set_mode((Width, Height), RESIZABLE)
current_size = screen.get_size()
virtual_surface = Surface((Width, Height))
FPS = 15
clock = pygame.time.Clock()
pygame.display.set_caption("My game")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

cellSize = 30
world = [
    "                           ",
    "                           ",
    "    XX                     ",
    "                           ",
    "          XXX              ",
    "                 XXX       ",
    "                           ",
    "                           ",
    "      XXX XX               ",
    "                           ",
    "                  XX       ",
    "XXX                        ",
    "                           ",
    "                           ",
    "                           ",
]  # 27 x 27 15x27
worldwidth = Width // cellSize
worldheight: Height = Width // cellSize

for row in range(worldheight):
    line = []
    for col in range(worldwidth):
        line.append(0)
    world.append(line)

bg = pygame.image.load("images/bg.jpg")
bg = pygame.transform.scale(bg, bg_s)

none = pygame.image.load("images/none.png")

platform = pygame.image.load("images/platform.png")
platform = pygame.transform.scale(platform, (30, 30))

coins = [
    pygame.image.load("images/coin0.png"),
    pygame.image.load("images/coin1.png"),
    pygame.image.load("images/coin2.png"),
    pygame.image.load("images/coin3.png"),
    pygame.image.load("images/coin4.png"),
    pygame.image.load("images/coin5.png"),
    pygame.image.load("images/coin6.png"),
    pygame.image.load("images/coin7.png"),
]

walk_right = [
    pygame.image.load("images/right1.png"),
    pygame.image.load("images/right2.png"),
    pygame.image.load("images/right3.png"),
    pygame.image.load("images/right4.png"),
]

walk_left = [
    pygame.image.load("images/left1.png"),
    pygame.image.load("images/left2.png"),
    pygame.image.load("images/left3.png"),
    pygame.image.load("images/left4.png"),
]

coins_animation_count = 0

coins_speed = 5
coin_x = 25
coin_y = 400

player_animation_count = 0

jump_count = 8

pl_speed = 7
pl_x = 10
pl_y = 400

is_jump = True

bg_song = pygame.mixer.Sound("songs/song.mp3")
bg_song.play()

running = True
while running:
    clock.tick(FPS)
    virtual_surface.blit(bg, (0, 0))
    virtual_surface.blit(coins[coins_animation_count], (coin_x, coin_y))
    virtual_surface.blit(platform, (360, 300))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        virtual_surface.blit(walk_right[player_animation_count], (pl_x, pl_y))
    elif keys[pygame.K_a]:
        virtual_surface.blit(walk_left[player_animation_count], (pl_x, pl_y))
    else:
        virtual_surface.blit(none, (pl_x, pl_y))

    if keys[pygame.K_a] and pl_x > 8:
        pl_x -= pl_speed
    elif keys[pygame.K_d] and pl_x < 750:
        pl_x += pl_speed

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -8:
            if jump_count > 0:
                pl_y -= (jump_count ** 2) / 2
            else:
                pl_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 8

    if player_animation_count == 3:
        player_animation_count = 0
    else:
        player_animation_count += 1

    if coins_animation_count == 6:
        coins_animation_count = 0
    else:
        coins_animation_count += 1

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == VIDEORESIZE:
            current_size = event.size
    scaled_surface = transform.scale(virtual_surface, current_size)
    screen.blit(scaled_surface, (0, 0))

    pygame.display.flip()

quit()
