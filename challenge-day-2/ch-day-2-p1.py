"""
Aoc 2nd day challenge
"""
from enum import Enum


horizontal_position = 0
depth = 0
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
        elif operation == Direction.UP.value:
            depth -= operand
        elif operation == Direction.DOWN.value:
            depth += operand

if __name__ == "__main__":
    print(f"The final horizontal position is {horizontal_position}")
    print(f"The final depth is {depth}")
    print(f"Product of horizontal position and depth is {horizontal_position*depth}")