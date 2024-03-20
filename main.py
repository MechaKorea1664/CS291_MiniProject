# main window
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from main_menu import Main_Menu
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(500,500)
    w.setWindowTitle("Main Window")
    #insert main menu here
    Main_Menu(w).main_menu_screen()
    w.show()
    sys.exit(app.exec_())