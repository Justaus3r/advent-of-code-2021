"""
Advent of code Day 1 challenge part 2
"""

element_one_index = 0
element_two_index = 1
element_three_index = 2
not_exhausted = True
first_element_ignore = True
sum_list = []
inc_countup = 0

with open("input.txt") as file:
    element_list = [int(stained_element.strip()) for stained_element in file.readlines()]


while not_exhausted:
    try:
        sum_list.append(element_list[element_one_index] + element_list[element_two_index] + element_list[element_three_index])            
        element_one_index += 1
        element_two_index += 1
        element_three_index += 1
    except IndexError:
        not_exhausted = False

for idx ,_ in enumerate(sum_list):
    if sum_list[idx] == 0:
        continue
    try:
        if sum_list[idx] < sum_list[idx + 1]:
            inc_countup += 1
    except IndexError:
        pass

if __name__ == "__main__":
    print(sum_list)
    print(inc_countup)