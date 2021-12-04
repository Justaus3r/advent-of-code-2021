"""
Aoc challenge day 3 part 2
"""

MAX_BIT_POSITION = 11
ON_BIT = "1"
OFF_BIT = "0"


current_bit_position = 0
on_bits = 0
off_bits = 0
most_common_bit = None
least_common_bit = None


with open("input.txt") as f:
    data_list = [stained_element.strip() for stained_element in f.readlines()]


def list_filterer(common_bit: str, curr_bit_position: int) -> None:
    global data_list
    temp_list = []
    for element in data_list:
        if element[curr_bit_position] == common_bit:
            temp_list.append(element)
    data_list = temp_list


data_list_copy = data_list


def rate_calculator(rate_type: str) -> int:
    """
    an ugly idea to change globals values in functions,xDD
    """
    global current_bit_position
    global most_common_bit
    global least_common_bit
    global data_list
    global on_bits
    global off_bits
    while current_bit_position <= MAX_BIT_POSITION:
        for element in data_list:
            if element[current_bit_position] == ON_BIT:
                on_bits += 1
            else:
                off_bits += 1
        most_common_bit = OFF_BIT if off_bits > on_bits else ON_BIT
        least_common_bit = ON_BIT if on_bits < off_bits else OFF_BIT
        on_bits = 0
        off_bits = 0

        rate = most_common_bit if rate_type == "oxygen-gen-rate" else least_common_bit
        list_filterer(rate, current_bit_position)
        current_bit_position += 1
        if len(data_list) == 1:
            result = int(data_list[0], 2)
            data_list = data_list_copy
            current_bit_position = 0
            return result


oxygen_generator_rate = rate_calculator("oxygen-gen-rate")
coc_sucrubber_rate = rate_calculator("coc-scrub-rate")


if __name__ == "__main__":
    print(f"Oxygen generator rate: {oxygen_generator_rate}")
    print(f"Coc Sucrubber rate: {coc_sucrubber_rate}")
    print(f"Life support Rate: {oxygen_generator_rate * coc_sucrubber_rate}")
