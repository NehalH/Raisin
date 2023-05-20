def calcu_efficiency(original_file, compressed_data):
	original_size = os.path.getsize(original_file)
	compressed_size = len(compressed_data)

	print('=========================================')
	print('Original file size : ', original_size)
	print('Compressed file size : ', compressed_size)
	print('Size difference : ', original_size - compressed_size)	
	print('Percentage compression:', (1 - compressed_size / original_size) * 100, '%')
	print('Magnitude compression:', original_size / compressed_size)
	print('=========================================')

	if original_size > compressed_size:
		return True
	
	return False