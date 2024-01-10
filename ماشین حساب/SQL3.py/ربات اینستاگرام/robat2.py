
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit
from instagrapi import Client
from instagrapi.types import Media
from datetime import datetime

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
        
        self.comment_button = QPushButton('comment', self)
        self.comment_button.clicked.connect(self.comment)

        self.messages_label = QLabel('Messages:')
        
        self.messages_text = QTextEdit(self)
        self.messages_text.setReadOnly(True)
        
        layout.addWidget(self.like_button)
        layout.addWidget(self.messages_label)
        layout.addWidget(self.messages_text)
        
        self.setLayout(layout)
        
    def login(self):
        self.api.login(self.username, self.password)  
        self.api.client.user_session_id = self.api.cookie_dict['sessionid']
        self.api.client.user_id = self.api.user_id
        self.api.client.username = self.api.username
        self.api.client.user_agent = self.api.user_agent
        self.api.client.headers.update({'X-CSRFToken': self.api.client.csrftoken})

    def init_post(self, content):
        self.content = content
        self.comments = []
    
    def add_comment(self, comment):
        timestamp = datetime.now()
        self.comments.append((comment, timestamp))
    
    def show_comments(self):
        for comment, timestamp in self.comments:
            print(f"{timestamp}: {comment}")
   
    def init_page(self):
        self.posts = []
    
    def add_post(self, post):
        self.posts.append(post)
    
    def show_posts(self):
        for post in self.posts:
            print(post.content)
            post.show_comments()

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