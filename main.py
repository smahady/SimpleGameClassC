import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot
from SimpleGame.Scene import Scene
from SimpleGame.Sprite import Sprite
from SimpleGame.Block import Block
from SimpleGame.Background import Background
from enum import Enum

class States(Enum):
	FALLING = 0
	WALK = 1
	JUMP = 2
	STAND = 3

class Facing():
	RIGHT = 0
	LEFT = 1

class Ground(Block):
	def __init__(self, thisScene):
		spriteMaker = [["sprites/ground.png"] ] *30
		super().__init__(thisScene, spriteMaker, 120, 40)
		self.x = 0
		self.y = 500
		
	def update(self, offsetX, offsetY):
				
		super().update(offsetX, offsetY)

class Character(Sprite):
	def __init__(self, thisScene, sprite, x, y):
		self.state = States.FALLING
		self.facing = Facing.RIGHT
		super().__init__(thisScene, sprite, x, y)
		self.stateTimer = 0
		self.dy = 7 
		self.setBoundAction(Scene.CONTINUE)
		
	def update(self, offsetX = 0, offsetY = 0):
		if self.state == States.FALLING:
			if self.scene.ground.collidesWith(self):
				self.standBehavior()
		elif self.state == States.STAND or self.state == States.WALK:
			if self.scene.keysDown[Scene.K_SPACE]:
				self.jumpBehavior()
			elif self.scene.keysDown[Scene.K_RIGHT] or self.scene.keysDown[Scene.K_LEFT]:
				self.walkBehavior()
			elif self.state == States.WALK:
				if (self.facing == Facing.RIGHT) and (self.scene.keysDown[Scene.K_RIGHT] == None):
					self.standBehavior()
				if (self.facing == Facing.LEFT) and (self.scene.keysDown[Scene.K_LEFT] == None):
					self.standBehavior()
		elif self.state == States.JUMP:
			self.stateTimer = self.stateTimer - 1
			if self.stateTimer < 1:
				self.dy = self.dy * -1
				self.state = States.FALLING
		super().update(offsetX, offsetY)

	def standBehavior(self):
		self.dy = 0
		self.dx = 0
		self.state = States.STAND
		self.pauseAnimation()

	# override this in your Character
	def jumpBehavior(self):
		pass

	# override this in your Character
	def walkBehavior(self):
		pass

