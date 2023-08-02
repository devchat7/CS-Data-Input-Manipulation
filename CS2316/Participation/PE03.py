# Your import statements are provided below. Do NOT import
# any other modules for PE03 base
 
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QRadioButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget
    )

class Cryptography(QWidget):

    def __init__(self):
        # everything in self scope is required to be named the same
        super().__init__()

        #set window title
        self.setWindowTitle("Keyword Decoder")

        # set attributes - do NOT change attribute names
        self.key_word_label = QLabel("Keyword:")
        self.key_word = QLineEdit()
        self.encoder = QRadioButton("Encode")
        self.decoder = QRadioButton("Decode")
        self.message_label = QLabel("Message:")
        self.message = QLineEdit()
        self.scrambler = QPushButton("Scramble")
        self.output_label = QLabel("Output Message...")
        self.output = QLineEdit()
        self.history_label = QLabel("History:Input/Output/Keyword")
        self.history = QListWidget()
        self.my_reset = QPushButton("Reset")
        

        # set attribute default status
        self.encoder.setChecked(True)
        self.scrambler.setEnabled(True)
        self.my_reset.setEnabled(False)
        self.message.setEnabled(True)
        self.output.setEnabled(True)

        # connect buttons
        self.scrambler.clicked.connect(self.message_scrambler)
        self.my_reset.clicked.connect(self.reset_all)

        ##############################################################
        # Create your own layout. You may use or ignore
        # the layout skeleton below.
        # It is ok if your layout differs from the example,
        # as long as all features are shown and functional.
        # Remember to set your layout!
        ##############################################################
        # layout (is base layout horizontal (hbox) or vertical (vbox))
        # You can create your boxes and add corresponding widgets below.
        # You can also see the Layout examples at the end of the prompt.

        # level 1 - vbox
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.output_label)
        vbox1.addWidget(self.output)
        vbox1.addWidget(self.my_reset)

        # level 2 - hbox
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.key_word_label)
        hbox1.addWidget(self.key_word)

        # level 3 - hbox
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.encoder)
        hbox2.addWidget(self.decoder)

        # level 4 - hbox
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.scrambler)

        # level 5 - hbox
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.history_label)
        hbox5.addWidget(self.history)

        # level 6 - hbox
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.message_label)
        hbox4.addWidget(self.message)

        vbox=QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox3)
        vbox.addLayout(vbox1)
        vbox.addLayout(hbox5)
        self.setLayout(vbox)

        # set layout
        # You can set the layout/arrangement of your boxes here.

    ##################################################################
    # this method is given to you; do NOT change for PE03 base
    def coder(self):
        a_bet = "abcdefghijklmnopqrstuvwxyz .?!,"
        keyword = self.key_word.text().lower()
        new_str = ""
        for i in keyword + a_bet:
            if i not in new_str:
                new_str += i
            else:
                continue
        if self.encoder.isChecked() == True:
            return {key:val for key, val in zip(list(a_bet), list(new_str))}
        if self.decoder.isChecked() == True:
            return {val:key for key, val in zip(list(a_bet), list(new_str))}
    ###################################################################
    def message_scrambler(self) :
        output_text = ""
        self.my_reset.setEnabled(True)
        self.scrambler.setEnabled(False)
        self.key_word.setEnabled(False)
        self.message.setEnabled(False)
        input_text = self.message.text().lower()
        keyboard = self.key_word.text().lower()
        for value in input_text :
            output_text += self.coder()[value]
        self.output.setText(output_text)
        self.history.addItem(f"{input_text}/{output_text}/{keyboard}")


    def reset_all(self):
        self.my_reset.setEnabled(False)
        self.key_word.setEnabled(True)
        self.scrambler.setEnabled(True)
        self.message.setEnabled(True)
        self.encoder.setChecked(True)
        self.decoder.setChecked(False)
        self.key_word.clear()
        self.message.clear()
        self.output.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Cryptography()
    main.show()
    exit_code = app.exec_()
    sys.exit(exit_code)
