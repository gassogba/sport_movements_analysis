# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaceTestQt.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 0, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 70, 111, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 111, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 190, 531, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 50, 531, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(160, 70, 261, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(160, 110, 261, 31))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 210, 511, 121))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setKerning(False)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 20, 241, 17))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(250, 20, 487, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 291, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(310, 60, 42, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(10)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.verticalLayout.addWidget(self.groupBox)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(30, 520, 531, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 540, 111, 31))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(30, 340, 531, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 360, 511, 161))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.PCA = QtGui.QWidget()
        self.PCA.setObjectName(_fromUtf8("PCA"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.PCA)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 491, 72))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBox_6 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.horizontalLayout_2.addWidget(self.checkBox_6)
        self.checkBox_7 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.horizontalLayout_2.addWidget(self.checkBox_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBox_8 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.horizontalLayout.addWidget(self.checkBox_8)
        self.checkBox_5 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.horizontalLayout.addWidget(self.checkBox_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.label_2 = QtGui.QLabel(self.PCA)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.spinBox = QtGui.QSpinBox(self.PCA)
        self.spinBox.setGeometry(QtCore.QRect(170, 10, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setValue(3)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.tabWidget.addTab(self.PCA, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 491, 72))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkBox_9 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.horizontalLayout_3.addWidget(self.checkBox_9)
        self.checkBox_10 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.horizontalLayout_3.addWidget(self.checkBox_10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.checkBox_11 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.horizontalLayout_4.addWidget(self.checkBox_11)
        self.checkBox_12 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.horizontalLayout_4.addWidget(self.checkBox_12)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 160, 221, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.spinBox_3 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(270, 160, 42, 22))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(10)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.checkBox_13 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_13.setGeometry(QtCore.QRect(30, 550, 291, 17))
        self.checkBox_13.setTristate(False)
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sport analysis", None))
        self.label.setText(_translate("MainWindow", "Analysis of sport mouvements thanks to machine learning algorithms", None))
        self.pushButton.setText(_translate("MainWindow", "Movement data file", None))
        self.pushButton_2.setText(_translate("MainWindow", "Performance data file", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.groupBox.setTitle(_translate("MainWindow", "Choose the method for distinguishing the best and worst performance:", None))
        self.radioButton_2.setText(_translate("MainWindow", "K-means method", None))
        self.radioButton.setText(_translate("MainWindow", "33% worst / 33% best performance", None))
        self.label_5.setText(_translate("MainWindow", "Number of Performance variables to use for the distinctions:", None))
        self.pushButton_3.setText(_translate("MainWindow", "Launch", None))
        self.label_3.setText(_translate("MainWindow", "Choose the method(s) to perform on the data:", None))
        self.checkBox_6.setText(_translate("MainWindow", "regressions using loadings and perf matrix", None))
        self.checkBox_7.setText(_translate("MainWindow", "data projection along PCs axis", None))
        self.checkBox_8.setText(_translate("MainWindow", "projections of best and wosrt groups", None))
        self.checkBox_5.setText(_translate("MainWindow", "PC scores with  loadings\' standard deviation", None))
        self.label_2.setText(_translate("MainWindow", "Number of Principal Component:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PCA), _translate("MainWindow", "PCA", None))
        self.label_4.setText(_translate("MainWindow", "Choose the method(s) to perform on the data:", None))
        self.checkBox_9.setText(_translate("MainWindow", "algo1", None))
        self.checkBox_10.setText(_translate("MainWindow", "algo2", None))
        self.checkBox_11.setText(_translate("MainWindow", "algo 3", None))
        self.checkBox_12.setText(_translate("MainWindow", "algo 4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "other algos", None))
        self.label_6.setText(_translate("MainWindow", "Number of Performance variables to analyze:", None))
        self.checkBox_13.setText(_translate("MainWindow", "Save the figures in a pylatex file named \"results.tex\"", None))

