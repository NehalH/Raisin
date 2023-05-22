
# ENCODER

import collections

class TreeNode:
    def __init__(self, chars, freq):
        self.chars = chars
        self.freq = freq
        self.left = None
        self.right = None

def build_huffman_tree(freq_table):
    queue = collections.deque(sorted(freq_table.items(), key=lambda x: x[1]))

    while len(queue) > 1:
        chars1, freq1 = queue.popleft()
        chars2, freq2 = queue.popleft()

        internal_node = TreeNode(None, freq1 + freq2)
        internal_node.left = chars1 if isinstance(chars1, TreeNode) else TreeNode(chars1, freq1)
        internal_node.right = chars2 if isinstance(chars2, TreeNode) else TreeNode(chars2, freq2)

        queue.append((internal_node, freq1 + freq2))
        queue = collections.deque(sorted(queue, key=lambda x: x[1]))

    return queue[0][0]

def traverse_huffman_tree(root, code, codes_dict):
    if root.chars is not None:
        codes_dict[root.chars] = code
    else:
        traverse_huffman_tree(root.left, code + "0", codes_dict)
        traverse_huffman_tree(root.right, code + "1", codes_dict)

def huffman_L2(bin_str):
    # Calculate character frequencies by considering two characters at a time
    freq_table = collections.Counter(bin_str[i:i+2] for i in range(0, len(bin_str), 2))

    # Build Huffman tree
    root = build_huffman_tree(freq_table)

    # Traverse Huffman tree and generate codes dictionary
    codes_dict = {}
    traverse_huffman_tree(root, "", codes_dict)

    # Encode the input binary string using Huffman codes
    encoded_str = "".join(codes_dict[bin_str[i:i+2]] for i in range(0, len(bin_str), 2))

    return encoded_str, codes_dict


# DECODER

def decode_L2(bin_str, codes_dict):
    reversed_codes_dict = {v: k for k, v in codes_dict.items()}
    decoded_str = ""
    curr_code = ""
    i = 0

    while i < len(bin_str):
        curr_code += bin_str[i]
        if curr_code in reversed_codes_dict:
            decoded_str += reversed_codes_dict[curr_code]
            curr_code = ""
        i += 1

    return decoded_str
