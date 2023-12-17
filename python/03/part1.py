def is_valid(char):
    if char != "." and not char.isnumeric():
        return True
    return False


def check_neighbors(schema, x, y, max_x, max_y):
    check_left = x > 0
    check_right = x < max_x
    check_up = y > 0
    check_down = y < max_y
    valid = False
    if (check_left):
        if is_valid(schema[y][x-1]):
            valid = True
            pass
    if (check_down):
        if is_valid(schema[y+1][x]):
            valid = True
            pass
        if (check_left):
            if is_valid(schema[y+1][x-1]):
                valid = True
                pass
        if (check_right):
            if is_valid(schema[y+1][x+1]):
                valid = True
                pass
    if (check_right):
        if is_valid(schema[y][x+1]):
            valid = True
            pass
    if (check_up):
        if is_valid(schema[y-1][x]):
            valid = True
            pass
        if (check_left):
            if is_valid(schema[y-1][x-1]):
                valid = True
                pass
        if (check_right):
            if is_valid(schema[y-1][x+1]):
                valid = True
                pass
    return valid

def part1(x):
    total = 0
    with open(x, "r") as f:
        schematics = [list(line.strip()) for line in f]
        len_y = len(schematics)
        len_x = len(schematics[0])
        max_x = len_x-1
        max_y = len_y-1
        valid = True
        for y in range(len_y):
            digit = ''
            valid = False
            for x in range(len_x):
                current = schematics[y][x]
                if valid and current.isnumeric():
                    digit += current
                elif current.isnumeric() and not valid:
                    digit += current
                    valid = check_neighbors(schematics, x, y, max_x, max_y)
                elif not current.isnumeric() and valid:
                    total += int(digit)
                    digit = ''
                    valid = False
                else:
                    valid = False
                    digit = ''
                if x == (len_x-1) and valid:
                    total += int(digit)
                    digit = ''
    return total