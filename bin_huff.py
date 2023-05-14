import heapq
import os
import rle

# Define a node class for the Huffman tree
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

# Define a function to build the Huffman tree
def build_tree(freq_dict):
    heap = []
    for char, freq in freq_dict.items():
        node = Node(freq, char)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(left.freq + right.freq, left.char + right.char, left, right)
        heapq.heappush(heap, parent)

    return heap[0]

# Define a function to generate the Huffman codes for each character
def generate_codes(node, code='', code_dict={}):
    if node.char:
        code_dict[node.char] = code
    if node.left:
        generate_codes(node.left, code + '0', code_dict)
    if node.right:
        generate_codes(node.right, code + '1', code_dict)
    return code_dict

# Define a function to encode a text file using Huffman encoding
def huffman_encode(file_path, binary_file_path):
    # Read the text file and build a frequency dictionary
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        freq_dict = {}
        for char in text:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1

    # Build the Huffman tree and generate the Huffman codes
    tree = build_tree(freq_dict)
    codes = generate_codes(tree)
    # Encode the text using the Huffman codes
    encoded_text = ''
    for char in text:
        encoded_text += codes[char]
    binary_data = int(encoded_text, 2).to_bytes((len(encoded_text) + 7) // 8, byteorder='big')
    
    # Write encoded data to file
    with open(binary_file_path, 'wb') as f:
        f.write(binary_data)

    # Calculate the percentage and magnitude of size compression
    original_size = os.path.getsize(file_path)
    compressed_size = os.path.getsize(binary_file_path)
    percentage_compression = (1 - compressed_size / original_size) * 100
    magnitude_compression = original_size / compressed_size

    return percentage_compression, original_size, compressed_size, magnitude_compression




source_file= 'example.txt'
huffen_bin_file= 'huffen_bin.txt'
rle_bin_file= 'rle_bin.bin'
percentage_compression, original_size, compressed_size, magnitude_compression = huffman_encode(source_file, huffen_bin_file)
print('////////')
print('Huffman encoding complete.')
print('Percentage compression:', percentage_compression, '%')
print('Original size:', original_size)
print('Compressed size:', compressed_size)
print('Magnitude compression:', magnitude_compression)
print('////////')
'''
rle.run_length_encoding(huffen_bin_file, rle_bin_file)
print('////////')
'''