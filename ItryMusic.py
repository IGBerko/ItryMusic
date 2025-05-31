import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Itry Music Loader")

        self.browser = QWebEngineView()
        self.browser.load(QUrl("https://www.music.itrypro.ru"))
        self.setCentralWidget(self.browser)

app = QApplication(sys.argv)
window = MainWindow()
window.resize(700, 500)
window.show()
sys.exit(app.exec())
