"""
Aoc 2nd day challenge part 2
Basicaly just a slightly modified version of the first part
"""
from enum import Enum


horizontal_position = 0
depth = 0
aim = 0
parse_line = lambda line: [line.split()[0],int(line.split()[1])] # no need for list comprehension

class Direction(Enum):
    FORWARD = "forward"
    UP = "up"
    DOWN = "down"


with open('input.txt','r') as file:
    for line in file:
        operation,operand = parse_line(line)
        if operation == Direction.FORWARD.value:
            horizontal_position += operand
            depth += aim * operand
        elif operation == Direction.UP.value:
            aim -= operand
        elif operation == Direction.DOWN.value:
            aim += operand


if __name__ == "__main__":
    print(f"The final horizontal position is {horizontal_position}")
    print(f"The final depth is {depth}")
    print(f"The final aim is {aim}")
    print(f"Product of horizontal position and depth is {horizontal_position*depth}")