
# All this is bullshit
# A waste of time

import random
import string

def create_random_dictionary(n):
    dictionary = {}
    chars = string.ascii_lowercase + string.ascii_uppercase
    
    for _ in range(n):
        key = random.choice(chars)
        value = random.randint(1, 999999999)
        dictionary[key] = value
    
    return dictionary

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
    frequencies, levels = sort_lists(frequencies, levels)
    return frequencies, levels

def traverse_tree(node, code, characters, frequencies, levels, level):
    if node.char:
        characters.append(node.char)
        frequencies.append(node.freq)
        levels.append(level)
    else:
        traverse_tree(node.left, code + '0', characters, frequencies, levels, level + 1)
        traverse_tree(node.right, code + '1', characters, frequencies, levels, level + 1)

def solve(bits, frequencies, levels):
    size = 0
    for i in range(len(frequencies)):
        size += frequencies[i]*(levels[i]-1)*bits
    #print(f'{size},\n{frequencies},\n{levels},\n{bits}\n\n')
    return size

def find_opt_bits(frequencies, levels):
    opt_bits = 2;
    opt_size = solve(opt_bits, frequencies, levels)
    for i in range(opt_bits+1,9):
        size = solve(i, frequencies, levels)
        if size <= opt_size:
            opt_bits = i
            opt_size = size

    return opt_bits, opt_size

def sort_lists(list1, list2):
    zipped = zip(list1, list2)  # Zip the two lists together
    sorted_lists = sorted(zipped)  # Sort the zipped lists based on the first list
    sorted_list1, sorted_list2 = zip(*sorted_lists)  # Unzip the sorted lists
    
    return list(sorted_list1), list(sorted_list2)

def compare_size(frequencies, opt_size, opt_bits):
    original_size = 0
    for i in frequencies:
        original_size += i * opt_bits
    if(original_size>=opt_size):
        return True
    else:
        return False


iterations = 1000
success_count = 0
fail_count = 0
for _ in range(iterations):
    frequencies, levels = create_huffman_tree(create_random_dictionary(1000))
    opt_bits, opt_size = find_opt_bits(frequencies, levels)
    if compare_size(frequencies, opt_size, opt_bits):
        success_count += 1
    else:
        fail_count += 1
    if(opt_bits!=2):
        print(opt_bits)

print('SUCCESS : ',success_count)
print('FAIL : ',fail_count)
print('Success rate : ',success_count*100/iterations,'%')    
print("END")