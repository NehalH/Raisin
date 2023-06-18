import level_1
import level_2
from pack_unpack import pack
from pack_unpack import unpack
import read_write

# quick_test_data = 'Helllllooooo Worrrlllddd, I am Nehalll. This is Reeeeeeddddduuunnnndaaaanncccccccyyyyyy.'
# path = '../test_subject/example.txt'

# with open(path, 'r', encoding='utf-8') as file:
#     file_data = file.read()

data, path = read_write.read_from_file()

encoded_data_l1, codes_l1 = level_1.huffman_L1(data)
encoded_data_l2, codes_l2 = level_2.huffman_L2(encoded_data_l1, 2)

packed = pack(2, codes_l1, codes_l2, encoded_data_l2)


read_write.write_to_compressed_file(path, packed)


############################################################

# level, l1_codes, l2_codes, encoded_data = unpack(packed)

# if level==2:
# 	decoded_l2 = level_2.decode_L2(encoded_data_l2, codes_l2)
# 	decoded_l1 = level_1.decode_L1(decoded_l2, codes_l1)
# else:
# 	decoded_l1 = level_1.decode_L1(encoded_data, codes_l1)

# if decoded_l1 == data:
# 	print('SUCCESS')
