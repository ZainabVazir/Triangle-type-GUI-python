
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("What's your triangle?🤔")
        self.setStyleSheet("color: #823FAC;"
                           "background-color: #C1B2E2;")
        self.setGeometry(700, 300, 600, 600)
        self.setWindowIcon(QIcon("Screenshot_2025-09-20-19-56-31-402_com.pinterest.png"))

        label = QLabel("Know the type of triangle", self)
        label.setGeometry(0, 0, 600, 100)
        label.setScaledContents(True)
        label.setStyleSheet("color: #060606;"
                            "background-color: #7E7299;"
                            "font-size: 40px;"
                            "font-family: Sans Serif;"
                            "border-radius: 20px;")
        label.setAlignment(Qt.AlignCenter)

        self.side_a = QLineEdit(self)
        self.side_a.setPlaceholderText("Enter the value of side a:")
        self.side_a.setGeometry(0, 100, 300, 50)
        self.side_a.setStyleSheet("color: #060606;"
                                 "background-color: #988ABA;"
                                 "font-size: 20px;"
                                 "font-family: Sans Serif;"
                                 "border-radius: 10px;")
  
        self.side_b = QLineEdit(self)
        self.side_b.setPlaceholderText("Enter the value of side b:")
        self.side_b.setGeometry(0, 160, 300, 50)
        self.side_b.setStyleSheet("color: #060606;"
                                 "background-color: #988ABA;"
                                 "font-size: 20px;"
                                 "font-family: Sans Serif;"
                                 "border-radius: 10px;")

        
        self.side_c = QLineEdit(self)
        self.side_c.setPlaceholderText("Enter the value of side c:")
        self.side_c.setGeometry(0, 220, 300, 50)
        self.side_c.setStyleSheet("color: #060606;"
                                 "background-color: #988ABA;"
                                 "font-size: 20px;"
                                 "font-family: Sans Serif;"
                                 "border-radius: 10px;")
        
        self.button = QPushButton("Submit", self)
        self.button.clicked.connect(self.check_tri)
        self.button.setGeometry(250, 350, 100, 50)

        self.result = QLabel("It is :", self)
        self.result.setGeometry(150, 420, 300, 50)
        self.result.setScaledContents(True)
        self.result.setStyleSheet("color: #F5F3F8;"
                                  "background-color: #655D78;"
                                  "font-size:20px;"
                                  "font-family: Sans Serif;"
                                  "border-radius: 10px;")
        
        self.label_x = QLabel("Please enter the values before submitting☺️", self)
        self.label_x.setGeometry(50, 490, 500, 40)
        self.label_x.setAlignment(Qt.AlignCenter)
        self.label_x.setStyleSheet("color: #F5F3F8;"
                                 "background-color: #988ABA;"
                                 "font-size: 20px;"
                                 "font-family: Sans Serif;"
                                 "border-radius: 2px;")

    def check_tri(self):
        a = int(self.side_a.text())
        b = int(self.side_b.text())
        c = int(self.side_c.text())

        if a == b == c:
            print("It is an Equilateral triangle.")
            self.result.setText("an Equilateral triangle.")
        elif a == b or a == c or b == c:
            print("It is an Isosceles triangle.")
            self.result.setText("an Isosceles triangle.")
        else:
            print("It's a Scalene triangle.")
            self.result.setText("a Scalene triangle.")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()