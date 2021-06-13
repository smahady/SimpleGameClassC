import sys
from Keys import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
#from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

class Scene(QWidget):
	
	# class variables, instance variables, local variables, and global variables 
	# global variables are outside of any function, method, or class definition
	# local variables are defined inside of a function or method

	# class variables
	WRAP = 0
	BOUNCE = 1 
	STOP = 3
	DIE = 4 
	CONTINUE = 5
	
	# key variables
	K_ESC = 27
	K_SPACE = 32
	K_PGUP = 33
	K_PGDOWN = 34
	K_END = 35
	K_HOME = 36
	K_LEFT = 37
	K_UP = 38
	K_RIGHT = 39
	K_DOWN = 40
	
	# slope variables
	SLOPE_RIGHT = True
	SLOPE_LEFT = True	


	def __init__(self, x=600, y=400, speed=33):
		super().__init__()	

	

		
		self.setGeometry(50,50,x,y)
		self.setWindowTitle("PyQt5 Example")

		self.speed = speed
		
		self.width = x 
		self.height = y		
		
		self.timer = QTimer()
		self.timer.timeout.connect(self.updateTask)
		
		self.keysDown = [None] * 256
		self.boardKeysDown = [None] * 256
		self.virtKeysDown = [None] * 256		
		
		self.initKeys()


	def start(self):
		self.timer.start(self.speed)
		
	def stop(self):
		self.timer.stop()

	def updateTask(self):
		self.update()
	
	def paintEvent(self, event):
		for i in range(255):
			self.keysDown[i] = (self.boardKeysDown[i] or self.virtKeysDown[i])	
		
		self.updateGame()	
	
	# this should be overwritten by the game	
	def updateGame(self):
		pass

	# initializes key values to false
	def initKeys(self):
		for i in range(255):
			self.keysDown[i] = False
		for i in range(255):
			self.boardKeysDown[i] = False

	def keyPressEvent(self, event):
		for i in range(255):
			if KeyTbl[i] == event.key():
				self.boardKeysDown = True
		
	def keyReleaseEvent(self, event):
		for i in range(255):
			if KeyTbl[i] == event.key():
				self.boardKeysDown = False



