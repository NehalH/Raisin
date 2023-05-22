import level_1
import level_2
from pack_unpack import pack
from pack_unpack import unpack
import read_write

data = 'Helllllooooo Worrrlllddd, I am Nehalll.\nThis is Reeeeeeddddduuunnnndaaaanncccccccyyyyyy.'
path = './example_short.txt'

encoded_data_l1, codes_l1 = level_1.huffman_L1(data)
encoded_data_l2, codes_l2 = level_2.huffman_L2(encoded_data_l1)

#decoded_l2 = level_2.decode_L2(encoded_data_l2, codes_l2)
#decoded_l1 = level_1.decode_L1(decoded_l2, codes_l1)

#print(decoded_l1)
#if decoded_l1 == data: print('SUCCESS')

packed = pack(2, codes_l1, codes_l2, encoded_data_l2)
read_write.write_to_compressed_file(path, packed)
