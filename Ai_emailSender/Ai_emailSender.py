
import os
import sys
import getpass
import projectpath
import Ai_Email_data
import datetime
import smtplib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets as qw



class ai_email_senderUI(QtWidgets.QWidget):



    def __init__(self):
        super(ai_email_senderUI, self).__init__()
        un = getpass.getuser()

        self.setObjectName("ai_email_senderUI")
        self.resize(425, 350)
        # self.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        # self.setAnimated(True)
        # self.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(7)
        self.formLayout.setObjectName("formLayout")

        ########################### username / password ###########################

        self.username_lab = QtWidgets.QLabel(self.formLayoutWidget)
        self.username_lab.setObjectName("username_lab")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username_lab)
        self.usernameTxt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameTxt.setObjectName("usernameTxt")
        self.usernameTxt.setText(un)

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameTxt)
        self.pw_lab = QtWidgets.QLabel(self.formLayoutWidget)
        self.pw_lab.setObjectName("pw_lab")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pw_lab)
        self.pwTxt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pwTxt.setInputMask("")
        self.pwTxt.setText("")
        self.pwTxt.setObjectName("pwTxt")
        self.pwTxt.setEchoMode(self.pwTxt.Password)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pwTxt)

        ########################### combobox ###########################

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(300, 10, 111, 51))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("0")
        self.comboBox.addItem("1")
        self.comboBox.addItem("2")
        self.comboBox.currentIndexChanged.connect(self.cb_changed)

        ########################### exp_path / maxfile_path / other_word ###########################

        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 70, 401, 221))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")

        self.exp_path_lab = QtWidgets.QLabel(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exp_path_lab.sizePolicy().hasHeightForWidth())
        self.exp_path_lab.setSizePolicy(sizePolicy)
        self.exp_path_lab.setObjectName("exp_path_lab")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.exp_path_lab)

        self.exp_path = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.exp_path.setObjectName("exp_path_txt")
        self.exp_path.textChanged.connect(self.exp_path_changed)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.exp_path)

        self.maxfile_lab = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.maxfile_lab.setObjectName("maxfile_lab")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxfile_lab)

        self.maxfile_path = QtWidgets.QPlainTextEdit(self.formLayoutWidget_2)
        self.maxfile_path.setObjectName("maxfile_txt")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maxfile_path)

        self.other_word = QtWidgets.QPlainTextEdit(self.formLayoutWidget_2)
        self.other_word.setObjectName("other_word_txt")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.other_word)

        self.other_txt_lab = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.other_txt_lab.setObjectName("other_txt_lab")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.other_txt_lab)

        ########################### chkbx ###########################

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 300, 401, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.ben_chk = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.ben_chk.setObjectName("ben_chk")
        self.horizontalLayout.addWidget(self.ben_chk)

        self.rick_chk = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.rick_chk.setObjectName("rick_chk")
        self.horizontalLayout.addWidget(self.rick_chk)

        self.ccw_chk = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.ccw_chk.setObjectName("ccw_chk")
        self.horizontalLayout.addWidget(self.ccw_chk)

        self.rozy_chk = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.rozy_chk.setObjectName("rozy_chk")
        self.horizontalLayout.addWidget(self.rozy_chk)

        self.send_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.send_btn.setObjectName("send_btn")
        self.send_btn.clicked.connect(self.send_btn_clicked)
        self.horizontalLayout.addWidget(self.send_btn)

        ########################### layout word ######################################

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Ai_emailSender_layout", "Ai Email Sender"))
        self.username_lab.setText(_translate("Ai_emailSender_layout", "USERNAME : "))
        self.pw_lab.setText(_translate("Ai_emailSender_layout", "PASSWORD : "))
        self.comboBox.setItemText(0, _translate("Ai_emailSender_layout", "首次輸出"))
        self.comboBox.setItemText(1, _translate("Ai_emailSender_layout", "修改輸出"))
        self.comboBox.setItemText(2, _translate("Ai_emailSender_layout", "燈光構圖輸出"))
        self.exp_path_lab.setText(_translate("Ai_emailSender_layout", "EXPORT : "))
        self.maxfile_lab.setText(_translate("Ai_emailSender_layout", "檔案連結 : "))
        self.other_txt_lab.setText(_translate("Ai_emailSender_layout", "其他文字 : "))
        self.ben_chk.setText(_translate("Ai_emailSender_layout", "總監"))
        self.rick_chk.setText(_translate("Ai_emailSender_layout", "Rick"))
        self.ccw_chk.setText(_translate("Ai_emailSender_layout", "筑君"))
        self.rozy_chk.setText(_translate("Ai_emailSender_layout", "Rozy"))
        self.send_btn.setText(_translate("Ai_emailSender_layout", "Send Email"))

    ########################### fn cb_changed ###########################

    def cb_changed(self, i):
        if i==0:
            self.ben_chk.setChecked(True)
            self.rick_chk.setChecked(False)
            self.ccw_chk.setChecked(True)
        elif i==1:
            self.ben_chk.setChecked(False)
            self.rick_chk.setChecked(True)
            self.ccw_chk.setChecked(False)
        elif i==2:
            self.ben_chk.setChecked(True)
            self.rick_chk.setChecked(True)
            self.ccw_chk.setChecked(True)

    ########################### fn exp_path_changed ###########################

    def exp_path_changed(self ,exp_path):
        try:
            space_name = Ai_Email_data.get_space_name(exp_path)
            self.other_word.setPlainText("空間 : " + space_name)
        except:
            return

    ########################### fn send_btn_clicked ###########################

    def send_btn_clicked(self):

        un = self.usernameTxt.text()
        pw = self.pwTxt.text()
        type_index = self.comboBox.currentIndex()
        other_word = self.other_word.toPlainText()

        now = datetime.datetime.now()

        if now.month > 9:
            month = str(now.month)
        else:
            month = "0" + str(now.month)

        if now.day > 9:
            day = str(now.day)
        else:
            day = "0" + str(now.day)

        today = str(now.year) + month + day
        send_over = False

        sender = un + " <" + un + "@aistyle.com>"

        try:
            export_path = self.exp_path.text()
            path = projectpath.AiProjectPath(export_path)
            ref_path = path.get_reference()
            final_path = path.get_final()
            cht_name = path.get_chinese_name()
            sc_path = path.get_scenes()

            if cht_name == None:
                cht_name = path.get_english_name()

            maxfile_ary = []
            maxfile_name = (self.maxfile_path.toPlainText()).split()
            for i in maxfile_name:
                maxfile_ary.append(sc_path+i)

            dest = Ai_Email_data.email_dest(self.ben_chk.isChecked(), self.rick_chk.isChecked()
                                            , self.ccw_chk.isChecked(), self.rozy_chk.isChecked())
            subject = Ai_Email_data.email_subject(type_index) + cht_name + "_" + today
            content = Ai_Email_data.email_content(type_index, export_path, ref_path, final_path, "\n".join(maxfile_ary))

            try:
                Ai_Email_data.email_send(un, pw, sender, dest, subject, ("\n\n" + other_word + "\n\n" + content))
                send_over = True

            except smtplib.SMTPAuthenticationError:
                qw.QMessageBox.information(self, "warning", "Login failed!")

        except ValueError:
            qw.QMessageBox.information(self, "warning", "Wrong Export Path!")

        if send_over:
            qw.QMessageBox.information(self, "information", "done!")



if __name__ == '__main__':

    app = qw.QApplication(sys.argv)
    di = ai_email_senderUI()
    di.show()
    sys.exit(app.exec_())

