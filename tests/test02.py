import random
import string

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

###############################
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

###############################
def create_random_dictionary(n):
    dictionary = {}
    chars = string.ascii_lowercase + string.ascii_uppercase
    
    for _ in range(n):
        key = random.choice(chars)
        value = random.randint(1, 200)
        dictionary[key] = value
    
    return dictionary

###############################
def sort_lists(list1, list2):
    zipped = zip(list1, list2)  # Zip the two lists together
    sorted_lists = sorted(zipped)  # Sort the zipped lists based on the first list
    sorted_list1, sorted_list2 = zip(*sorted_lists)  # Unzip the sorted lists
    
    return list(sorted_list1), list(sorted_list2)

##############################
def find_ratios(list1):
    list2 = []
    for i in range(len(list1)-1):
        list2.append(round(list1[i]/list1[i+1],2))
    return list2

for _ in range(20):
    list1, list2 =create_huffman_tree(create_random_dictionary(10))
    l1,l2 = sort_lists(list1, list2)
    print(l1)
    #print(l2)
    print(find_ratios(l1))