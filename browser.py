import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QProgressBar, QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import configparser

cnfg = configparser.ConfigParser()
cnfg.read("storage/config.inf")

GENERAL_SEC = cnfg["General"]
HOMEPAGE = GENERAL_SEC["HomePage"]
VERSION = GENERAL_SEC["Version"]
LANG = GENERAL_SEC["Language"]
SHOW = GENERAL_SEC["ShowType"]

NEW_PAGE_NAME = ""
RELOAD_NAME = ""
HOME_NAME = ""
BROWSER_NAME = ""

if LANG == "pt":
    NEW_PAGE_NAME = "Nova Guia"
    RELOAD_NAME = "Recarregar"
    HOME_NAME = "Página Inicial"
    BROWSER_NAME = "NavegadorPy"
elif LANG == "en":
    NEW_PAGE_NAME = "New Tab"
    RELOAD_NAME = "Reload"
    HOME_NAME = "Home"
    BROWSER_NAME = "BrowserPy"
elif LANG == "es":
    NEW_PAGE_NAME = "Nueva guia"
    RELOAD_NAME = "Recargar"
    HOME_NAME = "Página de inicio"
    BROWSER_NAME = "NavegadorPy"
elif LANG == "ja":
    NEW_PAGE_NAME = "新しいタブ"
    RELOAD_NAME = "リチャージ"
    HOME_NAME = "ホームページ"
    BROWSER_NAME = "ブラウザパイ"

class BrowserWindow(QMainWindow):
    def __init__(self):        
        super().__init__()

        print(
"""
 /$$$$$$$                                                                  /$$$$$$$           
| $$__  $$                                                                | $$__  $$          
| $$  \ $$  /$$$$$$   /$$$$$$  /$$  /$$  /$$  /$$$$$$$  /$$$$$$   /$$$$$$ | $$  \ $$ /$$   /$$
| $$$$$$$  /$$__  $$ /$$__  $$| $$ | $$ | $$ /$$_____/ /$$__  $$ /$$__  $$| $$$$$$$/| $$  | $$
| $$__  $$| $$  \__/| $$  \ $$| $$ | $$ | $$|  $$$$$$ | $$$$$$$$| $$  \__/| $$____/ | $$  | $$
| $$  \ $$| $$      | $$  | $$| $$ | $$ | $$ \____  $$| $$_____/| $$      | $$      | $$  | $$
| $$$$$$$/| $$      |  $$$$$$/|  $$$$$/$$$$/ /$$$$$$$/|  $$$$$$$| $$      | $$      |  $$$$$$$
|_______/ |__/       \______/  \_____/\___/ |_______/  \_______/|__/      |__/       \____  $$
                                                                                     /$$  | $$
                                                                                    |  $$$$$$/
                                                                                     \______/     version """ + VERSION +
"""

[WARNING]
If you paid for this program, you has been scammed.
Get your money back before it's too late!
""")

        self.setWindowTitle(f"{BROWSER_NAME} v" + VERSION)
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        if SHOW == "Max":
            self.showMaximized()
        elif SHOW == "Nor":
            self.showNormal()
        elif SHOW == "Min":
            self.showMinimized()
            
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)
        self.add_tab()
        self.add_tab_button = QPushButton("+")
        self.add_tab_button.clicked.connect(self.add_tab)
        self.remove_tab_button = QPushButton("-")
        self.remove_tab_button.clicked.connect(self.remove_current_tab)
        tab_buttons_layout = QHBoxLayout()
        tab_buttons_layout.addWidget(self.add_tab_button)
        tab_buttons_layout.addWidget(self.remove_tab_button)
        self.layout.addLayout(tab_buttons_layout)

    def add_tab(self):
        tab = QWidget()
        tab_layout = QVBoxLayout()
        tab.setLayout(tab_layout)

        browser = QWebEngineView()
        browser.setUrl(QUrl(HOMEPAGE))

        url_bar = QLineEdit()
        url_bar.returnPressed.connect(lambda: self.navigate_to_url(browser, url_bar))

        back_button = QPushButton("<-")
        back_button.clicked.connect(browser.back)

        forward_button = QPushButton("->")
        forward_button.clicked.connect(browser.forward)

        reload_button = QPushButton(f"{RELOAD_NAME}")
        reload_button.clicked.connect(browser.reload)

        home_button = QPushButton(f"{HOME_NAME}")
        home_button.clicked.connect(lambda: browser.setUrl(QUrl(HOMEPAGE)))

        progress_bar = QProgressBar()
        browser.loadProgress.connect(progress_bar.setValue)

        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(back_button)
        navigation_layout.addWidget(forward_button)
        navigation_layout.addWidget(reload_button)
        navigation_layout.addWidget(home_button)

        tab_layout.addWidget(url_bar)
        tab_layout.addLayout(navigation_layout)
        tab_layout.addWidget(progress_bar)
        tab_layout.addWidget(browser)

        self.tabs.addTab(tab, f"{NEW_PAGE_NAME}")

    def remove_current_tab(self):
        current_index = self.tabs.currentIndex()
        if current_index != -1:
            self.tabs.removeTab(current_index)

    def navigate_to_url(self, browser, url_bar):
        url = url_bar.text()
        if not url.startswith('http'):
            url = f'http://www.google.com/search?q={url}'
        browser.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())
