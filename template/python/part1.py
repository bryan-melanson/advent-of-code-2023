import time


def part1(x):
    with open(x, "r") as f:
        return f.read().splitlines()


test_val = 0
if part1("test1") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part1("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
