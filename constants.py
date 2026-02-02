import pygame

# window size
WIDTH = 800
HEIGHT = 800

# Player variables
PLAYER_NAME = "Ghost"
FRIEND1_NAME = "Shredder"
FRIEND2_NAME = "Hannah"

# Map
MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT

GAME_MAP = [["Room 0 where unused objects are kept", 0, 0, False, False]]
OUTDOOR_ROOMS = range(1, 26)  # this looks like a constant to me
for planetsectors in range(25):
    GAME_MAP.append(["The dusty planet surface", 13, 13, True, True])

GAME_MAP.extend(
    [
        # ["Room name", height, width, Top exit?, Right exit?]
        ["Airlock", 13, 5, True, False],  # room 26
        ["Engineering Lab", 13, 13, False, False],  # room 27
        ["Gator Mission Control", 9, 13, False, True],  # room 28
        ["Viewing Gallery", 9, 15, False, False],  # room 29
        ["Crew's Bathroom", 5, 5, False, False],  # room 30
        ["Airlock Entry Bay", 7, 11, True, True],  # room 31
        ["Left Elbow Room", 9, 7, True, False],  # room 32
        ["Right Elbow Room", 7, 13, True, True],  # room 33
        ["Science Lab", 13, 13, False, True],  # room 34
        ["Greenhouse", 13, 13, True, False],  # room 35
        [f"{PLAYER_NAME}'s Sleeping Quarters", 9, 11, False, False],  # room 36
        ["West Corridor", 15, 5, True, True],  # room 37
        ["Briefing Room", 7, 13, False, True],  # room 38
        ["Community Room", 11, 13, True, False],  # room 39
        ["Main Mission Conrol", 14, 14, False, False],  # room 40
        ["Sick Bay", 12, 7, True, False],  # room 41
        ["West Corridor", 9, 7, True, False],  # room 42
        ["Utilities Control Room", 9, 9, False, True],  # room 43
        ["Systems Engineering Bay", 9, 11, False, False],  # room 44
        ["Security Portal to Mission Control", 7, 7, True, False],  # room 45
        [f"{FRIEND1_NAME}'s Sleeping Quarters", 9, 11, True, True],  # room 46
        [f"{FRIEND2_NAME}'s Sleeping Quarters", 9, 11, True, True],  # room 47
        ["Pipeworks", 13, 11, True, False],  # room 48
        ["Chief Scientist's Office", 9, 7, True, True],  # room 49
        ["Robot Workshop", 9, 11, True, False],  # room 50
    ]
)

# Load images
BACKDROP = pygame.image.load("images/backdrop.jpg")

FLOOR = pygame.image.load("images/floor.png")
PILLAR = pygame.image.load("images/pillar.png")
SOIL = pygame.image.load("images/soil.png")
DEMO_OBJECTS = [FLOOR, PILLAR, SOIL]