# sean mahady
#250x100
# 50, 50
class Sean(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/sean_sheet.png", 250, 100)
		self.x = 75	
		self.y = 100
		self.dy = 10
		self.boundAction = Scene.WRAP
		self.loadAnimation(250, 100, 50, 50) 	# divides the sprite sheet into pieces
		self.generateAnimationCycles() 	#sets up each "cylce" into rows
		self.setAnimationSpeed(10)	#sets a QTimer to 100ms
		self.playAnimation()	#starts the QTimer

		#make a state for you class
		self.state = States.FALLING	#falling

	# Add a method called walkBehavior. 
	# This should check if self.scene.keysDown[Scene.K_RIGHT]is True. If so self.facing to 0, self.setCurrentCycle to 0, call the self.playAnimation method. Set the DX to a value between 0 and 10. Set a State to States.WALK
	# If not check if self.scene.keysDown[Scene.K_LEFT] is True. If so self.facing to 1, self.setCurrentCycle to 1, call the self.playAnimation method. Set the DX to a value between 0 and -10. Set a State to States.WALK
	def walkBehavior(self):
		if self.scene.keysDown[Scene.K_RIGHT]:
			self.facing = 0
			self.setCurrentCycle(0)
			self.playAnimation()
			self.dx = 4
			self.state = States.WALK
		elif self.scene.keysDown[Scene.K_LEFT]:
			self.facing = 1
			self.setCurrentCycle(1)
			self.playAnimation()
			self.dx = -4
			self.state = States.WALK

	# Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.
	def jumpBehavior(self):
		self.stateTimer = 25
		self.dy = -4	
		self.state = States.JUMP



#Ethan's Character
# 125 x 123 - non-animated
# 1600x800 sheet version
# 400 x 200 - animation cells
# Change arguments on the super init to 1600 x 800
class CheesePuff(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/ethan_sheet.png", 400, 200)
		self.x = 150
		self.y = 150

		# add loadAnimation, generateAnimation, setAnimationSpeed, and playAnimation methods
		#loadAnimation(sheetX, sheetY, cellX, cellY)
		self.loadAnimation(400, 200, 100, 100)
		self.generateAnimationCycles()
		self.setAnimationSpeed(30)
		self.playAnimation()
		self.dx = 8 	
		self.dy = 9
		self.state = States.FALLING		

	def update(self, offsetX, offsetY):
		super().update(offsetX, offsetY)


	def walkBehavior(self):
		if self.scene.keysDown[Scene.K_RIGHT]:
			self.facing = 0
			self.setCurrentCycle(0)
			self.playAnimation()
			self.dx = 8
			self.state = States.WALK
		elif self.scene.keysDown[Scene.K_LEFT]:
			self.facing = 1
			self.setCurrentCycle(1)
			self.playAnimation()
			self.dx = -8
			self.state = States.WALK

	def jumpBehavior(self):
		self.stateTimer = 23
		self.dy = -6
		self.state = States.JUMP


	# Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.




#Henry's Character
# 75 x 75
#Sheet : 176 x 192 
# Animation cell: 44 x 48
class RickAstley(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/henry_sheet.png", 176, 192)
    self.dx = 9
    self.x = 50
    self.y = 50
    self.dy = 9
		#loadAnimation(sheetX, sheetY, cellX, cellY)
    self.loadAnimation(176, 192, 88, 96)
    self.generateAnimationCycles()
    self.setAnimationSpeed(30)	
    self.playAnimation()
    self.boundAction = Scene.WRAP
    self.state = States.FALLING


    

    # add loadAnimation, generateAnimation, setAnimationSpeed, and playAnimation methods

  def walkBehavior(self):
    if self.scene.keysDown[Scene.K_RIGHT]:
      self.facing = 0
      self.setCurrentCycle(0)
      self.playAnimation()
      self.dx = 9
      self.state = States.WALK
    elif self.scene.keysDown[Scene.K_LEFT]:
      self.facing = 1
      self.setCurrentCycle(1)
      self.playAnimation()
      self.dx = -9
      self.state = States.WALK

  def jumpBehavior(self):
    self.stateTimer = 20
    self.dy = -9
    self.state = States.JUMP

    
  
  def update(self, offsetX, offsetY):
    super().update(offsetX, offsetY)


  


# Kamille's Character
# 75 x 79
# Sheet: 320 x 128
# Animation Cell: 64 x 64
# change super init arguments to 320 x 128
class Kamille(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/kamille_sheet.png", 320, 128)
    self.x = 70
    self.y = 70
    self.dx += 5
    self.dy += 5
    self.boundAction = Scene.WRAP

		# add loadAnimation, generateAnimation, setAnimationSpeed, and playAnimation methods
    self.loadAnimation(320, 128, 64, 64)
    self.generateAnimationCycles()
    self.setAnimationSpeed(30)
    self.playAnimation()
    self.state = States.FALLING

  def update(self, offsetX, offsetY):
    super().update(offsetX, offsetY)

	# Add a method called walkBehavior. 
	# This should check if self.scene.keysDown[K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and 10
	# If not check if self.scene.keysDown[K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and -10
  def walkBehavior(self):
    if self.scene.keysDown[Scene.K_RIGHT]:
      self.facing = 0
      self.setCurrentCycle(0)
      self.playAnimation()
      self.dx = 5
      self.state = States.WALK
    elif self.scene.keysDown[Scene.K_LEFT]:
      self.facing = 1
      self.setCurrentCycle(1)
      self.playAnimation()
      self.dx = -5
      self.state = States.WALK
	# Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.
  def jumpBehavior(self):
    self.stateTimer = 21
    self.dy = -5
    self.state=States.JUMP



#Raphael's Character
# 112 x 67
# Sheet: 1232 x 130
# Animation cell: 112x65
class Raphael(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene,"sprites/raphael_sheet.png", 1232, 130)
    self.x = 65
    self.y = 65
    self.dx = 3
    self.dy = 3
    self.boundAction = Scene.WRAP

    self.loadAnimation(1232, 130, 112,65)
    self.generateAnimationCycles()
    self.setAnimationSpeed(30)
    self.playAnimation()
    self.state = States.FALLING

  def walkBehavior(self):
    if self.scene.keysDown[Scene.K_RIGHT]:
      self.facing = 0
      self.setCurrentCycle(0)
      self.playAnimation()
      self.dx = 5
      self.state = States.WALK
    elif self.scene.keysDown[Scene.K_LEFT]:
      self.facing = 1
      self.setCurrentCycle(1)
      self.playAnimation()
      self.dx = -5
      self.state = States.WALK

    
  def update(self, offsetX, offsetY):
    super().update(offsetX, offsetY)

  def jumpBehavior(self):
    self.startTimer = 25
    self.dy = -6


# Nelsun's Character
# 112 x 67
# Sheet: 1232 x 130
# Animation cell: 112x65
class SourCreamAndOnionPringles(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene,"sprites/nelsun_sprite.png" , 1232, 130) # change to sheet size
    self.x += 60
    self.y += 60


		# add loadAnimation, generateAnimation, setAnimationSpeed, and playAnimation methods
    self.boundAction = Scene.WRAP
    self.loadAnimation(1232, 130, 112, 65)
    self.generateAnimationCycles()
    self.setAnimationSpeed(1000)
    self.playAnimation()
    self.dx = 10
    self.dy = 8	
    self.boundAction = Scene.WRAP
    self.state = States.FALLING

  def update(self, offsetX, offsetY):
    super().update(offsetX, offsetY)

	# Add a method called walkBehavior. 
	# This should check if self.scene.keysDown[K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and 10
	# If not check if self.scene.keysDown[K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and -10

	# Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.

# Make a class that inherits character
#Sophie's Character
# 75 x 50
# Sheet: 144x64
# cell: 48x32
class Sophie(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/sophie_sprite.png", 144, 64)
    self.x += 75
    self.y += 50
    self.dx = 1
    self.dy = -1
    self.boundAction = Scene.WRAP

		# add loadAnimation, generateAnimation, setAnimationSpeed, and playAnimation methods
    self.loadAnimation(144, 64, 48, 32)
    self.generateAnimationCycles()
    self.setAnimationSpeed(30)
    self.playAnimation()
    self.dx = 1
    self.dy = -1
    self.boundAction = Scene.WRAP
    self.state = States.FALLING

  def walkBehavior(self):
    if self.scene.keysDown[Scene.K_RIGHT]:
      self.facing = Facing.RIGHT
      self.setCurrentCycle(Facing.RIGHT)
      self.playAnimation()
      self.dx = 3
    elif self.scene.keysDown[Scene.K_LEFT]:
      self.facing = Facing.LEFT
      self.setCurrentCycle(Facing.LEFT)
      self.playAnimation()
      self.dx = -3

  def jumpBehavior(self):
    self.startTimer = 50
    self.dy = -6
  def update(self, offsetX, offsetY):
    super().update(offsetX, offsetY)





app = QApplication(sys.argv)

class Spaceship(Sprite):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/spaceship100.png", 100, 100)
		self.x = 300
		self.y = 100
		self.dx = 6
		self.timer = 60
		self.enemies = []
	def checkBounds(self):

		if self.drawX < 0:
			self.dx = 6
		if self.drawX > 550:
			self.dx = -6
		self.timer -= 1
		if self.timer < 1:
			self.timer = 60
			self.enemySpawn()

		#for enemy in self.enemies:
		#	enemy.update(self.scene.offsetX, self.scene.offsetY)

	def enemySpawn(self):
		pass


class Game(Scene):
	def __init__(self):
		super().__init__(600,600)

		#self.changeBoundSize(4096, 600)

		self.offsetX = 20
		self.offsetY = 20
		self.bg0 = Background(self, "sprites/parallax-forest-back-trees.png", 1020, 600, .25, 0)
		self.bg1 = Background(self, "sprites/parallax-forest-middle-trees.png", 1020, 600, .5, 0)		
		self.bg2 = Background(self, "sprites/parallax-forest-front-trees.png", 1020, 600, .75, 0)
		self.bg3 = Background(self, "sprites/parallax-forest-lights.png", 1020, 600, 1, 0)		


		self.ground = Ground(self)

		self.sean = Sean(self)
		#self.SourCreamAndOnionPringles = SourCreamAndOnionPringles(self)
		self.kamille = Kamille(self)
		self.Rickrolled = RickAstley(self)
		self.raphael = Raphael(self)
		self.Ethan = CheesePuff(self)	#CheesePuff
		#self.CaptainPanini = CaptainPanini(self)
		self.sophie = Sophie(self)

		self.spaceship = Spaceship(self)

		
	def updateGame(self):

		

		self.bg0.update(self.offsetX, self.offsetY)
		self.bg1.update(self.offsetX, self.offsetY)
		self.bg2.update(self.offsetX, self.offsetY)
		self.bg3.update(self.offsetX, self.offsetY)

		self.ground.update(self.offsetX, self.offsetY)

		self.sean.update(self.offsetX, self.offsetY)
		self.kamille.update(self.offsetX, self.offsetY)
		self.Ethan.update(self.offsetX, self.offsetY)
		self.Rickrolled.update(self.offsetX, self.offsetY)
		self.raphael.update(self.offsetX, self.offsetY)
		self.sophie.update(self.offsetX, self.offsetY)




		self.spaceship.update(self.offsetX, self.offsetY)
		



		

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





