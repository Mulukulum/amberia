# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(718, 384)
        MainWindow.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 709, 373))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet("background: rgb(255, 85, 0)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setStyleSheet("background: rgb(255, 85, 0)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("background: rgb(255, 255, 127)")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 4)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 4)
        self.TodayTasksScrollArea = QtWidgets.QScrollArea(self.widget)
        self.TodayTasksScrollArea.setStyleSheet("background: rgb(255, 255, 255)")
        self.TodayTasksScrollArea.setWidgetResizable(True)
        self.TodayTasksScrollArea.setObjectName("TodayTasksScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 505, 255))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.TodayTasksScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.TodayTasksScrollArea, 2, 4, 2, 1)
        self.ProjectScrollArea = QtWidgets.QScrollArea(self.widget)
        self.ProjectScrollArea.setWidgetResizable(True)
        self.ProjectScrollArea.setObjectName("ProjectScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 192, 223))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.ProjectScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.ProjectScrollArea, 3, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.pushButton_2.setText(_translate("MainWindow", "<---"))
        self.pushButton_4.setText(_translate("MainWindow", "--->"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">AMBERIA </span><span style=\" font-size:24pt; color:#ffffff; vertical-align:super;\">©2022</span></p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Today\'s Task(s)"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Today\'s Date: Curdate</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Project(s)</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
