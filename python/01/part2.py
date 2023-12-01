import time
import re

'''
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
'''

def find_number(line, nums):
    for i in range(len(line)):
        if '0' <= line[i] <= '9':
            return line[i]
        for j in range(len(nums)):
            if line.startswith(nums[j], i):
                c = j + 1 + ord('0')
                return nums[c]

def part2(x):
    with open(x, "r") as f:
        total = 0
        numbers = {
            "one": 1, 
            "two": 2, 
            "three": 3, 
            "four": 4, 
            "five": 5, 
            "six": 6, 
            "seven": 7, 
            "eight": 8, 
            "nine": 9
        }   
        for line in f.read().splitlines():
            number = 0
            c = find_number(line, numbers)
            number += int(c) * 10
            line = line[::-1]
            c = find_number(line, [s[::-1] for s in numbers])
            number += c
            total += number
    return total

# --- 0.0035772323608398438 seconds ---

test_val = 281
if part2("test2") == test_val:
    start_time = time.time()
    print('Solution is {}'.format(part2("input")))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Test failed")
