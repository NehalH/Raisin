import heapq
import os
from collections import defaultdict

class Node:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.mid = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def encode(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    
    pq = []
    for char, f in freq.items():
        pq.append(Node(f, char))
    heapq.heapify(pq)
    
    # Handle special cases where there are fewer than 3 distinct characters in the input text
    if len(pq) == 0:
        return '', {}
    elif len(pq) == 1:
        huffman_table = {pq[0].char: '0'}
        encoded_text = ''.join(huffman_table[char] for char in text)
        return encoded_text, huffman_table
    
    while len(pq) > 1:
        left = heapq.heappop(pq)
        mid = heapq.heappop(pq) if len(pq) > 0 else None
        right = heapq.heappop(pq) if len(pq) > 0 else None
        parent = Node(left.freq + (mid.freq if mid is not None else 0) + (right.freq if right is not None else 0))
        parent.left = left
        parent.mid = mid
        parent.right = right
        heapq.heappush(pq, parent)
    
    huffman_table = {}
    def traverse(node, code=''):
        if node is None:
            return
        if node.char is not None:
            huffman_table[node.char] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.mid, code + '1')
            traverse(node.right, code + '2')

    traverse(pq[0])

    
    encoded_text = ''.join(huffman_table[char] for char in text)
    
    return encoded_text, huffman_table

def save_encoded_text(encoded_text, huffman_table, encoded_filename):
    with open(encoded_filename, 'wb') as f:
        # Write Huffman table
        for char, code in huffman_table.items():
            f.write(f'{char} {code}\n'.encode())

        # Write encoded text
        f.write(encoded_text.encode())



def read_encoded_text(encoded_filename):
    with open(encoded_filename, 'rb') as f:
        # Read Huffman table
        huffman_table = {}
        line = f.readline().decode('utf-8').strip()
        while line != '':
            char, code = line.split()
            huffman_table[char] = code
            line = f.readline().decode('utf-8').strip()

        # Read encoded text
        encoded_text = f.read()

    return encoded_text, huffman_table


def decode(encoded_text, huffman_table):
    inv_huffman_table = {v: k for k, v in huffman_table.items()}
    
    decoded_text = ''
    i = 0
    while i < len(encoded_text):
        code = ''
        while encoded_text[i] in '012':
            code += encoded_text[i]
            i += 1
        decoded_text += inv_huffman_table[code]
    
    return decoded_text

filename = 'example.txt'
encoded_filename = 'encoded_text.txt'

with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

encoded_text, huffman_table = encode(text)
save_encoded_text(encoded_text, huffman_table, encoded_filename)

text_size = os.path.getsize(filename)
encoded_text_size = os.path.getsize(encoded_filename)

print(f'Text size: {text_size} bytes')
print(f'Encoded text size: {encoded_text_size} bytes')
print(f'Percentage difference: {(text_size - encoded_text_size) / text_size * 100}%')
