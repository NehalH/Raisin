import os

files = ['example.txt','huffen_bin.txt', 'l2_huffen_bin.txt', 'l3_huffen_bin.txt']
print('=========================================')
for i in range(len(files)-1):
	original_size = os.path.getsize(files[i])
	compressed_size = os.path.getsize(files[i+1])
	print('Original file size : ', original_size)
	print('Compressed file size : ', compressed_size)
	print('Size difference : ', original_size - compressed_size)	
	print('Percentage compression:', (1 - compressed_size / original_size) * 100, '%')
	print('Magnitude compression:', original_size / compressed_size)
	print('=========================================')
print('=========================================')
print('Overall:')
original_size = os.path.getsize(files[0])
compressed_size = os.path.getsize(files[-1])
print('Original file size : ', original_size)
print('Compressed file size : ', compressed_size)
print('Size difference : ', original_size - compressed_size)	
print('Percentage compression:', (1 - compressed_size / original_size) * 100, '%')
print('Magnitude compression:', original_size / compressed_size)
print('=========================================')