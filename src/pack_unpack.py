
# PACK

def dictionary_to_string(dictionary):
    pairs = []
    for key, value in dictionary.items():
        pairs.append(f"'{key}'::{value}")
    return ',,'.join(pairs)

def data_padding(binary_str):
    padding = 8 - len(binary_str) % 8
    for i in range(padding):
        binary_str += "0"
    return padding, binary_str

def bits_to_byte_array(bit_string):
    byte_array = bytearray()
    for i in range(0, len(bit_string), 8):
        byte = bit_string[i:i+8]
        byte_array.append(int(byte, 2))
    return byte_array

def pack(level, codes_l1, codes_l2, encoded_data):
    padding, encoded_data = data_padding(encoded_data)
    encoded_data = bits_to_byte_array(encoded_data)
    l1_codes_string = dictionary_to_string(codes_l1)
    l2_codes_string = dictionary_to_string(codes_l2)

    meta_data = str(level) + '|' + str(padding) + '|' + str(len(l1_codes_string)) + '|' + str(len(l2_codes_string)) + '|' + l1_codes_string + l2_codes_string
    packed_data =  bytes(meta_data, 'utf-8') + encoded_data
    
    return packed_data

# UNPACK

def string_to_dictionary(string):
    dictionary = {}
    key_value_pairs = string.split(',,')

    for pair in key_value_pairs:
        if '::' in pair:
            key, value = pair.split('::')
            if key == "'''":
                key = "'"
            else:
                key = key.strip().strip('\'')
            value = value.strip().strip('\'')
            dictionary[key] = value

    return dictionary

def byte_array_to_bits(byte_array):
    bit_string = ""
    for byte in byte_array:
        # Convert the byte to its binary representation
        byte_bits = bin(byte)[2:].zfill(8)
        bit_string += byte_bits
    return bit_string

def unpack(packed_data):
    level = ""
    padding = ""
    l1_codes_len = ""
    l2_codes_len = ""
    l1_codes = ""
    l2_codes = ""
    i = 0

    # extract level
    while i < len(packed_data):
        char = packed_data[i]
        if char != ord(b'|'):
            level += chr(char)
        else:
            break
        i += 1
    packed_data = packed_data[i+1:]
    i = 0

    # extract padding
    while i < len(packed_data):
        char = packed_data[i]
        if char != ord(b'|'):
            padding += chr(char)
        else:
            break
        i += 1
    packed_data = packed_data[i+1:]
    i = 0

    # extract l1_codes_len
    while i < len(packed_data):
        char = packed_data[i]
        if char != ord(b'|'):
            l1_codes_len += chr(char)
        else:
            break
        i += 1
    packed_data = packed_data[i+1:]
    i = 0

    # extract l2_codes_len
    while i < len(packed_data):
        char = packed_data[i]
        if char != ord(b'|'):
            l2_codes_len += chr(char)
        else:
            break
        i += 1
    packed_data = packed_data[i+1:]

    level = int(level)
    padding = int(padding)
    l1_codes_len = int(l1_codes_len)
    l2_codes_len = int(l2_codes_len)

    l1_codes = packed_data[:l1_codes_len].decode('utf-8')
    packed_data = packed_data[l1_codes_len:]
    l2_codes = packed_data[:l2_codes_len].decode('utf-8')
    packed_data = packed_data[l2_codes_len:]
    encoded_data = byte_array_to_bits(bytearray(packed_data))

    l1_codes = string_to_dictionary(l1_codes)
    l2_codes = string_to_dictionary(l2_codes)

    return level, l1_codes, l2_codes, encoded_data



# def unpack(packed_data):

#     level = ""
#     padding = ""
#     l1_codes_len = ""
#     l2_codes_len = ""
#     l1_codes = ""
#     l2_codes = ""
#     i = 0

#     # extract level
#     for byte in packed_data:
#         char = bytes([byte]).decode('utf-8')
#         if char != '|':
#             level += char
#         i += 1
#     packed_data = packed_data[i:]
#     i = 0

#     # extract padding
#     for byte in packed_data:
#         char = bytes([byte]).decode('utf-8')
#         if char != '|':
#             padding += char
#         i += 1
#     packed_data = packed_data[i:]
#     i = 0

#     # extract l1_codes_len
#     for byte in packed_data:
#         char = bytes([byte]).decode('utf-8')
#         if char != '|':
#             l1_codes_len += char
#         i += 1
#     packed_data = packed_data[i:]
#     i = 0

#     # extract l2_codes_len
#     for byte in packed_data:
#         char = bytes([byte]).decode('utf-8')
#         if char != '|':
#             l2_codes_len += char
#         i += 1
#     packed_data = packed_data[i:]

#     level = int(level)
#     padding = int(padding)
#     l1_codes_len = int(l1_codes_len)
#     l2_codes_len = int(l2_codes_len)

#     l1_codes = packed_data[:l1_codes_len]
#     packed_data = packed_data[l1_codes_len:]
#     l2_codes = packed_data[:l2_codes_len]
#     packed_data = packed_data[l2_codes_len:]
#     encoded_data = packed_data

#     return level, l1_codes, l2_codes, encoded_data






# def unpack(packed_data):
#     pos = 0
#     char = packed_data[pos]
#     level = ""
#     padding = ""
#     l1_codes_len = ""
#     l2_codes_len = ""
#     l1_codes = ""
#     l2_codes = ""

#     while char != '|':
#         level += char
#         pos += 1
#         char = packed_data[pos]
#     pos += 1
#     char = packed_data[pos]

#     while char != '|':
#         padding += char
#         pos += 1
#         char = packed_data[pos]
#     pos += 1
#     char = packed_data[pos]

#     while char != '|':
#         l1_codes_len += char
#         pos += 1
#         char = packed_data[pos]
#     pos += 1
#     char = packed_data[pos]

#     while char != '|':
#         l2_codes_len += char
#         pos += 1
#         char = packed_data[pos]
#     pos += 1

#     level = int(level)
#     padding = int(padding)
#     l1_codes_len = int(l1_codes_len)
#     l2_codes_len = int(l2_codes_len)

#     semi_packed_data = packed_data[pos:]
#     l1_codes = semi_packed_data[:l1_codes_len]
#     semi_packed_data = semi_packed_data[l1_codes_len:]
#     l2_codes = semi_packed_data[:l2_codes_len]
#     semi_packed_data = semi_packed_data[l2_codes_len:]
#     encoded_data = chars_to_bits(semi_packed_data)

#     l1_codes = string_to_dictionary(l1_codes)
#     l2_codes = string_to_dictionary(l2_codes)

#     return level, l1_codes, l2_codes, encoded_data