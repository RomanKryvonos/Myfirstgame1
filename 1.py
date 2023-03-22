import pygame
from pygame import *
from pygame.locals import *

pygame.init()

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

#pause = pygame.image.load("images/pause.png")
#pause = pygame.transform.scale(pause, (50, 50))
start = pygame.image.load("images/start.png")
start = pygame.transform.scale(start, (250, 85))
bg = pygame.image.load("images/bg.jpg")
bg = pygame.transform.scale(bg, (bg_s))

none = pygame.image.load("images/none.png")

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

player_animation_count = 0

jump_count = 8

pl_speed = 7
pl_x = 10
pl_y = 400

bg_song = pygame.mixer.Sound("songs/song.mp3")
bg_song.play()

is_jump = True

running = True
while running:
    clock.tick(FPS)



    virtual_surface.blit(bg, (0, 0))

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



