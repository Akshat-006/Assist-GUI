# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JarvisGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisGUI(object):
    def setupUi(self, JarvisGUI):
        JarvisGUI.setObjectName("JarvisGUI")
        JarvisGUI.resize(707, 468)
        self.centralwidget = QtWidgets.QWidget(JarvisGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-14, -8, 731, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/user/Downloads/armour.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 240, 161, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/user/Downloads/Button (6).jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 330, 161, 71))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:/Users/user/Downloads/Button (6).jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 260, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(35, 199, 207);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 350, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(230, 0, 3);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(-20, -60, 321, 201))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("C:/Users/user/Downloads/Initialise.gif"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, -10, 191, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/user/Downloads/Button (2).jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, -10, 181, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/user/Downloads/Button (2).jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(520, 10, 151, 41))
        self.textBrowser_3.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(330, 10, 151, 41))
        self.textBrowser_4.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser_4.setObjectName("textBrowser_4")
        JarvisGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JarvisGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 21))
        self.menubar.setObjectName("menubar")
        JarvisGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JarvisGUI)
        self.statusbar.setObjectName("statusbar")
        JarvisGUI.setStatusBar(self.statusbar)

        self.retranslateUi(JarvisGUI)
        QtCore.QMetaObject.connectSlotsByName(JarvisGUI)

    def retranslateUi(self, JarvisGUI):
        _translate = QtCore.QCoreApplication.translate
        JarvisGUI.setWindowTitle(_translate("JarvisGUI", "MainWindow"))
        self.pushButton.setText(_translate("JarvisGUI", "Run"))
        self.pushButton_2.setText(_translate("JarvisGUI", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JarvisGUI = QtWidgets.QMainWindow()
    ui = Ui_JarvisGUI()
    ui.setupUi(JarvisGUI)
    JarvisGUI.show()
    sys.exit(app.exec_())
