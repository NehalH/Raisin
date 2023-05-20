import encoder_huffman_l1
import decoder_huffman_l1
import efficiency_calculator

file_name = 'example.txt'

encoded_data, codes = encoder_huffman_l1.huffman_encode(file_name)
decoded_data = decoder_huffman_l1.huffman_decode(encoded_data, codes)

efficiency_calculator.calcu_efficiency(file_name, decoded_data)
