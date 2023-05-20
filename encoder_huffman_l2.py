class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

def build_tree(freq_dict):
    nodes = [Node(freq, char) for char, freq in freq_dict.items()]

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node(left.freq + right.freq, None, left, right)
        nodes.append(parent)

    return nodes[0]

def generate_codes(node, code='', code_dict={}):
    if node.char:
        code_dict[node.char] = code
    if node.left:
        generate_codes(node.left, code + '0', code_dict)
    if node.right:
        generate_codes(node.right, code + '1', code_dict)
    return code_dict

def huffman_encode_l2(encoded_data, n):
    freq_dict = {}
    for i in range(0, len(encoded_data), n):
        group = encoded_data[i:i+n]
        if group in freq_dict:
            freq_dict[group] += 1
        else:
            freq_dict[group] = 1

    tree = build_tree(freq_dict)
    codes = generate_codes(tree)

    n_bit_encoded_data = ''
    for i in range(0, len(encoded_data), n):
        group = encoded_data[i:i+n]
        n_bit_encoded_data += codes[group]

    return n_bit_encoded_data, codes
