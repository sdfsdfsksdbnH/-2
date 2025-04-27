from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")


        self.eventName = QtWidgets.QLineEdit(self.centralwidget)
        self.eventName.setPlaceholderText("Название события")
        self.verticalLayout.addWidget(self.eventName)


        self.eventDate = QtWidgets.QDateEdit(self.centralwidget)
        self.eventDate.setCalendarPopup(True)
        self.eventDate.setDate(QtCore.QDate.currentDate())
        self.eventDate.setMinimumDate(QtCore.QDate.currentDate())
        self.verticalLayout.addWidget(self.eventDate)


        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setText("Добавить событие")
        self.verticalLayout.addWidget(self.addButton)


        self.eventList = QtWidgets.QListWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.eventList)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Event Tracker"))
