
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from instapy import InstaPy

class InstagramBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Instagram Bot')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        
        self.label = QLabel('Welcome to Instagram Bot', self)
        layout.addWidget(self.label)

        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.like_button = QPushButton('Like Posts', self)
        self.like_button.clicked.connect(self.like_posts)
        layout.addWidget(self.like_button)

        self.logout_button = QPushButton('Logout', self)
        self.logout_button.clicked.connect(self.logout)
        layout.addWidget(self.logout_button)

        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.session = None

    def login(self):
        username = 'your_username'
        password = 'your_password'
        self.session = InstaPy(username=username, password=password)
        self.session.login()
        self
vmess://eyJhZGQiOiJtci5tYW5zdXJpc3BlZWQxLm9ubGluZSIsImFpZCI6IjAiLCJob3N0IjoiIiwiaWQiOiJjY2JiZmEzOC1iM2E2LTQ2OTctYWNlMi1hYzI0MWRiYjVkNTIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiIiwicG9ydCI6IjE2OTA3IiwicHMiOiJCMzMgYW1pcm1haGRpIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6Im5vbmUiLCJ0eXBlIjoibm9uZSIsInYiOiIyIn0=