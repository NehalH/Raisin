from PyQt5.QtWidgets import QApplication, QFileDialog



def open_directory_dialog(initial_directory):
    app = QApplication([])
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.DirectoryOnly)
    file_dialog.setOption(QFileDialog.ShowDirsOnly, True)
    file_dialog.setDirectory(initial_directory)
    
    if file_dialog.exec_() == QFileDialog.Accepted:
        selected_directory = file_dialog.selectedFiles()[0]
        return selected_directory
    
    return None

def open_file_dialog():
    app = QApplication([])
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.AnyFile)

    if file_dialog.exec_() == QFileDialog.Accepted:
        selected_files = file_dialog.selectedFiles()
        if len(selected_files) > 0:
            selected_file = selected_files[0]
            return selected_file

    return None