import os
from gui import read_write_gui

def write_to_raisin_file(path, packed_data):
    path = os.path.abspath(path)
    default_dir = os.path.dirname(path)
    dest_dir = read_write_gui.open_directory_dialog(default_dir)
    if dest_dir is None:
        print('Dialog cancelled')
        return False

    dest_path = os.path.join(dest_dir, os.path.basename(path) + '.raisin')

    try:
        with open(dest_path, 'wb') as file:
            file.write(packed_data.encode('utf-8'))
        return True
    except Exception as e:
        print('Failed to Create File: ', str(e))
        return False


def read_from_file():
    file_path = read_write_gui.open_file_dialog()
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        return str(data), file_path
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")
    return None

def read_from_raisin_file():
    file_path = read_write_gui.open_raisin_file_dialog()
    try:
        with open(file_path, 'rb') as file:
            data = file.read().decode('utf-8')
        return data, file_path
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")
    return None, None


def write_to_file(path, data):
    path = os.path.abspath(path)
    default_dir = os.path.dirname(path)
    filename = os.path.basename(path)
    dest_dir = read_write_gui.open_directory_dialog(default_dir)
    if dest_dir is None:
        print('Dialog cancelled')
        return False

    dest_path = os.path.join(dest_dir, os.path.splitext(filename)[0])

    try:
        with open(dest_path, 'wb') as file:
            file.write(data.encode('utf-8'))
        print('File created:', dest_path)
        return dest_path
    except Exception as e:
        print('Failed to create file:', str(e))
        return None
