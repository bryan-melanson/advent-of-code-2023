def is_gear(char):
    if char != "." and not char.isnumeric():
        if char == '*':
            return True
    return False


def check_neighbors(schema, x, y, max_x, max_y):
    check_left = x > 0
    check_right = x < max_x
    check_up = y > 0
    check_down = y < max_y
    valid = False
    if (check_left):
        if is_gear(schema[y][x-1]):
            valid = True
            pass
    if (check_down):
        if is_gear(schema[y+1][x]):
            valid = True
            pass
        if (check_left):
            if is_gear(schema[y+1][x-1]):
                valid = True
                pass
        if (check_right):
            if is_gear(schema[y+1][x+1]):
                valid = True
                pass
    if (check_right):
        if is_gear(schema[y][x+1]):
            valid = True
            pass
    if (check_up):
        if is_gear(schema[y-1][x]):
            valid = True
            pass
        if (check_left):
            if is_gear(schema[y-1][x-1]):
                valid = True
                pass
        if (check_right):
            if is_gear(schema[y-1][x+1]):
                valid = True
                pass
    return valid


def part2(x):
    total = 0
    with open(x, "r") as f:
        schematics = [list(line.strip()) for line in f]
        len_y = len(schematics)
        len_x = len(schematics[0])
        max_x = len_x-1
        max_y = len_y-1
        valid = True
        for y in range(len_y):
            gears = {'first': '', 'second': '', '*': 0}
            temp1 = 0
            temp2 = 0
    return total
