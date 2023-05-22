
# PACK
def pack(level, codes_l1, codes_l2, encoded_data):
    packed_data = {
        'level': level,
        'codes_l1': codes_l1,
        'codes_l2': codes_l2,
        'encoded_data': encoded_data
    }
    return packed_data

# UNPACK
def unpack(packed_data):
    level = packed_data.get('level')
    codes_l1 = packed_data.get('codes_l1')
    codes_l2 = packed_data.get('codes_l2')
    encoded_data = packed_data.get('encoded_data')
    return level, codes_l1, codes_l2, encoded_data
