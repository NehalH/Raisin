
# ENCODER

import collections

class TreeNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_huffman_tree(freq_table):
    queue = collections.deque(sorted(freq_table.items(), key=lambda x: x[1]))

    while len(queue) > 1:
        char1, freq1 = queue.popleft()
        char2, freq2 = queue.popleft()

        internal_node = TreeNode(None, freq1 + freq2)
        internal_node.left = char1 if isinstance(char1, TreeNode) else TreeNode(char1, freq1)
        internal_node.right = char2 if isinstance(char2, TreeNode) else TreeNode(char2, freq2)

        queue.append((internal_node, freq1 + freq2))
        queue = collections.deque(sorted(queue, key=lambda x: x[1]))

    return queue[0][0]

def traverse_huffman_tree(root, code, codes_dict):
    if root.char is not None:
        codes_dict[root.char] = code
    else:
        traverse_huffman_tree(root.left, code + "0", codes_dict)
        traverse_huffman_tree(root.right, code + "1", codes_dict)

def huffman_L1(string):
    # Calculate character frequencies
    freq_table = collections.Counter(string)

    # Build Huffman tree
    root = build_huffman_tree(freq_table)

    # Traverse Huffman tree and generate codes dictionary
    codes_dict = {}
    traverse_huffman_tree(root, "", codes_dict)

    # Compress the input string using Huffman codes
    compressed_string = "".join(codes_dict[char] for char in string)

    return compressed_string, codes_dict


# DECODER

def decode_L1(bin_str, codes_dict):
    reversed_codes_dict = {v: k for k, v in codes_dict.items()}
    decoded_str = ""
    curr_code = ""
  
    for bit in bin_str:
        curr_code += bit
        if curr_code in reversed_codes_dict:
            decoded_str += reversed_codes_dict[curr_code]
            curr_code = ""

    return decoded_str
    