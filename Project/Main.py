import Excercise
import Test
import os
from PySide6.QtWidgets import QApplication, QDialog
from gui_main import Ui_Dialog
import sys

def make_directory():
    nazwa_folderu = "tests"
    if not os.path.exists(nazwa_folderu):
        os.makedirs(nazwa_folderu)

if __name__ == '__main__':
    make_directory()
    app = QApplication(sys.argv)
    dialog = QDialog()
    ui = Ui_Dialog()

    ui.setupUi(dialog)
    dialog.show()

    sys.exit(app.exec())