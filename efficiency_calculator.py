import os
import sys

def calcu_efficiency(original_file, compressed_data, codes_l1):
	dictionary_string = str(codes_l1)
	dict_size = sys.getsizeof(dictionary_string)
	original_size = os.path.getsize(original_file)
	compressed_size = (len(compressed_data)/8)+dict_size

	print('=========================================')
	print('Original file size : ', original_size)
	print('Compressed file size : ', compressed_size)
	print('Dictionary size : ', dict_size)
	print('Size difference : ', original_size - compressed_size)	
	print('Percentage compression:', (1 - compressed_size / original_size) * 100, '%')
	print('Magnitude compression:', original_size / compressed_size)
	print('=========================================')

	if original_size > compressed_size:
		return True

	return False

def calcu_efficiency_for_l2(original_data, compressed_data, codes_l1, codes_l2):
	dictionary1_string = str(codes_l1)
	dict1_size = sys.getsizeof(dictionary1_string)
	dictionary2_string = str(codes_l2)
	dict2_size = sys.getsizeof(dictionary2_string)
	original_size = (len(original_data)/8)+dict1_size
	compressed_size = (len(compressed_data)/8)+dict2_size

	print('=========================================')
	print('Original file size : ', original_size)
	print('Compressed file size : ', compressed_size)
	print('Dictionary size : ', dict2_size)
	print('Size difference : ', original_size - compressed_size)	
	print('Percentage compression:', (1 - compressed_size / original_size) * 100, '%')
	print('Magnitude compression:', original_size / compressed_size)
	print('=========================================')

	if original_size > compressed_size:
		return True

	return False