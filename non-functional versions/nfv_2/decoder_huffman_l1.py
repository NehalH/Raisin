def huffman_decode(encoded_data, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_data = ''
    current_code = ''
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data += reverse_codes[current_code]
            current_code = ''

    return decoded_data