from PyQt5 import QtCore, QtGui, QtWidgets
import infixToPostfix
import random_infix
from check_infix import isInfix

class Ui_Form(object):
	# tarahi windoow
	def widgets(self, Window):
		Window.setFixedSize(640, 350)

		font = QtGui.QFont()
		font.setPointSize(14)

		self.lblMain = QtWidgets.QLabel(Window)
		self.lblMain.setGeometry(QtCore.QRect(20, 20, 593, 19))

		self.txtInfix = QtWidgets.QLineEdit(Window)
		self.txtInfix.setGeometry(QtCore.QRect(70, 50, 520, 40))
		self.txtInfix.setFont(font)

		self.txtPostfix = QtWidgets.QTextBrowser(Window)
		self.txtPostfix.setGeometry(QtCore.QRect(70, 100, 520, 100))
		self.txtPostfix.setFont(font)

		self.btnClear = QtWidgets.QPushButton(Window)
		self.btnClear.setGeometry(QtCore.QRect(30, 50, 35, 35))

		self.btnMohasebeh = QtWidgets.QPushButton(Window)
		self.btnMohasebeh.setGeometry(QtCore.QRect(200, 210, 130, 33))

		self.checkboxAutomatic = QtWidgets.QCheckBox(Window)
		self.checkboxAutomatic.setGeometry(QtCore.QRect(350, 216, 150, 20))

		self.lblTedadAmalvand = QtWidgets.QLabel(Window)
		self.lblTedadAmalvand.setGeometry(QtCore.QRect(460, 245, 130, 32))

		self.tedadAmalvand = QtWidgets.QSpinBox(Window)
		self.tedadAmalvand.setGeometry(QtCore.QRect(460, 280, 130, 33))
		self.tedadAmalvand.setMinimum(2)
		self.tedadAmalvand.setMaximum(9999)

		self.btnRandom = QtWidgets.QPushButton(Window)
		self.btnRandom.setGeometry(QtCore.QRect(70, 280, 192, 33))

		self.retranslateUi(Window)
		QtCore.QMetaObject.connectSlotsByName(Window)

	def setupUi(self, Window):
		self.widgets(Window)

		# mohasebeh infix be postfix ba click
		self.btnMohasebeh.clicked.connect(lambda: self.mohasebehPostfix(matn=self.txtInfix.text()))

		# mohasebeh infix be postfix khodkar
		self.checkboxAutomatic.toggled.connect(lambda: self.checkboxAuto())

		# ijad infix random
		self.btnRandom.clicked.connect(lambda: self.clickBtnRandom())

		# pak krdn infix and postfix text
		self.btnClear.clicked.connect(lambda: self.clickBtnClear())

	# barresi checkbox
	def checkboxAuto(self):
		self.txtInfix.setFocus()
		if self.checkboxAutomatic.isChecked():
			self.btnMohasebeh.setEnabled(False)
			self.mohasebehPostfix(matn=self.txtInfix.text())
			self.txtInfix.textChanged.connect(lambda: self.mohasebehPostfix(matn=self.txtInfix.text()))
		else:
			self.btnMohasebeh.setEnabled(True)
			self.txtInfix.textChanged.disconnect()

	def mohasebehPostfix(self, matn):
		matn = ''.join(matn.split())

		printTerminal = False # marahel hal chap shavand ya na
		# agar character infix kamtar az 120 adad bod, marahel ra chap konad
		if len(matn) < 120:
			printTerminal = True

		# barresi infix bodan reshteh
		if isInfix(matn):
			self.txtPostfix.setText(infixToPostfix.infixToPostfix(infix=matn, printTerminal=printTerminal))
		else:
			self.txtPostfix.setText('ورودی درست نیست')
	
	def clickBtnRandom(self):
		self.txtPostfix.clear()
		randInfix = random_infix.randomInfix(self.tedadAmalvand.value())
		self.txtInfix.setText(randInfix)

	def clickBtnClear(self):
		self.txtInfix.clear()
		self.txtPostfix.clear()
		self.txtInfix.setFocus()

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Window", "تمرین شماره ۵ درس ساختمان داده‌ها و الگوریتم‌ها"))
		self.lblMain.setText(_translate("Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">برنامه‌ی تبدیل عبارت میانوندی به پسوندی</span></p></body></html>"))
		self.btnClear.setText(_translate("Window", "C"))
		self.btnMohasebeh.setText(_translate("Window", "محاسبه"))
		self.lblTedadAmalvand.setText(_translate("Window", "تعداد عملوندهای رندوم:"))
		self.btnRandom.setText(_translate("Window", "عبارت میانوندی رندوم"))
		self.checkboxAutomatic.setText(_translate("Window", "محاسبه خودکار"))


def runUI():
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
