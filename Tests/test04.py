import random
from collections import defaultdict

# Generate binary string of length length
def generate_level1_binary_huffman_code(length):
    random_string = ''.join(random.choice(['0', '1']) for _ in range(length))
    return random_string

# Return dict { n-bit numbers : fr }
def count_frequency(n, main_string):
    # Generate a list of n-character long strings from main_string
    string_list = [main_string[i:i+n] for i in range(0, len(main_string), n)]

    # Create a dictionary to count the frequency of each unique element
    frequency_dict = defaultdict(int)
    for string in string_list:
        frequency_dict[string] += 1

    return frequency_dict

# Class for Huffman Tree Node
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def create_huffman_tree(dictionary):
    # Convert the dictionary into a list of nodes
    nodes = [Node(char, freq) for char, freq in dictionary.items()]

    while len(nodes) > 1:
        # Sort the nodes based on their frequency in ascending order
        nodes.sort(key=lambda x: x.freq)
        # Create a new parent node with the two nodes with the lowest frequencies
        parent = Node(None, nodes[0].freq + nodes[1].freq)
        parent.left = nodes.pop(0)
        parent.right = nodes.pop(0)
        # Add the parent node to the list of nodes
        nodes.append(parent)

    # Traverse the tree and collect the characters, frequencies, and levels
    characters = []
    frequencies = []
    levels = []
    traverse_tree(nodes[0], '', characters, frequencies, levels, 0)
    return frequencies, levels

def traverse_tree(node, code, characters, frequencies, levels, level):
    if node.char:
        characters.append(node.char)
        frequencies.append(node.freq)
        levels.append(level)
    else:
        traverse_tree(node.left, code + '0', characters, frequencies, levels, level + 1)
        traverse_tree(node.right, code + '1', characters, frequencies, levels, level + 1)

def find_opt_bit_group(binary_data_l1, data_length_l1, min_bit_group, max_bit_group):
    opt_size = data_length_l1
    opt_bit_group = 1
    for i in range(min_bit_group, max_bit_group+1):
        frequency_dict = count_frequency(i, binary_data_l1)
        frequencies, levels = create_huffman_tree(frequency_dict)
        size = find_size(opt_size, frequencies, levels)
        if opt_size > size:
            opt_size = size
            opt_bit_group = i

    return opt_bit_group, opt_size

def find_size(frequencies, levels):
    size = 0
    for i in range(len(frequencies)):
        size += frequencies[i]*(levels[i]-1)

    return size    



###############################################################################

data_length_l1 = 1000
min_bit_group = 2
max_bit_group = 8

for _ in range(10):
    binary_data_l1 = generate_level1_binary_huffman_code(data_length_l1)
    opt_bit_group = find_opt_bit_group(binary_data_l1, data_length_l1, min_bit_group, max_bit_group)

    print(frequencies)
    print(levels)
    print(opt_bit_group)