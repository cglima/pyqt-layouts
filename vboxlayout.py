import sys

from PySide6.QtWidgets import (
    QApplication, 
    QVBoxLayout, 
    QPushButton, 
    QWidget, 
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout Example")
        self.resize(270, 110)
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Top"))
        layout.addWidget(QPushButton("Center"))
        layout.addWidget(QPushButton("Bottom"))
        # CRIA UM ESPAÇADOR sem afetar a posição ou tamnho dos widgets
        layout.addStretch()
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())