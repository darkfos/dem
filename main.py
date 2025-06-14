import sys

from PySide6 import QtWidgets

from src.db.db_worker import DBWorker
from src.ui.pages.MainPage import MainWindow
from src.settings import SettingsApp


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    db = DBWorker()

    widget = MainWindow()
    widget.setWindowTitle(SettingsApp.APP_TITLE)
    widget.resize(SettingsApp.APP_WIDTH, SettingsApp.APP_HEIGH)
    widget.show()

    sys.exit(app.exec())