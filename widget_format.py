from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox, QApplication, QPushButton

class Widget_Format:
    def push_button (main_window, text, x, y, connect_to):
        button = QPushButton(main_window)
        button.setText(text)
        button.move(x,y)
        button.clicked.connect(connect_to)
        button.exec_()
    def message_box (title = "Error", text = "", text_detail = "", bool_std_button = False):
        message = QMessageBox()
        message.setText(text)
        message.setDetailedText(text_detail)
        if (bool_std_button):
            message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.exec_()