def huffman_decode_l2(encoded_data, codes):
    reverse_codes = {v: k for k, v in codes.items()}

    decoded_data = ""
    current_chunk = ""
    for bit in encoded_data:
        current_chunk += bit
        if current_chunk in reverse_codes:
            decoded_data += reverse_codes[current_chunk]
            current_chunk = ""

    return decoded_data
