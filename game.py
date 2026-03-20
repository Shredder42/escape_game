import pygame
from constants import *
from make_map import *

# from explorer import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Escape!")
clock = pygame.time.Clock()
running = True

current_room = 31

# top_left_x = 100
# top_left_y = 150

# verify GAME_MAP data entry
# print(GAME_MAP)
assert len(GAME_MAP) - 1 == MAP_SIZE, "Map size and game map don't match"

room_map = generate_map(
    GAME_MAP, current_room, OUTDOOR_ROOMS
)  # might be able to get rid of this command
# for row in room_map:
#     print(row)


while running:

    screen.blit(BACKDROP, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_room = move_rooms("left", current_room)
            if event.key == pygame.K_RIGHT:
                current_room = move_rooms("right", current_room)
            if event.key == pygame.K_UP:
                current_room = move_rooms("up", current_room)
            if event.key == pygame.K_DOWN:
                current_room = move_rooms("down", current_room)

    draw_room(GAME_MAP, current_room, OUTDOOR_ROOMS, screen)

    pygame.display.flip()

    clock.tick(60)  # frame rate in fps

pygame.quit()
