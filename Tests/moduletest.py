from collections import defaultdict
import random

def generate_level1_binary_huffman_code(length):
    random_string = ''.join(random.choice(['0', '1']) for _ in range(length))
    return random_string

def count_frequency(n, main_string):
    # Generate a list of n-character long strings from main_string
    string_list = [main_string[i:i+n] for i in range(0, len(main_string), n)]

    # Create a dictionary to count the frequency of each unique element
    frequency_dict = defaultdict(int)
    for string in string_list:
        frequency_dict[string] += 1

    return frequency_dict

# Example usage
n = 8
main_string = generate_level1_binary_huffman_code(999999)
frequency = count_frequency(n, main_string)
#print(main_string)
print(frequency)
