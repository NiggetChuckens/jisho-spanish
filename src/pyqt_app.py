from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from jisho import jisho
from translater import translate

def main():
    #define the app
    app = QApplication([])
    
    #define the window
    window = QWidget()
    window.setWindowTitle("Diccionario de Japonés a Español")
    window.setGeometry(100, 100, 350, 270)
    
    #creates a vertical layout
    layout = QVBoxLayout()
    
    #creates a label
    instruction = QLabel(window)
    instruction.setText("Ingrese la palabra japonesa \nde la que quiera tener la definición")
    instruction.setFont(QFont("Arial", 12))
    
    #creates a text box
    textbox = QTextEdit()
    
    #creates a button
    button = QPushButton(window)
    button.setText("Buscar")
    
    #connect the button to the function
    button.clicked.connect(lambda: translate_word(textbox.toPlainText()))
    
    #add the widgets to the layout
    layout.addWidget(instruction)
    layout.addWidget(textbox)
    layout.addWidget(button)
    
    #set the layout to the window
    window.setLayout(layout)
    
    #show the window
    window.show()
    app.exec_()

def translate_word(word):
    
    a = jisho.get_jisho_data(word)
    transalted_a = translate.translate(a[1])
    
    message = QMessageBox()
    message.setText(f"{a[0]} = {transalted_a}")
    
    message.exec_()


if __name__ == "__main__":
    main()
    '''
    word = input("Enter japanese word: ")
    a = jisho.get_jisho_data(word)
    transalted_a = translate.translate(a[1])
    print(f"{a[0]} = {transalted_a}")'''