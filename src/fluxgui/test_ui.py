# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_ui.ui'
#
# Created: Sun Mar  8 23:42:59 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_FluxGUIEvo(object):
    def setupUi(self, FluxGUIEvo):
        FluxGUIEvo.setObjectName(_fromUtf8("FluxGUIEvo"))
        FluxGUIEvo.resize(640, 480)
        self.buttonBox = QtGui.QDialogButtonBox(FluxGUIEvo)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(FluxGUIEvo)
        self.tabWidget.setGeometry(QtCore.QRect(10, 130, 621, 301))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.summer_time = QtGui.QWidget()
        self.summer_time.setObjectName(_fromUtf8("summer_time"))
        self.tabWidget.addTab(self.summer_time, _fromUtf8(""))
        self.winter_time = QtGui.QWidget()
        self.winter_time.setObjectName(_fromUtf8("winter_time"))
        self.tabWidget.addTab(self.winter_time, _fromUtf8(""))
        self.textBrowser = QtGui.QTextBrowser(FluxGUIEvo)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 601, 91))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(FluxGUIEvo)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FluxGUIEvo.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FluxGUIEvo.reject)
        QtCore.QMetaObject.connectSlotsByName(FluxGUIEvo)

    def retranslateUi(self, FluxGUIEvo):
        FluxGUIEvo.setWindowTitle(_translate("FluxGUIEvo", "Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.summer_time), _translate("FluxGUIEvo", "Summer Time", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.winter_time), _translate("FluxGUIEvo", "Winter Time", None))
        self.textBrowser.setHtml(_translate("FluxGUIEvo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to the FluxGUI Evolution indicator. It is a complete QT rewrite from the Killian f.lux indicator applet written in GTK+.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It comes with more advanced features like transitional screen hues and different settings for summer and winter time.</p></body></html>", None))

