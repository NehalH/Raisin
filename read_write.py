import pickle
import os

def write_to_compressed_file(path, packed_dict):
    filename = os.path.basename(path)
    dest_path = 'Compressed_'+ filename
    try:
        with open(dest_path, 'wb') as file:
            pickle.dump(packed_dict, file)
        return True
    except:
        return False


