current_direction = 'east'
horizontal_position = 0
vertical_position = 0
directions = [[direction[0], int(direction[1:])] for direction in open('day12_input.txt')]

next_direction = { 'north': 'east', 'east': 'south', 'south': 'west', 'west': 'north'}
# part 1
for direction, distance in directions:
    if direction == 'F':
        if current_direction == 'east':
            horizontal_position += distance
        elif current_direction == 'west':
            horizontal_position -= distance
        elif current_direction == 'north':
            vertical_position += distance
        elif current_direction == 'south':
            vertical_position -= distance
    elif direction == 'N':
        vertical_position += distance
    elif direction == 'S':
        vertical_position -= distance
    elif direction == 'E':
        horizontal_position += distance
    elif direction == 'W':
        horizontal_position -= distance
    elif direction == 'R' or direction == 'L':
        rotations = distance/ 90
        rotations = 4 - rotations if direction == 'L' else rotations
        while rotations > 0:
            current_direction = next_direction[current_direction]
            rotations -= 1
print('part 1 manhattan distance', abs(horizontal_position) + abs(vertical_position))

# part 2
horizontal_position = 0
vertical_position = 0
waypoint_horizontal = 10
waypoint_vertical = 1

for direction, distance in directions:
    if direction == 'F':
        horizontal_position += waypoint_horizontal * distance
        vertical_position += waypoint_vertical * distance
    elif direction == 'N':
        waypoint_vertical += distance
    elif direction == 'S':
        waypoint_vertical -= distance
    elif direction == 'E':
        waypoint_horizontal += distance
    elif direction == 'W':
        waypoint_horizontal -= distance
    else:
        rotations= distance/90
        if (direction == 'R' and rotations == 1) or (direction == 'L' and rotations == 3):
            waypoint_horizontal, waypoint_vertical = waypoint_vertical, -waypoint_horizontal
        elif rotations == 2:
            waypoint_horizontal = -waypoint_horizontal
            waypoint_vertical = - waypoint_vertical
        elif (direction == 'R' and rotations == 3) or (direction == 'L' and rotations == 1): 
            waypoint_horizontal, waypoint_vertical = -waypoint_vertical, waypoint_horizontal
print('part 2 manhattan distance', abs(horizontal_position) + abs(vertical_position))