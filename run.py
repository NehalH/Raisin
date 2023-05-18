import l1_huffman_encoder
import l1_frequency_generator

file_name = 'example.txt'

character_frequencies = l1_frequency_generator.get_character_frequencies(file_name)
encoded_data = l1_huffman_encoder.huffman_encode(character_frequencies)

print("Encoded data:", encoded_data)