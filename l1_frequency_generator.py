def get_character_frequencies(file_name):
    freq_dict = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char in freq_dict:
                    freq_dict[char] += 1
                else:
                    freq_dict[char] = 1
    return freq_dict

