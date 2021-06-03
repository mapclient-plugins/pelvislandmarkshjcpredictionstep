# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hjcpredictionviewerwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from gias2.mappluginutils.mayaviviewer.mayaviscenewidget import MayaviSceneWidget


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1145, 804)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widgetMain = QWidget(Dialog)
        self.widgetMain.setObjectName(u"widgetMain")
        self.widgetMain.setEnabled(True)
        sizePolicy.setHeightForWidth(self.widgetMain.sizePolicy().hasHeightForWidth())
        self.widgetMain.setSizePolicy(sizePolicy)
        self.widgetMain.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.widgetMain)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.widgetMain)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 150))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout.addWidget(self.tableWidget)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.comboBoxPredMethod = QComboBox(self.widget)
        self.comboBoxPredMethod.setObjectName(u"comboBoxPredMethod")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBoxPredMethod)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.comboBoxPopClass = QComboBox(self.widget)
        self.comboBoxPopClass.setObjectName(u"comboBoxPopClass")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBoxPopClass)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label)

        self.comboBoxLASIS = QComboBox(self.widget)
        self.comboBoxLASIS.setObjectName(u"comboBoxLASIS")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.comboBoxLASIS)

        self.comboBoxRASIS = QComboBox(self.widget)
        self.comboBoxRASIS.setObjectName(u"comboBoxRASIS")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.comboBoxRASIS)

        self.comboBoxLPSIS = QComboBox(self.widget)
        self.comboBoxLPSIS.setObjectName(u"comboBoxLPSIS")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.comboBoxLPSIS)

        self.comboBoxRPSIS = QComboBox(self.widget)
        self.comboBoxRPSIS.setObjectName(u"comboBoxRPSIS")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.comboBoxRPSIS)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.comboBoxPS = QComboBox(self.widget)
        self.comboBoxPS.setObjectName(u"comboBoxPS")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.comboBoxPS)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_7)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.predictButton = QPushButton(self.widget)
        self.predictButton.setObjectName(u"predictButton")

        self.gridLayout_2.addWidget(self.predictButton, 0, 0, 1, 1)

        self.resetButton = QPushButton(self.widget)
        self.resetButton.setObjectName(u"resetButton")

        self.gridLayout_2.addWidget(self.resetButton, 0, 1, 1, 1)

        self.acceptButton = QPushButton(self.widget)
        self.acceptButton.setObjectName(u"acceptButton")

        self.gridLayout_2.addWidget(self.acceptButton, 1, 1, 1, 1)

        self.abortButton = QPushButton(self.widget)
        self.abortButton.setObjectName(u"abortButton")

        self.gridLayout_2.addWidget(self.abortButton, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.screenshotgroup = QGroupBox(self.widget)
        self.screenshotgroup.setObjectName(u"screenshotgroup")
        self.screenshotgroup.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout = QFormLayout(self.screenshotgroup)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.pixelsXLabel = QLabel(self.screenshotgroup)
        self.pixelsXLabel.setObjectName(u"pixelsXLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pixelsXLabel.sizePolicy().hasHeightForWidth())
        self.pixelsXLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pixelsXLabel)

        self.screenshotPixelXLineEdit = QLineEdit(self.screenshotgroup)
        self.screenshotPixelXLineEdit.setObjectName(u"screenshotPixelXLineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.screenshotPixelXLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelXLineEdit.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.screenshotPixelXLineEdit)

        self.pixelsYLabel = QLabel(self.screenshotgroup)
        self.pixelsYLabel.setObjectName(u"pixelsYLabel")
        sizePolicy2.setHeightForWidth(self.pixelsYLabel.sizePolicy().hasHeightForWidth())
        self.pixelsYLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pixelsYLabel)

        self.screenshotPixelYLineEdit = QLineEdit(self.screenshotgroup)
        self.screenshotPixelYLineEdit.setObjectName(u"screenshotPixelYLineEdit")
        sizePolicy3.setHeightForWidth(self.screenshotPixelYLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelYLineEdit.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.screenshotPixelYLineEdit)

        self.screenshotFilenameLabel = QLabel(self.screenshotgroup)
        self.screenshotFilenameLabel.setObjectName(u"screenshotFilenameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.screenshotFilenameLabel)

        self.screenshotFilenameLineEdit = QLineEdit(self.screenshotgroup)
        self.screenshotFilenameLineEdit.setObjectName(u"screenshotFilenameLineEdit")
        sizePolicy3.setHeightForWidth(self.screenshotFilenameLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotFilenameLineEdit.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.screenshotFilenameLineEdit)

        self.screenshotSaveButton = QPushButton(self.screenshotgroup)
        self.screenshotSaveButton.setObjectName(u"screenshotSaveButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.screenshotSaveButton.sizePolicy().hasHeightForWidth())
        self.screenshotSaveButton.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.screenshotSaveButton)


        self.verticalLayout.addWidget(self.screenshotgroup)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.MayaviScene = MayaviSceneWidget(self.widgetMain)
        self.MayaviScene.setObjectName(u"MayaviScene")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.MayaviScene.sizePolicy().hasHeightForWidth())
        self.MayaviScene.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.MayaviScene, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.widgetMain)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Landmark HJC Prediction", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Landmarks", None));
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Prediction Method:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Population Class:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"LASIS:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"RASIS:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"LPSIS:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"RPSIS:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Pubis Symphysis:", None))
        self.predictButton.setText(QCoreApplication.translate("Dialog", u"Predict", None))
        self.resetButton.setText(QCoreApplication.translate("Dialog", u"Reset", None))
        self.acceptButton.setText(QCoreApplication.translate("Dialog", u"Accept", None))
        self.abortButton.setText(QCoreApplication.translate("Dialog", u"Abort", None))
        self.screenshotgroup.setTitle(QCoreApplication.translate("Dialog", u"Screenshot", None))
        self.pixelsXLabel.setText(QCoreApplication.translate("Dialog", u"Pixels X:", None))
        self.screenshotPixelXLineEdit.setText(QCoreApplication.translate("Dialog", u"800", None))
        self.pixelsYLabel.setText(QCoreApplication.translate("Dialog", u"Pixels Y:", None))
        self.screenshotPixelYLineEdit.setText(QCoreApplication.translate("Dialog", u"600", None))
        self.screenshotFilenameLabel.setText(QCoreApplication.translate("Dialog", u"Filename:", None))
        self.screenshotFilenameLineEdit.setText(QCoreApplication.translate("Dialog", u"screenshot.png", None))
        self.screenshotSaveButton.setText(QCoreApplication.translate("Dialog", u"Save Screenshot", None))
    # retranslateUi

