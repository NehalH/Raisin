import encoder_huffman_l1
import encoder_huffman_l2
import decoder_huffman_l1
import decoder_huffman_l2
import efficiency_calculator

file_name = 'example.txt'
#file_name = 'example_large.txt'
bit_group = 2

# L1 encode
encoded_data_l1, codes_l1 = encoder_huffman_l1.huffman_encode(file_name)

# L2 encode
encoded_data_l2, codes_l2 = encoder_huffman_l2.huffman_encode_l2(encoded_data_l1, bit_group)

# L2 decode
decoded_data_l2 = decoder_huffman_l2.huffman_decode_two_chars(encoded_data_l2, codes_l2)

# L1 decode
decoded_data_l1 = decoder_huffman_l1.huffman_decode(decoded_data_l2, codes_l1)


#efficiency_calculator.calcu_efficiency(file_name, encoded_data_l1, codes_l1)
efficiency_calculator.calcu_efficiency_for_l2(encoded_data_l1, encoded_data_l2, codes_l1, codes_l2)

#print(codes_l2)

with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()

if text == decoded_data_l1:
	print('SUCCESSFUL')