import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout,QVBoxLayout, QPushButton, QMessageBox 
import PyQt5.QtCore

def addToLikes():
	print(":)")

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("Create Playlists")
b1 = QPushButton("Like song")
b1.clicked.connect(lambda x: addToLikes())
b2 = QPushButton("Press me")
b2.clicked.connect(lambda x : w.setWindowTitle("Playlist created!"))
layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout2.addWidget(b1)
layout2.addWidget(b2)
layout1.addWidget(QLabel("Spotify > Apple Music"))
layout1.addLayout(layout2)
w.setLayout(layout1)
w.show()
return_code = app.exec_()
sys.exit(return_code)