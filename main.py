import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(400, 200)

        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(50, 50, 71, 16))
        self.label_email.setObjectName("label_Username")

        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(50, 90, 71, 16))
        self.label_password.setObjectName("label_password")

        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(130, 50, 191, 20))
        self.lineEdit_email.setObjectName("lineEdit_username")

        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(130, 90, 191, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")

        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(150, 140, 75, 23))
        self.pushButton_login.setObjectName("pushButton_login")
        
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(250, 140, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.label_email.setText(_translate("LoginWindow", "Username:"))
        self.label_password.setText(_translate("LoginWindow", "Password:"))
        self.pushButton_login.setText(_translate("LoginWindow", "Login"))
        self.pushButton_cancel.setText(_translate("LoginWindow", "Batal"))
        
        

        

#Formulir Peminjaman Buku
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 708)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 270, 54, 14))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 380, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 300, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 410, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 50, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 380, 101, 16))
        self.label_8.setObjectName("label_8")
        self.IsiID = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.IsiID.setGeometry(QtCore.QRect(160, 340, 551, 31))
        self.IsiID.setObjectName("IsiID")
        self.IsiKode = QtWidgets.QLineEdit(self.centralwidget)
        self.IsiKode.setGeometry(QtCore.QRect(160, 440, 113, 20))
        self.IsiKode.setObjectName("IsiKode")
        self.IsiNama = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.IsiNama.setGeometry(QtCore.QRect(160, 260, 551, 31))
        self.IsiNama.setObjectName("IsiNama")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 340, 101, 16))
        self.label_9.setObjectName("label_9")
        self.IsiNoTelp = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.IsiNoTelp.setGeometry(QtCore.QRect(160, 300, 551, 31))
        self.IsiNoTelp.setObjectName("IsiNoTelp")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 440, 101, 16))
        self.label_3.setObjectName("label_3")
        self.Simpan = QtWidgets.QPushButton(self.centralwidget)
        self.Simpan.setGeometry(QtCore.QRect(720, 510, 85, 26))
        self.Simpan.setObjectName("Simpan")
        self.Batal = QtWidgets.QPushButton(self.centralwidget)
        self.Batal.setGeometry(QtCore.QRect(820, 510, 85, 26))
        self.Batal.setObjectName("Batal")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 110, 291, 141))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 139))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 291, 141))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.JUDUL = QtWidgets.QComboBox(self.centralwidget)
        self.JUDUL.setGeometry(QtCore.QRect(160, 410, 181, 22))
        self.JUDUL.setObjectName("JUDUL")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.JUDUL.addItem("")
        self.IsiLama = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.IsiLama.setGeometry(QtCore.QRect(160, 380, 111, 21))
        self.IsiLama.setObjectName("IsiLama")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionlogin = QtWidgets.QAction(MainWindow)
        self.actionlogin.setObjectName("actionlogin")

        self.retranslateUi(MainWindow)
        self.Batal.clicked.connect(MainWindow.close)
        self.Simpan.clicked.connect(self.on_Simpan_clicked)
        self.IsiNoTelp.textChanged.connect(self.update_buttons)
        self.IsiID.textChanged.connect(self.update_buttons)
        self.IsiKode.textChanged['QString'].connect(self.update_buttons)
        self.IsiNama.textChanged.connect(self.update_buttons)
        self.JUDUL.activated['QString'].connect(self.update_buttons)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Peminjaman Buku"))
        self.label_2.setText(_translate("MainWindow", "NAMA"))
        self.label_7.setText(_translate("MainWindow", "LAMA"))
        self.label_6.setText(_translate("MainWindow", "NO.TELP"))
        self.label_5.setText(_translate("MainWindow", "JUDUL"))
        self.label.setText(_translate("MainWindow", "PEMINJAMAN BUKU PERPUSTAKAAN"))
        self.label_8.setText(_translate("MainWindow", "HARI"))
        self.label_9.setText(_translate("MainWindow", "ID CARD"))
        self.label_3.setText(_translate("MainWindow", "KODE BUKU"))
        self.Simpan.setText(_translate("MainWindow", "Simpan"))
        self.Batal.setText(_translate("MainWindow", "Batal"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "1. Air Mata Terakhir Bunda || 1211"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "2. Perestroika || 1212"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "3. Madilog || 1213"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "4. Mein Kampf || 1214"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "5. Bocchi The Rock || 1215"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "6. A Silent Voice || 1216"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "7. Jujur Kasian || 1217"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "8. Six day War || 1218"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "9. A Man Called Ahok || 1219"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "10. Art of War || 1220"))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "11. Kono Hatsukoi wa Fiction Desu || 1221"))
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "12. Comic Girls || 1222"))
        item = self.listWidget.item(12)
        item.setText(_translate("MainWindow", "13. Holocaust || 1223"))
        item = self.listWidget.item(13)
        item.setText(_translate("MainWindow", "14. Santa Cruz 1991  || 1224"))
        item = self.listWidget.item(14)
        item.setText(_translate("MainWindow", "15. Unai Emery: El Maestro || 1225"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.JUDUL.setItemText(0, _translate("MainWindow", "1. Air Mata Terakhir Bunda"))
        self.JUDUL.setItemText(1, _translate("MainWindow", "2. Perestroika"))
        self.JUDUL.setItemText(2, _translate("MainWindow", "3. Madilog"))
        self.JUDUL.setItemText(3, _translate("MainWindow", "4. Mein Kampf"))
        self.JUDUL.setItemText(4, _translate("MainWindow", "5. Bocchi the Rock"))
        self.JUDUL.setItemText(5, _translate("MainWindow", "6. A Silent Voice"))
        self.JUDUL.setItemText(6, _translate("MainWindow", "7. Jujur Kasian"))
        self.JUDUL.setItemText(7, _translate("MainWindow", "8. Six Day War"))
        self.JUDUL.setItemText(8, _translate("MainWindow", "9. A Man Called Ahok"))
        self.JUDUL.setItemText(9, _translate("MainWindow", "10. Art of War!"))
        self.JUDUL.setItemText(10, _translate("MainWindow", "11. Kono Hatsukoi wa Fiction Desu"))
        self.JUDUL.setItemText(11, _translate("MainWindow", "12. Comic Girls"))
        self.JUDUL.setItemText(12, _translate("MainWindow", "13. Holocaust"))
        self.JUDUL.setItemText(13, _translate("MainWindow", "14. Santa Cruz 1991"))
        self.JUDUL.setItemText(14, _translate("MainWindow", "15. Unai Emery: El Maestro"))
        self.actionlogin.setText(_translate("MainWindow", "login"))

    def update_buttons(self):
        is_all_filled = all(
            [
                self.IsiNama.toPlainText(),
                self.IsiNoTelp.toPlainText(),
                self.IsiID.toPlainText(),
                self.IsiKode.text(),
                self.JUDUL.currentText()
            ]
        )
        self.Simpan.setEnabled(is_all_filled)

        pass

#Koneksi ke database
    def on_Simpan_clicked(self):
        nama = self.IsiNama.toPlainText()
        no_telp = self.IsiNoTelp.toPlainText()
        id_card = self.IsiID.toPlainText()
        kode_buku = self.IsiKode.text()
        judul_buku = self.JUDUL.currentText()

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="library",
                port=3306
            )

            cursor = conn.cursor()

            query = "INSERT INTO surat_pengunjung (nama, no_telp, id_card, kode_buku, judul_buku) VALUES (%s, %s, %s, %s, %s)"
            values = (nama, no_telp, id_card, kode_buku, judul_buku)

            cursor.execute(query, values)

            conn.commit()

            QtWidgets.QMessageBox.information(None, "Informasi", "Data berhasil disimpan")
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            QtWidgets.QMessageBox.warning(None, "Peringatan", f"Gagal menyimpan data, Error: {err}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        pass
    
class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.pushButton_login.clicked.connect(self.on_login_clicked)
        self.pushButton_cancel.clicked.connect(self.close)

    def on_login_clicked(self):
        self.close()
        main_window.show()

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    main_window = QtWidgets.QMainWindow()
    ui_main = Ui_MainWindow()
    ui_main.setupUi(main_window)
    sys.exit(app.exec_())
