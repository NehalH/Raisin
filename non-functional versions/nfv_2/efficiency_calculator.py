import os
import sys
from rich import print

def calcu_efficiency(original_file, compressed_data, codes_l1):
	dict_size = sys.getsizeof(codes_l1)
	original_size = os.path.getsize(original_file)
	compressed_size = (len(compressed_data)/8)+dict_size

	print('=========================================')
	print('Original file size \t:\t ', original_size)
	print('Compressed file size \t:\t ', compressed_size)
	print('Dictionary size \t:\t ', dict_size)
	print('Size difference \t:\t ', original_size - compressed_size)	
	print('Percentage compression \t:\t ', (1 - compressed_size / original_size) * 100, '%')
	print('Magnitude compression \t:\t ', original_size / compressed_size)
	print('=========================================')

	if original_size > compressed_size:
		return True

	return False

def calcu_efficiency_for_l2(original_data, compressed_data, codes_l1, codes_l2):
    dict1_size = sys.getsizeof(codes_l1)
    dict2_size = sys.getsizeof(codes_l2)
    original_size = (len(original_data) / 8) + dict1_size
    compressed_size = (len(compressed_data) / 8) + dict2_size
    '''
    print('=========================================')
    print('Original file size \t:\t ', original_size)
    print('Compressed file size \t:\t ', compressed_size)
    print('Dictionary size \t:\t ', dict2_size)
    print('Size difference \t:\t ', original_size - compressed_size)
    print('Percentage compression \t:\t ', (1 - compressed_size / original_size) * 100, '%')
    print('Magnitude compression \t:\t ', original_size / compressed_size)
    print('=========================================')
    '''
    if original_size > compressed_size:
        return compressed_size

    return original_size

def print_efficiency_for_l2(original_data, codes_l1, compressed_size):
    dict1_size = sys.getsizeof(codes_l1)
    original_size = (len(original_data) / 8) + dict1_size

    print('=========================================')
    print('Original file size \t:\t ', original_size)
    print('Compressed file size \t:\t ', compressed_size)
    print('Size difference \t:\t ', original_size - compressed_size)
    print('Percentage compression \t:\t ', (1 - compressed_size / original_size) * 100, '%')
    print('Magnitude compression \t:\t ', original_size / compressed_size)
    print('=========================================')

    if original_size > compressed_size:
        return compressed_size

    return original_size