
# PACK

def dictionary_to_string(dictionary):
    pairs = []
    for key, value in dictionary.items():
        pairs.append(f"'{key}':'{value}'")
    return '{' + ',,'.join(pairs) + '}'

def data_padding(binary_str):
    padding = 8 - len(binary_str) % 8
    for i in range(padding):
        binary_str += "0"
    return padding, binary_str

def bits_to_chars(bit_string):
    char_string = ''
    for i in range(0, len(bit_string), 8):
        bits = bit_string[i:i+8]
        char = chr(int(bits, 2))
        char_string += char
    return char_string

def pack(level, codes_l1, codes_l2, encoded_data):
    padding, encoded_data = data_padding(encoded_data)
    encoded_data = bits_to_chars(encoded_data)
    l1_codes_string = dictionary_to_string(codes_l1)
    l2_codes_string = dictionary_to_string(codes_l2)

    semi_packed_data = l1_codes_string + l2_codes_string + encoded_data
    packed_data = str(level) + '|' + str(padding) + '|' + str(len(l1_codes_string)) + '|' + str(len(l2_codes_string)) + '|' + semi_packed_data
    return packed_data

# UNPACK

def string_to_dictionary(string):
    dictionary = {}
    key_value_pairs = string.split(',,')

    for pair in key_value_pairs:
        if ':' in pair:
            key, value = pair.split(':')
            key = key.strip().strip('\'')
            value = value.strip().strip('\'')
            dictionary[key] = value

    return dictionary


def unpack(packed_data):
    pos = 0
    char = packed_data[pos]
    level = ""
    padding = ""
    l1_codes_len = ""
    l2_codes_len = ""
    l1_codes = ""
    l2_codes = ""

    while char != '|':
        level += char
        pos += 1
        char = packed_data[pos]
    pos += 1
    char = packed_data[pos]

    while char != '|':
        padding += char
        pos += 1
        char = packed_data[pos]
    pos += 1
    char = packed_data[pos]

    while char != '|':
        l1_codes_len += char
        pos += 1
        char = packed_data[pos]
    pos += 1
    char = packed_data[pos]

    while char != '|':
        l2_codes_len += char
        pos += 1
        char = packed_data[pos]
    pos += 1

    level = int(level)
    padding = int(padding)
    l1_codes_len = int(l1_codes_len)
    l2_codes_len = int(l2_codes_len)

    semi_packed_data = packed_data[pos:]
    l1_codes = semi_packed_data[:l1_codes_len]
    semi_packed_data = semi_packed_data[l1_codes_len:]
    l2_codes = semi_packed_data[:l2_codes_len]
    semi_packed_data = semi_packed_data[l2_codes_len:]
    encoded_data = semi_packed_data

    l1_codes = string_to_dictionary(l1_codes)
    l2_codes = string_to_dictionary(l2_codes)

    return level, l1_codes, l2_codes, encoded_data

