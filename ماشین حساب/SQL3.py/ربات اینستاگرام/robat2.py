
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit
from instagrapi import Client
from instagrapi.types import Media

class InstagramBot(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
        self.username = 'your_username'
        self.password = 'your_password'
        self.api = Client()
        
    def init_ui(self):
        self.setWindowTitle('Instagram Bot')
        
        layout = QVBoxLayout()
        
        self.like_button = QPushButton('Like', self)
        self.like_button.clicked.connect(self.like_photos)
        
        self.messages_label = QLabel('Messages:')
        
        self.messages_text = QTextEdit(self)
        self.messages_text.setReadOnly(True)
        
        layout.addWidget(self.like_button)
        layout.addWidget(self.messages_label)
        layout.addWidget(self.messages_text)
        
        self.setLayout(layout)
        
    def login(self):
        self.api.login(self.username, self.password)
        
    def like_photos(self):
        self.login()
        media = self.api.get_user_feed(self.api.user_id)
        for m in media:
            if m.like_count < 10:  # لایک فقط برای عکس هایی که کمتر از 10 لایک دارند
                self.api.like(m.pk, Media.pk)
        
    def get_messages(self):
        self.login()
        messages = self.api.get_inbox_v2()
        for thread in messages.threads:
            for message in thread.items:
                self.messages_text.append(message.text)
        
if __name__ == '__main__':
    app = QApplication([])
    window = InstagramBot()
    window.show()
    app.exec_()