import sys
import math
from PySide2.QtGui import QImage, QPainter
from PySide2.QtCore import QTimer


class Sprite():

	# class variables
	WRAP = 0 
	BOUNCE = 1
	STOP = 3
	DIE = 4
	CONTINUE = 5

	def __init__(self, thisScene, imageFile, xSize, ySize):
		self.width=xSize
		self.height=ySize
		self.animation = False
		self.scene = thisScene
		self.x = 0
		self.y = 0
		self.dx = 0
		self.dy = 0
		
		# set bound action
		self.boundAction = Sprite.WRAP	
		
		# rotation variables
		self.rotated = False
		
		
		# Load our file
		self.file = QImage(imageFile)
		
		# get the width of our scene and set it to self.cWidth
		self.cWidth = thisScene.width
		
		# get the height of our scene and set it to self.cHeight
		self.cHeight = thisScene.height
		
		
		#set self.boundAction to WRAP
		self.boundAction = Sprite.WRAP
		
		self.isVisible = True
	
	# changeImage(imgFile) – Changes the image to the image file.  	
	def changeImage(self):
		pass
		
	# loadAnimation(width, height, cellWidth, cellHeight) Sets varialbes to slice up a sprite sheet into sprite
	def loadAnimation(self, sheetWidth, sheetHeight, cellWidth, cellHeight):
		self.animation = true
		self.animationLength = 1000
		self.animationState = 0
		#self.animTimer = new QTimer()
		#self.animTimer.timeout.connect(self.animationLength)
		self.animCellWidth = cellWidth
		self.animCellHeight = cellHeight
		self.animSheetWidth = sheetWidth
		self.animSheetHeight = sheetHeight
		self.width = cellWidth
		self.height = cellHeight
		
	'''// generateAnimationCycles() sets up animation cycles based on horizontal and vertical rows and columns.
	public void generateAnimationCycles()
	{
		// compute horizontal animations
		hAnimations = (int)(animSheetWidth / animCellWidth);
		vAnimations = (int)(animSheetHeight / animCellHeight);
		
		sheet = new BufferedImage[hAnimations][vAnimations];
		
		// go through columns and rows
		for (int i = 0; i < vAnimations; i++) {
			for (int j = 0; j < hAnimations; j++) {
				sheet[j][i] = src.getSubimage(j * animCellWidth, i * animCellHeight, animCellWidth, animCellHeight);
			}		
		}	
	}'''		
		
	# generateAnimationCycles() sets up animation cycles based on horizontal and vertical rows and columns
	def generateAnimationCycle(self):
		pass
		
	# renameCycles(cycleNameArray) This method allows you to set string names to each of the cycles. 
	# Typically these will indicate directions or behaviors.
	def renameCycles(self, cycleNameArray):
		pass
	
	# setAnimationSpeed(speed) – This method indicates how quickly the animation will cycle. Setting a higher value 
	# will slow down the animation.
	def setAnimationSpeed(self, speed):
		pass
		
	# setCurrentCycle(cycleName) – Changes the animation cycle to the one indicated by the cycle name. 
	# Normally used to change animation state.
	def setCurrentCycle(self, cycleName):
		pass
	
	# setCurrentCycle(cycleState) – Changes the animation cycle to the one indicated by the number. 
	def setCurrentCycle(self, state):
		self.animationState = state;
		
	# playAnimation() - begins (and repeats) the currently indicated animation.
	def playAnimation(self):
		pass
	
	# pauseAnimation() - Pauses the animation until it is re-started with a playAnimation() command.
	def pauseAnimation(self):
		pass
		
	# setImage(fileName) – Another name for changeImage(). Works exactly like changeImage()
	def setImage(self, imageFile):
		self.changeImage(imageFile)
	
	
	# hides the sprite
	def hide(self):
		self.isVisible = False	
	
	# unhides the sprite
	def show(self):
		self.isVisible = True

	# report is a utility for debugging info to the console
	def report(self):
		print("x: " + self.x + ", y:" + self.y + ", dx: " + self.dx + ", dy: " + self.dy + ", speed:" + self.currentSpeed + ", angle: " + self.moveAngle) 				
		
		

	
	def update(self, offX = 0, offY = 0):
		self.x += self.dx
		self.y += self.dy
		
		self.checkBounds()
		
		if self.isVisible:
				self.draw(offX, offY)
		
	def draw(self, offX, offY): 
		drawX	= self.x - int(self.width/2) - offX
		drawY = self.y - int(self.height/2) - offY
		
		if self.rotated:
			pass
		else:
			if self.animation == False:
				qp = QPainter(self.scene)
				qp.drawImage(drawX, drawY, self.file)
			else:
				pass			
					
				

		
	def checkBounds(self):
		# make leftBorder, rightBorder, topBorder, and bottomBorder		
		leftBorder = 0
		rightBorder = self.cWidth
		topBorder = 0
		bottomBorder = self.cHeight
		
		# set offRight, offLeft, offTop, and offBottom to False
		offRight = False
		offLeft = False
		offTop = False
		offBottom = False
	
		# check each border
		if self.x > rightBorder:
			offRight = True
		if self.x < leftBorder:
			offLeft = True
		if self.y > bottomBorder:
			offBottom = True
		if self.y < topBorder:
			offTop = True
			
		if self.boundAction == Sprite.WRAP:
			if offLeft:
				self.x = rightBorder
			if offTop:
				self.y = bottomBorder
			if offRight:
				self.x = leftBorder	
			if offBottom:
				self.y = topBorder
				

				
		# deflects
		if self.boundAction == Sprite.BOUNCE:
			if offLeft:
				self.dx *= -1
				self.calcSpeedAngle()
				self.imgAngle = self.moveAngle
			if offTop:
				self.dy *= -1
				self.calcSpeedAngle()
				self.imgAngle = self.moveAngle				
			if offRight:
				self.dx *= -1
				self.calcSpeedAngle()
				self.imgAngle = self.moveAngle
			if offBottom:
				self.dy *= -1
				self.calcSpeedAngle()
				self.imgAngle = self.moveAngle
		
		if self.boundAction == Sprite.STOP:
			if offLeft or offRight or offTop or offBottom:
				self.setSpeed(0)
				
		if self.boundAction == Sprite.DIE:
			if offLeft or offRight or offTop or offBottom:
				self.setSpeed(0)
				self.hide()

	def changeImageAngle(self, degrees):
		self.imgAngle += (degrees * math.pi / 180)
		
		if self.imgAngle == 0:
			rotated = False
		else:
			rotated = True
			
	def getImgAngle(self):
		degrees = self.imgAngle * 180 / math.pi
		degrees = degrees + 90
		return degrees
		
	def setMoveAngle(self):
		degrees = degrees - 90
		self.moveAngle = degrees * math.pi / 180
		self.calcVector()
	
	# changeMoveAngleBy(degrees) changes the movement angle by the indicated amount	
	def changeMoveAngle(self, degrees):
		self.moveAngle += (degrees * math.pi / 180)
		calcVector
		
	# getMoveAngle() returns the sprite's motion angle in degrees
	def getMoveAngle(self):
		degrees = self.moveAngle * 180 / math.pi
		degrees = degrees + 90
		return degrees
	
	# setAngle(degrees) changes both the image and motion angle. Allows both to go in same direction.
	def setAngle(self, degrees):
		self.setMoveAngle(degrees)
		self.setImgAngle(degrees)

	# changeAngleBy(degrees) changes both the image and motion angles by degrees
	def changeAngleBy(self, degrees):
		self.changeMoveAngle(degrees)
		self.changeImgAngle(degrees)
		
	# turnBy(degrees) calls changeangleBy(degrees)
	def turnBy(self, degrees):
		self.changeAngleBy(degrees)

	# addVector(degrees, thrust) - allows you to add a motion vector to the sprite.	
	def addVector(self, degrees, thrust):			
		# offset angle by 90 degrees, because the original does this but I should ask andy why
		degrees -= 90
		
		# convert degrees to radians
		angle = degrees * math.pi / 180
		
		#  calculate new dx and dy
		newDX = (thrust * math.cos(angle))
		newDY = (thrust * math.sin(angle))
		self.dx += newDX;
		self.dy += newDY;
		
		self.calcSpeedAngle()

	# setBoundAction(action) sets the boundAction to one of the integers supplied in both classes
	def setBoundAction(self, action):
		self.boundAction = action	

	# collideswith(Sprite) - checks for collision with another sprite
	def collidesWith(self, sprite):
		# coollisions only happen when both are visible
		collision = False
		
		if self.isVisible:
			if sprite.visible:
				# check borders
				left = self.x - (self.width / 2)
				top = self.y - (self.height / 2)
				right = self.x + (self.width / 2)
				bottom = self.y + (self.height / 2)
				spriteLeft = sprite.x - (sprite.width / 2)
				spriteTop = sprite.y - (sprite.height / 2)
				spriteRight = sprite.x + (sprite.width / 2)
				spriteBottom = sprite.y + (sprite.height / 2)
				
				# assume collision
				collision = true
				
				# determine if there's a miss
				if ((left > spriteRight) or (top > spriteBottom) or (right < spriteLeft) or (bottom < spriteTop)):
					collision = false	

		return collision


	# visible tells us if the sprite is visible
	def visible(self):
		return self.isVisible
	

	# distanceTo(sprite) determines the distance between two sprites, in pixels
	def distanceTo(sprite):
		distance = (int((math.sqrt((sprite.x - self.x)^2 + (sprite.y - self.y)^2))))
		
		return distance

	# angleto(sprite) returns the angle (in degrees) from the current sprite to the given sprite
	def angleTo(sprite):
		radians = math.atan2((self.y - sprite.y),(self.x - sprite.x))
		degrees = radians * 180 / math.pi
		
		return degrees

	





	





	
	# sets speed and moveAngle based on dx and dy
	def calcSpeedAngle(self):
		self.currentSpeed = math.sqrt((self.dx * self.dx) + (self.dy * self.dy))
		self.moveAngle = math.atan2(self.dx, self.dy)
		
		

		
	def setSpeed(self):
		pass
		