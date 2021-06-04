# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(418, 391)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.configGroupBox = QGroupBox(Dialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit0)

        self.label1 = QLabel(self.configGroupBox)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label1)

        self.comboBoxMethod = QComboBox(self.configGroupBox)
        self.comboBoxMethod.setObjectName(u"comboBoxMethod")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBoxMethod)

        self.comboBoxClass = QComboBox(self.configGroupBox)
        self.comboBoxClass.setObjectName(u"comboBoxClass")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxClass)

        self.label = QLabel(self.configGroupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.configGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.lineEditLASIS = QLineEdit(self.configGroupBox)
        self.lineEditLASIS.setObjectName(u"lineEditLASIS")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEditLASIS)

        self.label_3 = QLabel(self.configGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.configGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.configGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.configGroupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.lineEditRASIS = QLineEdit(self.configGroupBox)
        self.lineEditRASIS.setObjectName(u"lineEditRASIS")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEditRASIS)

        self.lineEditLPSIS = QLineEdit(self.configGroupBox)
        self.lineEditLPSIS.setObjectName(u"lineEditLPSIS")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEditLPSIS)

        self.lineEditRPSIS = QLineEdit(self.configGroupBox)
        self.lineEditRPSIS.setObjectName(u"lineEditRPSIS")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEditRPSIS)

        self.lineEditPS = QLineEdit(self.configGroupBox)
        self.lineEditPS.setObjectName(u"lineEditPS")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEditPS)

        self.label_7 = QLabel(self.configGroupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_7)

        self.checkBoxGUI = QCheckBox(self.configGroupBox)
        self.checkBoxGUI.setObjectName(u"checkBoxGUI")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.checkBoxGUI)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ConfigureDialog", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("Dialog", u"identifier:  ", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"Prediction Method:  ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Population Class:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"LASIS:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"RASIS:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"LPSIS:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"RPSIS:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Pubis Symphysis:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"GUI:", None))
        self.checkBoxGUI.setText("")
    # retranslateUi

