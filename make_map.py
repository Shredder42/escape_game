from constants import MAP_WIDTH, MAP_HEIGHT, MAP_SIZE


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
            room_map[MAP_HEIGHT - 1][middle_column] = floor_type
            room_map[MAP_HEIGHT - 1][middle_column - 1] = floor_type
            room_map[MAP_HEIGHT - 1][middle_column + 1] = floor_type

    return room_map
