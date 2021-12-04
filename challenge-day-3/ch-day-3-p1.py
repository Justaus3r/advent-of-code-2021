"""
Day 2 challenge part 1 rewritten cuz , first one got kabooom
"""

MAX_BIT_POSITION = 11
ON_BIT = "1"
OFF_BIT = "0"

current_bit_position = 0
on_bits = 0
off_bits = 0
most_common_bit = None
least_common_bit = None
final_gamma_rate_bits = ""
final_epsilon_rate_bits = ""

with open("input.txt") as f:
    data_list = [stained_element.strip() for stained_element in f.readlines()]

while current_bit_position <= MAX_BIT_POSITION:
    for element in data_list:
        if element[current_bit_position] == ON_BIT:
            on_bits += 1
        else:
            off_bits += 1
    most_common_bit = ON_BIT if on_bits > off_bits else OFF_BIT
    least_common_bit = ON_BIT if on_bits < off_bits else OFF_BIT
    final_gamma_rate_bits += most_common_bit
    final_epsilon_rate_bits += least_common_bit
    off_bits = 0
    on_bits = 0
    current_bit_position += 1

gamma_rate = int(final_gamma_rate_bits, 2)
epsilon_rate = int(final_epsilon_rate_bits, 2)
power_consumption = gamma_rate * epsilon_rate

if __name__ == "__main__":
    print(f"Gamma Rate: {gamma_rate}")
    print(f"Epsilon Rate: {epsilon_rate}")
    print(f"Power Consumption: {power_consumption}")
