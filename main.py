import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtCore import QTimer


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(100, 100, 300, 50)
        self.setWindowTitle('Disappearing Text')

        # setup widget
        self.widget = QWidget()
        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

        self.type_field = QTextEdit()
        self.placeholder = "Anything you type will disappear if you stop typing for 10 seconds..."
        self.type_field.setPlaceholderText(self.placeholder)
        layout.addWidget(self.type_field)

        self.timer = QTimer()
        self.timer.timeout.connect(self.delete_text)

        self.type_field.textChanged.connect(self.start_timer)

        # show the window
        self.show()

    def start_timer(self):
        self.timer.start(10000)

    def delete_text(self):
        self.type_field.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
