import sys
from PySide6.QtWidgets import QApplication, QDialog
from gui import Ui_Dialog

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = QDialog()
    ui = Ui_Dialog()

    ui.setupUi(dialog)

    dialog.show()

    sys.exit(app.exec())