import pygame
from constants import *
from make_map import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Escape!")
clock = pygame.time.Clock()
running = True

current_room = 31

top_left_x = 100
top_left_y = 150

# verify GAME_MAP data entry
# print(GAME_MAP)
assert len(GAME_MAP) - 1 == MAP_SIZE, "Map size and game map don't match"

room_map = generate_map(GAME_MAP, current_room, OUTDOOR_ROOMS)
for row in room_map:
    print(row)


while running:

    screen.blit(BACKDROP, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)  # frame rate in fps

pygame.quit()
