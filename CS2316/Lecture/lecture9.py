#Lecture 9 - Inheritance


class Employee:
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		print("Calling the __init__ from Employee")

	def get_raise(self):
		self.salary *= 1.10

	def __repr__(self):
		return f"Employee: {self.name} makes {round(self.salary,2)}"

	def is_highly_paid(self): # add this to Manager
		return self.salary > 20.0



class Manager(Employee):  #manager inherits from Employee
	def __init__(self,name,salary):
		super().__init__(name, salary) #takes everything the same and adds more
		self.employees = []
		print("Calling the __init__ from Manager")

	def hire(self,emp):
		self.employees.append(emp)

	def __repr__(self):
		return f"Manager: {self.name} makes {round(self.salary,2)} \
             has {len(self.employees)} workers"


pablo = Employee("Pablo", 9.75)
print(pablo)
pablo.get_raise()
print(pablo)


melinda = Manager("Melinda",16.25) #calls the __init__
melinda.hire(pablo)
print(melinda)
melinda.get_raise() #uses from employee class
print(melinda)

for e in melinda.employees:
	e.get_raise()
print(pablo)



# the code below shows the lecture11.py the end-of-lecture practice added
# 
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
    QLineEdit,QHBoxLayout,QLabel,QRadioButton)

class MainWindow (QWidget):
    def __init__(self):
        super().__init__()  
        self.setWindowTitle("Hello PyQt!")
        vbox = QVBoxLayout()
        self.label1 = QLabel("I will show which button you click on!")
        vbox.addWidget(self.label1)
        hbox1 = QHBoxLayout()
        self.b1 = QPushButton("Hello!")
        self.b1.setEnabled(False)
        self.b1.clicked.connect(self.change_label)
        hbox1.addWidget(self.b1)
        b2 = QPushButton("Hola!")
        b2.clicked.connect(self.change_label)
        hbox1.addWidget(b2)
        hbox2 = QHBoxLayout()
        b3 = QPushButton("Bye!")
        b3.clicked.connect(self.change_label)        
        hbox2.addWidget(b3)
        self.b4 = QPushButton("Chao!")
        self.b4.clicked.connect(self.change_label)         
        hbox2.addWidget(self.b4)
        self.word_entry = QLineEdit()
        vbox.addWidget(self.word_entry)
        self.word_entry.textEdited.connect(self.on_word_entered) 
        self.rb1 = QRadioButton("1")
        self.rb2 = QRadioButton("2")
        self.rb3 = QRadioButton("3")      
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        self.setLayout(vbox)
    def on_button2_clicked(self):
        print("Hola!")
        print("Amigo")
        self.setWindowTitle("Spanish Practice")
    def on_b3_clicked(self):
        self.setWindowTitle("PyQt!")        
    def on_b4_clicked(self):
        print("Chao")
        self.b4.setText(self.b4.text() * 2) 
    def on_word_entered(self):
        self.setWindowTitle(self.word_entry.text())
        self.rb1.setChecked(True)
        self.b1.setEnabled(True)
    def do_something(self):
        btn = self.sender() # gets sender
        btn.setText("Me!") 
    def change_label(self):
        btn = self.sender() # gets sender
        self.label1.setText("You clicked on " + btn.text())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())





