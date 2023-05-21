import encoder_huffman_l1
import encoder_huffman_l2
import decoder_huffman_l1
import decoder_huffman_l2
import efficiency_calculator
from rich import print
import sys

file_name = 'example_short.txt'
#file_name = 'example.txt'
#file_name = 'example_large.txt'

bit_group = 2

# L1 encode
encoded_data_l1, codes_l1 = encoder_huffman_l1.huffman_encode(file_name)

# L2 encode
encoded_data_l2, codes_l2, bit_group, compressed_size_l2 = encoder_huffman_l2.huffman_encode_l2(encoded_data_l1, codes_l1)
#encoded_data_l2, codes_l2 = encoder_huffman_l2.huffman_encode(encoded_data_l1, bit_group)

# L2 decode
decoded_data_l2 = decoder_huffman_l2.huffman_decode_l2(encoded_data_l2, codes_l2)

# L1 decode
decoded_data_l1 = decoder_huffman_l1.huffman_decode(decoded_data_l2, codes_l1)


efficiency_calculator.calcu_efficiency(file_name, encoded_data_l1, codes_l1)
efficiency_calculator.print_efficiency_for_l2(encoded_data_l1, codes_l1, compressed_size_l2)

#print(codes_l2)

print('BIT GROUP :', bit_group)
with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()

if text == decoded_data_l1:
	print('SUCCESSFUL')
print(text,'\n',decoded_data_l1)