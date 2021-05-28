import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot

class Scene(QWidget):
	def __init__(self):
		super().__init__()	# run QWidget's __init__()

	
	
		textLabel = QLabel(self)
		textLabel.setText("Hello World!")
		textLabel.move(110,85)
		
		self.setGeometry(50,50,320,200)
		self.setWindowTitle("PyQt5 Example")






app = QApplication(sys.argv)
myScene = Scene()
myScene.show()
sys.exit(app.exec_())


####################################
#app = QApplication(sys.argv)
#widget = QWidget()

#textLabel = QLabel(widget)
#textLabel.setText("Hello World!")
#textLabel.move(110,85)

#widget.setGeometry(50,50,320,200)	#tk.geometry('320x200+50+50')
#widget.setWindowTitle("PyQt5 Example")
#widget.show()
#sys.exit(app.exec_())	#Tk.mainloop()

from students import *

arr = []

arr.append(Doge())
arr.append(Congrats())
arr.append(Car())
arr.append(Cat())
arr.append(Poyo())
arr.append(what())

for chara in arr:
	chara.move()