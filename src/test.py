import level_1
import level_2
from pack_unpack import pack
from pack_unpack import unpack
import read_write

def compress():
	data, path = read_write.read_from_file()

	encoded_data_l1, codes_l1 = level_1.huffman_L1(data)
	encoded_data_l2, codes_l2 = level_2.huffman_L2(encoded_data_l1, 2)

	packed = pack(2, codes_l1, codes_l2, encoded_data_l2)


	read_write.write_to_raisin_file(path, packed)


def decompress():
    data, path = read_write.read_from_raisin_file()

    level, l1_codes, l2_codes, encoded_data = unpack(data)
    print(level)
    print(l1_codes)
    print(l2_codes)
    if level == 2:
        decoded_l2 = level_2.decode_L2(encoded_data, l2_codes)
        decoded_l1 = level_1.decode_L1(decoded_l2, l1_codes)
    else:
        decoded_l1 = level_1.decode_L1(encoded_data, l1_codes)
    print('Decoded L2: '+decoded_l2)
    print('Decoded L1: '+decoded_l1)

    read_write.write_to_file(path, decoded_l1)



opt = int(input('1. COMPRESS\n2. DECOMPRESS\n'))
if opt == 1: compress()
else: decompress()
