from constants import (
    MAP_WIDTH,
    MAP_HEIGHT,
    MAP_SIZE,
    DEMO_OBJECTS,
    TOP_LEFT_X,
    TOP_LEFT_Y,
)


def get_floor_type(current_room, outdoor_rooms):
    if current_room in outdoor_rooms:
        return 2  # soil
    else:
        return 0  # tiled floor


def generate_map(game_map, current_room, outdoor_rooms):
    # this function makes the map for the current room,
    # using room data, scenery data and prop data.
    global room_map, room_width, room_height, room_name, hazard_map
    global top_left_x, top_left_y, wall_transparency_frame
    room_data = game_map[current_room]
    room_name = room_data[0]
    room_height = room_data[1]
    room_width = room_data[2]

    floor_type = get_floor_type(current_room, outdoor_rooms)
    if current_room in range(1, 21):
        bottom_edge = 2  # soil
        side_edge = 2  # soil
    if current_room in range(21, 26):
        bottom_edge = 1  # wall
        side_edge = 2  # soil
    if current_room > 25:
        bottom_edge = 1  # wall
        side_edge = 1  # wall

    # Create top line of room map
    room_map = [[side_edge] * room_width]
    # Add middle lines of room map (wall, floor to fill width, wall)
    for y in range(room_height - 2):
        room_map.append([side_edge] + [floor_type] * (room_width - 2) + [side_edge])
    # Add bottom line of room map
    room_map.append([bottom_edge] * room_width)

    # Add doorways
    middle_row = int(room_height / 2)
    middle_column = int(room_width / 2)

    if room_data[4]:  # If exit at right of this room
        room_map[middle_row][room_width - 1] = floor_type
        room_map[middle_row - 1][room_width - 1] = floor_type
        room_map[middle_row + 1][room_width - 1] = floor_type

    if current_room % MAP_WIDTH != 1:  # If room not on left side of map
        if game_map[current_room - 1][4]:  # If room on left has right exit
            room_map[middle_row][0] = floor_type
            room_map[middle_row - 1][0] = floor_type
            room_map[middle_row + 1][0] = floor_type

    if room_data[3]:  # If exit at top of this room
        room_map[0][middle_column] = floor_type
        room_map[0][middle_column - 1] = floor_type
        room_map[0][middle_column + 1] = floor_type

    if current_room <= MAP_SIZE - MAP_WIDTH:  # If room not in bottom row
        if game_map[current_room + MAP_WIDTH][3]:  # If room below has top exit
            room_map[room_height - 1][middle_column] = floor_type
            room_map[room_height - 1][middle_column - 1] = floor_type
            room_map[room_height - 1][middle_column + 1] = floor_type

    return room_map


##############
## Explorer ##
##############


def draw_room(game_map, current_room, outdoor_rooms, screen):
    global room_height, room_width, room_map
    generate_map(game_map, current_room, outdoor_rooms)
    screen.fill("black")  # this takes place of the screen.clear command in the book

    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = DEMO_OBJECTS[room_map[y][x]]
            screen.blit(
                image_to_draw,
                (
                    TOP_LEFT_X + (x * 30),
                    TOP_LEFT_Y + (y * 30) - image_to_draw.get_height(),
                ),
            )
    return


def move_rooms(move, current_room):
    old_room = current_room

    if move == "left":
        current_room -= 1
    if move == "right":
        current_room += 1
    if move == "up":
        current_room -= MAP_WIDTH
    if move == "down":
        current_room += MAP_WIDTH

    if current_room > 50:
        current_room = 50
    if current_room < 1:
        current_room = 1

    if current_room != old_room:
        print(f"Entering room: {current_room}")

    return current_room
