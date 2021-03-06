# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from DB import add , fetch , fetchall

class Ui_Form(object):
    def setupUi(self,Form):
        Form.setObjectName("Form")
        Form.resize(408, 314)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 40, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 110, 61, 20))
        self.label_3.setObjectName("label_3")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(220, 40, 113, 20))
        self.name.setObjectName("name")
        self.nickName = QtWidgets.QLineEdit(Form)
        self.nickName.setGeometry(QtCore.QRect(220, 80, 113, 20))
        self.nickName.setObjectName("nickName")
        self.classe = QtWidgets.QLineEdit(Form)
        self.classe.setGeometry(QtCore.QRect(220, 120, 113, 20))
        self.classe.setObjectName("classe")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 200, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.CIN = QtWidgets.QLineEdit(Form)
        self.CIN.setGeometry(QtCore.QRect(220, 10, 113, 20))
        self.CIN.setObjectName("CIN")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(100, 10, 47, 13))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "name :"))
        self.label_2.setText(_translate("Form", "nickname :"))
        self.label_3.setText(_translate("Form", "classe :"))
        self.pushButton.setText(_translate("Form", "Add"))
        self.pushButton_2.setText(_translate("Form", "show Liste"))
        self.label_4.setText(_translate("Form", "CIN :"))
        self.pushButton.clicked.connect(self.click)
        
        
        
    


    def click(self):
        cin = self.CIN.text()
        name = self.name.text()
        nickName = self.nickName.text()
        classe = self.classe.text()

        add(cin,name,nickName,classe)
        fetchall()    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    

