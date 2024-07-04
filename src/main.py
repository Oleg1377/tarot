import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class TarotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Гадалка на картах Таро')
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 500, 300)
        self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton('Показать карту', self)
        self.button.setGeometry(250, 10, 100, 30)
        self.button.clicked.connect(self.show_card)

    def show_card(self):
        cards = ['src/card1.jpg', 'src/card2.jpg', 'src/card3.jpg']  # Примеры путей к изображениям карт Таро
        card = random.choice(cards)
        pixmap = QPixmap(card)
        self.label.setPixmap(pixmap.scaledToWidth(500))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TarotApp()
    window.show()
    sys.exit(app.exec_())
