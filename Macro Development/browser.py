import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Survey Browser")
window.setGeometry(200, 100, 1500, 1000)

browser = QWebEngineView(window)
window.setCentralWidget(browser)

profile = browser.page().profile()
profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)

url = QUrl.fromUserInput(sys.argv[1])
browser.setUrl(url)

window.show()
sys.exit(app.exec_())