import time


def part1(x):
    total = 0
    with open(x, "r") as f:
        for line in f.read().splitlines():
            print(line)
    return total
