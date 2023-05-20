import encoder_huffman_l1
import decoder_huffman_l1

file_name = 'example.txt'

l1_bin_file_suffix = 'encoded_l1_'
l2_bin_file_suffix = 'encoded_l2_'

l1_encoded_filename = l1_bin_file_suffix+file_name.split('.')[0]+'.bin'

encoded_data, codes = encoder_huffman_l1.huffman_encode(file_name)
decoded_data = decoder_huffman_l1.huffman_decode(encoded_data, codes)

print(encoded_data)
print(decoded_data)