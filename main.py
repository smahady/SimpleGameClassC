import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot
from SimpleGame.Scene import Scene
from SimpleGame.Sprite import Sprite

# Base class
class Character(Sprite):
	def __init__(self, thisScene, imageFile, xSize, ySize):
		super().__init__(thisScene, imageFile, xSize, ySize)
	def update(self):
		if self.y > 400:
			self.dx = 0
			self.dy = 0
			self.y = 400

		super().update()

# delete imageFile in __init__, change in super()__init__
# Sean Mahady's Character
# 75 x 75
class Sean(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/sean_sprite.png", 75, 75)
		self.x = 90
		self.y = 100
		self.dx = 1
		self.dy = -1		
		self.boundAction = Scene.WRAP



#Ethan's Character
# 125 x 123
class CheesePuff(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/ethan_sprite.png", 125, 123)
		self.x = 150
		self.y = 150
		
		self.dx = 8 	
		self.dy = 9
		self.boundAction = Scene.WRAP




#Henry's Character
# 75 x 75
class RickAstley(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/henry_sprite.png", 75, 75)
    self.dx = 9
    self.x = 50
    self.y = 50
    self.dy = 9
    self.boundAction = Scene.WRAP
  


#Kamille's Character
# 75 x 79
class Kamille(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/kamille_sprite.png", 75, 79)
    self.x = 70
    self.y = 70
    self.dx += 5
    self.dy += 5
    self.boundAction = Scene.WRAP

#Raphael's Character
# 112 x 67
class Raphael(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene,"sprites/raphael_sprite.png", 112, 67)
    self.x = 65
    self.y = 65
    self.dx = 3
    self.dy = 3
    self.boundAction = Scene.WRAP

#Nelsun's Character
# 112 x 67
class CaptainPanini(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene,"sprites/nelsun_sprite.png" , 112, 67)
    self.x += 60
    self.y += 60
    self.dx = 10
    self.dy = -10
    self.boundAction = Scene.WRAP

# Make a class that inherits character
#Sophie's Character
# 75 x 50
class Sophie(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/sophie_sprite.png", 75, 50)
    self.x += 75
    self.y += 50
    self.dx =6
    self.dy =6
    self.boundAction = Scene.WRAP






app = QApplication(sys.argv)



class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
		self.sean = Sean(self)
		self.CaptainPanini = CaptainPanini(self)
		self.kamille = Kamille(self)
		self.Rickrolled = RickAstley(self)
		self.raphael = Raphael(self)
		self.Ethan = CheesePuff(self)	#CheesePuff
		self.Sophie = Sophie(self)



		
	def updateGame(self):
		self.sean.update()
		self.kamille.update()
		self.Ethan.update()
		self.Rickrolled.update()
		self.raphael.update()
		self.Sophie.update()
		self.CaptainPanini.update()



		

myGame = Game()
myGame.start()
myGame.show()
sys.exit(app.exec_())
'''''
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


# Sean Mahady's Sprite
# 75 x 75
# https://opengameart.org/content/cat-fighter-sprite-sheet
# Cat Fighter by DogChicken @ OpenGameArt.org

# Raphael's Sprite
# 112 x 67
# https://opengameart.org/content/dog-walk-sprite-and-bone
# dog-walk-sprite-and-bone by kirard

# Sophie's Sprite
# 75 x 50
# https://opengameart.org/content/rabbit-2
# Rabbit by Aeynit

# HenryWasTaken
# 75 x 75
# https://opengameart.org/content/skeleton-guy-animated
# Disthron @ opengameart.org

# Nelsun's sprite sheet
# 112 x 67
# https://opengameart.org/content/dog-walk-sprite-and-bone
# dog sprite and bone by krirard

# Kamille's sprite sheet
# 75 x 79
# https://opengameart.org/content/deer
# deer sprite by calciumtrice

#Ethan's Sprite sheet
# 125 x 123
#https://opengameart.org/content/astronaut-4
#sprite sheet by gamer805'''''





