"""
Advent of code Day 1 challenge part 1 solved on day 2,xDD
"""

previous_figure = None
first_element_ignore = True
inc_countup = 0

with open("input.txt", "r") as file:
    for number in file:
        if first_element_ignore:
            first_element_ignore = False
            previous_figure = int(number)
            continue
        if int(number) > previous_figure:
            inc_countup += 1
        previous_figure = int(number)


if __name__ == "__main__":
    print(inc_countup)
