import sys

from PySide6.QtWidgets import (
    QApplication, 
    QHBoxLayout, 
    QPushButton, 
    QWidget, 
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout Example")
        layout = QHBoxLayout()
        layout.addWidget(QPushButton("Left-Most"))
        layout.addWidget(QPushButton("Center"), 1)
        layout.addWidget(QPushButton("Right-Most"), 2)
        self.setLayout(layout)
        print(self.children)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())