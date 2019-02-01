from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class CustomMessageBox(QMessageBox):
	def __init__(self, *__args):
		QMessageBox.__init__(self)
		self.timeout = 0
		self.autoclose = False
		self.currentTime = 0

	def showEvent(self, QShowEvent):
		self.currentTime = 0
		if self.autoclose:
			self.startTimer(1000)

	def timerEvent(self, *args, **kwargs):
		self.currentTime += 1
		if self.currentTime >= self.timeout:
			self.done(0)

	@staticmethod
	def showWithTimeout(timeoutSeconds,description,icon):
		w = CustomMessageBox()
		CSSLine="QPushButton{background:url(:/images/"+icon+".png)}"
		w.setStyleSheet(CSSLine)
		w.setGeometry(250,225,0,0)
		w.setText(description)
		w.setStandardButtons(QMessageBox.Ok)
		button=w.button(QMessageBox.Ok)
		button.setText("")
		w.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)		
		w.autoclose = True
		w.timeout = timeoutSeconds
		w.exec_()
