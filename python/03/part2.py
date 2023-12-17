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
    vals = (-1, -1)
    if (check_left):
        if is_gear(schema[y][x-1]):
            vals = (y, x-1)
            pass
    if (check_down):
        if is_gear(schema[y+1][x]):
            vals = (y+1, x)
            pass
        if (check_left):
            if is_gear(schema[y+1][x-1]):
                vals = (y+1, x-1)
                pass
        if (check_right):
            if is_gear(schema[y+1][x+1]):
                vals = (y+1, x+1)
                pass
    if (check_right):
        if is_gear(schema[y][x+1]):
            vals = (y, x+1)
            pass
    if (check_up):
        if is_gear(schema[y-1][x]):
            vals = (y-1, x)
            pass
        if (check_left):
            if is_gear(schema[y-1][x-1]):
                vals = (y-1, x-1)
                pass
        if (check_right):
            if is_gear(schema[y-1][x+1]):
                vals = (y-1, x+1)
                pass
    return vals


def part2(x):
    total = 0
    with open(x, "r") as f:
        schematics = [list(line.strip()) for line in f]
        len_y = len(schematics)
        len_x = len(schematics[0])
        max_x = len_x-1
        max_y = len_y-1
        valid = True
        gears = {}
        for row in range(len_y):
            number = ''
            gear_count = 0
            gear_loc = (-1, -1)
            gears_found = {}
            for col in range(len_x):
                char = schematics[row][col]
                if char.isnumeric():
                    number += char
                    if gear_count > 1:
                        valid = False
                    else:
                        gear_loc = check_neighbors(
                            schematics, col, row, max_x, max_y)
                        if gear_loc != (-1, -1):
                            valid = True
                    if valid and gear_loc != (-1, -1) and not gear_loc in gears_found:
                        gear_count += 1
                        gears_found[gear_loc] = 1
                else:
                    if number != '' and valid:
                        gears[number] = gear_loc
                        gear_loc = (-1, -1)
                    number = ''
        print(gears)
    return total


if __name__ == "__main__":
    part2('data/test2')
