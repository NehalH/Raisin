from tqdm import tqdm

# ENCODER

import collections
import heapq

class TreeNode:
    def __init__(self, chars, freq):
        self.chars = chars
        self.freq = freq
        self.left = None
        self.right = None

def build_huffman_tree(freq_table):
    priority_queue = []

    # Create tuples with negative frequencies to sort in reverse order
    for chars, freq in freq_table.items():
        heapq.heappush(priority_queue, (freq, TreeNode(chars, freq)))

    while len(priority_queue) > 1:
        # Pop two nodes with the highest frequencies
        neg_freq1, node1 = heapq.heappop(priority_queue)
        neg_freq2, node2 = heapq.heappop(priority_queue)

        # Create a new internal node with the sum of frequencies
        internal_node = TreeNode(None, node1.freq + node2.freq)
        internal_node.left = node1
        internal_node.right = node2

        # Push the new internal node back to the priority queue
        heapq.heappush(priority_queue, (-internal_node.freq, internal_node))

    # Return the root node of the Huffman tree
    return priority_queue[0][1]


def traverse_huffman_tree(root, code, codes_dict):
    if root.chars is not None:
        codes_dict[root.chars] = code
    else:
        traverse_huffman_tree(root.left, code + "0", codes_dict)
        traverse_huffman_tree(root.right, code + "1", codes_dict)

def dictionary_to_string(dictionary):
    pairs = []
    for key, value in dictionary.items():
        pairs.append(f"'{key}'::{value}")
    return ',,'.join(pairs)

def huffman_L2(bin_str, n):
    # Calculate character frequencies by considering n characters at a time
    freq_table = collections.Counter(bin_str[i:i+n] for i in range(0, len(bin_str), n))
    print('\n\n\n',freq_table,'\n\n\n')
    # Build Huffman tree
    root = build_huffman_tree(freq_table)

    # Traverse Huffman tree and generate codes dictionary
    codes_dict = {}
    traverse_huffman_tree(root, "", codes_dict)

    # Encode the input binary string using Huffman codes
    encoded_str = ""
    progress_bar = tqdm(total=len(bin_str), desc="Compressing (Level 2)")

    for i in range(0, len(bin_str), n):
        chunk = bin_str[i:i+n]
        encoded_str += codes_dict[chunk]
        progress_bar.update(len(chunk))

    progress_bar.close()

    print('\n\n\n',codes_dict,'\n\n\n')

    return encoded_str, codes_dict, len(encoded_str), len(dictionary_to_string(codes_dict))



# DECODER

def decode_L2(bin_str, codes_dict):
    reversed_codes_dict = {v: k for k, v in codes_dict.items()}
    decoded_str = ""
    curr_code = ""
    i = 0

    progress_bar = tqdm(total=len(bin_str), desc="Decompressing (Level 1)")

    while i < len(bin_str):
        curr_code += bin_str[i]
        if curr_code in reversed_codes_dict:
            decoded_str += reversed_codes_dict[curr_code]
            curr_code = ""
        i += 1
        progress_bar.update()

    progress_bar.close()

    return decoded_str
