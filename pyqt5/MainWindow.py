from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QMessageBox


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(100,100, 800,600)
        self.show()

        self.button = QPushButton('нажми сюда!', self)
        self.button.setGeometry(20,20 ,300,40)
        self.button.show()
        self.button.clicked.connect(self.on_click)


    def on_click(self):
        msg = QMessageBox(self)
        msg.setText('Чего нажал?!')
        msg.exec()