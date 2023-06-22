# def create_sorted_dict(dict1):
#     dict2 = {}
#     sorted_keys_list = sorted(dict1, key=dict1.get, reverse=True)

#     print(sorted_keys_list)
#     dict2[sorted_keys_list[0]] = '1'
#     dict2[sorted_keys_list[1]] = '01'
#     dict2[sorted_keys_list[2]] = '001'
#     dict2[sorted_keys_list[3]] = '000'
#     return dict2

# dict1 = {'11': 5851, '01': 4983, '10': 4846, '00': 4329}
# print(dict1)
# print(create_sorted_dict(dict1))

def create_sorted_dict(codes):
    l2_codes = {}
    sorted_keys_list = sorted(codes, key=codes.get, reverse=True)
    
    l2_codes[sorted_keys_list[0]] = '1'
    l2_codes[sorted_keys_list[1]] = '01'
    l2_codes[sorted_keys_list[2]] = '001'
    l2_codes[sorted_keys_list[3]] = '000'
    return l2_codes

fr_dict = {'11': 5851, '01': 4983, '10': 4846, '00': 4329}
print(create_sorted_dict(fr_dict))