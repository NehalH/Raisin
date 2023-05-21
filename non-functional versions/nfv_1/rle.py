import os

def run_length_encoding(binary_file, output_file):
    with open(binary_file, 'rb') as f:
        data = f.read()
    encoded_size = len(data)
    with open(output_file, 'wb') as f:
        i = 0
        while i < encoded_size:
            count = 1
            while i + count < encoded_size and data[i + count] == data[i]:
                count += 1
            if count > 1:
                f.write(bytes([count, data[i]]))
            else:
                f.write(bytes([data[i]]))
            i += count

    # Calculate the percentage and magnitude of size compression
    original_size = os.path.getsize(binary_file)
    compressed_size = os.path.getsize(output_file)
    percentage_compression = (1 - compressed_size / original_size) * 100
    magnitude_compression = original_size / compressed_size

    print('RL encoding complete.')
    print('Percentage compression:', percentage_compression, '%')
    print('Original size:', original_size)
    print('Compressed size:', compressed_size)
    print('Magnitude compression:', magnitude_compression)
