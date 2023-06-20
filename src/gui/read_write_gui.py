from PyQt5.QtWidgets import QApplication, QFileDialog
import os

# Disable QT_DEVICE_PIXEL_RATIO warning
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
os.environ["QT_SCALE_FACTOR"] = "1"

def open_directory_dialog(initial_directory):
    app = QApplication([])
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.DirectoryOnly)
    file_dialog.setOption(QFileDialog.ShowDirsOnly, True)
    file_dialog.setDirectory(initial_directory)
    file_dialog.setWindowTitle("Select destination directory")
    
    if file_dialog.exec_() == QFileDialog.Accepted:
        selected_directory = file_dialog.selectedFiles()[0]
        return selected_directory
    
    return None

def open_file_dialog():
    app = QApplication([])
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.AnyFile)
    file_dialog.setWindowTitle("Select file")

    if file_dialog.exec_() == QFileDialog.Accepted:
        selected_files = file_dialog.selectedFiles()
        if len(selected_files) > 0:
            selected_file = selected_files[0]
            return selected_file

    return None

def open_raisin_file_dialog():
    app = QApplication([])
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    file_dialog.setWindowTitle("Select compressed file")
    file_dialog.setNameFilter("Raisin Files (*.raisin)")

    if file_dialog.exec_() == QFileDialog.Accepted:
        selected_files = file_dialog.selectedFiles()
        if len(selected_files) > 0:
            file_path = selected_files[0]
            return file_path

    return None