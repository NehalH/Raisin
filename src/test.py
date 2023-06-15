import level_1
import level_2
from pack_unpack import pack
from pack_unpack import unpack
import read_write

quick_test_data = 'Helllllooooo Worrrlllddd, I am Nehalll. This is Reeeeeeddddduuunnnndaaaanncccccccyyyyyy.'
path = '../test_subject/example.txt'

with open(path, 'r', encoding='utf-8') as file:
    file_data = file.read()

data = file_data

encoded_data_l1, codes_l1 = level_1.huffman_L1(data)
encoded_data_l2, codes_l2 = level_2.huffman_L2(encoded_data_l1, 2)

# decoded_l2 = level_2.decode_L2(encoded_data_l2, codes_l2)
# decoded_l1 = level_1.decode_L1(decoded_l2, codes_l1)

# print(decoded_l1)
# if decoded_l1 == data: print('SUCCESS')

packed = pack(2, codes_l1, codes_l2, encoded_data_l2)
level, l1_codes, l2_codes, encoded_data = unpack(packed)

if level==2:
	decoded_l2 = level_2.decode_L2(encoded_data_l2, codes_l2)
	decoded_l1 = level_1.decode_L1(decoded_l2, codes_l1)
else:
	decoded_l1 = level_1.decode_L1(encoded_data, codes_l1)

if decoded_l1 == data:
	print('SUCCESS')

# print(data)
# print(packed)
# read_write.write_to_compressed_file(path, packed)

# print(len(data)-len(packed))
# print((len(data)-len(packed))*100/len(data))
# print(len(encoded_data_l1)-len(encoded_data_l2))
# print((len(encoded_data_l1)-len(encoded_data_l2))*100/len(encoded_data_l1))