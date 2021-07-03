import sys
import math
from PyQt5.QtGui import QImage, QPainter, QRgba64, QColor
from PyQt5.QtCore import QTimer, QRect, QPoint


class Sprite():

	# class variables
	WRAP = 0 
	BOUNCE = 1
	STOP = 3
	DIE = 4
	CONTINUE = 5

	def __init__(self, thisScene, imageFile, xSize, ySize):
		self.width = xSize
		self.height = ySize
		self.animation = False
		self.scene = thisScene
		self.x = 0
		self.y = 0
		self.dx = 0
		self.dy = 0
		self.animationCell = 0
		self.currentSpeed = 0
		self.drawX = 0
		self.drawY = 0
		self.tick = 0
		self.animC = False
		self.debug = False

		
		# set bound action
		self.boundAction = Sprite.WRAP	
		
		# rotation variables
		self.rotated = False
		
		# if tiled sprite set up tile
		#if type(imageFile) == type(list): #better
		#if type(imageFile) == list: #worst
		if isinstance(imageFile, list): 
			self.xLength = len(imageFile)
			self.yLength = len(imageFile[0])
			self.width = xSize * self.xLength
			self.height = ySize * self.yLength 
			self.src = QImage(self.width, self.height, QImage.Format_ARGB32)
			self.src.fill(QColor("transparent"))
			qp = QPainter(self.src)
			for ix in range(0, self.xLength):
				for iy in range(0, self.yLength):
					part = QImage(imageFile[ix][iy])
					
					qp.drawImage((ix * xSize), (iy * ySize), part) 
		else:		
			# Load our file
			
			self.changeImage(imageFile)
		
		# get the width of our scene and set it to self.cWidth
		self.cWidth = thisScene.width
		
		# get the height of our scene and set it to self.cHeight
		self.cHeight = thisScene.height
		
		
		#set self.boundAction to WRAP
		self.boundAction = Sprite.WRAP
		
		self.isVisible = True
		
		
	
	# changeImage(imgFile) – Changes the image to the image file.  	
	def changeImage(self, imageFile):
		
		self.src = QImage(self.width, self.height, QImage.Format_RGB32)
		qimage = QImage(imageFile)
		scaled = qimage.scaled(self.width, self.height)
		
		self.src = scaled
		
		

	# self.cat.loadAnimation(480, 240, 80, 60)	
	# loadAnimation(width, height, cellWidth, cellHeight) Sets varialbes to slice up a sprite sheet into sprite
	def loadAnimation(self, sheetWidth, sheetHeight, cellWidth, cellHeight):
		self.animation = True
		self.animationLength = 30
		self.animationState = 0
		self.animTimer = QTimer()
		self.animTimer.timeout.connect(self.AnimTask)
		self.animCellWidth = cellWidth
		self.animCellHeight = cellHeight
		self.animSheetWidth = sheetWidth
		self.animSheetHeight = sheetHeight
		self.width = cellWidth
		self.height = cellHeight
		self.animationCell = 0
		self.test = 0
		

		
	def AnimTask(self):
		self.animationCell = self.animationCell + 1
		self.test += 1
		if self.debug == True:
			print("Celll:", self.animationCell, self.hAnimations)
		if self.animationCell > (self.hAnimations-1):
			self.animationCell = 0
			if self.debug == True:
				print("Cell:", self.animationCell, self.hAnimations)
			

	def generateAnimationCycles(self):
		# compute horizontal animations
		self.hAnimations = (int(self.animSheetWidth / self.animCellWidth))
		self.vAnimations = (int(self.animSheetHeight / self.animCellHeight))
		
		self.sheet = [[None] * self.vAnimations] * self.hAnimations
		
		if self.debug == True:
			print("Len J:" + str(len(self.sheet)))
			print("Len I:" + str(len(self.sheet[0])))
			
			
			print(self.animSheetWidth)
			print(self.animSheetHeight)		
			print(self.hAnimations)
			print(self.vAnimations)
		
		
		# this never worked quite right...		
		'''# go through columns and rows
		for i in range(0, self.vAnimations):
			for j in range(0, self.hAnimations):
				self.sheet[j][i] = QImage(self.animCellWidth, self.animCellHeight, QImage.Format_ARGB32)
				jPix = j * self.animCellWidth
				iPix = i * self.animCellHeight
				if self.debug == True:					
					print("I:"+ str(i))				
					print("J:" + str(j))
					print("J pix:", jPix )
					print("I pix:", iPix )	
				#qp = QPainter(self.sheet[j][i])				
				#qp.drawImage(QRectF(0, 0, self.animCellWidth, self.animCellHeight), self.src, QRectF(jPix, iPix, self.animCellWidth, self.animCellHeight))			
				self.sheet[j][i] = self.src.copy(QRect(jPix, iPix, self.animCellWidth, self.animCellHeight))
				
				#del qp'''
				
				

			
		

		
	# renameCycles(cycleNameArray) This method allows you to set string names to each of the cycles. 
	# Typically these will indicate directions or behaviors.
	def renameCycles(self, cycleNameArray):
		pass
	
	# setAnimationSpeed(speed) – This method indicates how quickly the animation will cycle. Setting a higher value 
	# will slow down the animation.
	def setAnimationSpeed(self, speed):
		self.speed = speed
		
	# setCurrentCycle(cycleName) – Changes the animation cycle to the one indicated by the cycle name. 
	# Normally used to change animation state.
	#def setCurrentCycle(self, cycleName):
	#	pass
	
	# setCurrentCycle(cycleState) – Changes the animation cycle to the one indicated by the number. 
	def setCurrentCycle(self, state):
		self.animationState = state
		
	# playAnimation() - begins (and repeats) the currently indicated animation.
	def playAnimation(self):
		self.animTimer.stop()
		self.animTimer.start(self.speed)
		
	
	# pauseAnimation() - Pauses the animation until it is re-started with a playAnimation() command.
	def pauseAnimation(self):
		self.animTimer.stop()
		
		
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
		
		if self.debug == True:
			print ("update", self.animationCell) 
			
		
		if self.isVisible:
				self.draw(offX, offY)


		
	def draw(self, offX, offY):
				
		 
		self.drawX	= self.x - int(self.width/2) - offX
		self.drawY = self.y - int(self.height/2) - offY


					

		if self.rotated:
			pass
		else:
			if self.animation == False:
				qp = QPainter(self.scene)
				qp.drawImage(self.drawX, self.drawY, self.src)
			else:
				qp = QPainter(self.scene)
				if self.debug == True:
					#print("selfa:" , self.animationCell)
					#print("test:", self.test)
					#qp.drawImage(self.drawX, self.drawY, self.sheet[0][self.animationState])
					#qp.drawImage(self.drawX + 80, self.drawY, self.sheet[1][self.animationState])
					#qp.drawImage(self.drawX + 160, self.drawY, self.sheet[2][self.animationState])
					#qp.drawImage(self.drawX + 240, self.drawY, self.sheet[3][self.animationState])
					#qp.drawImage(self.drawX + 320, self.drawY, self.sheet[4][self.animationState])
					qp.drawImage(QPoint(self.drawX, self.drawY), self.src, QRect(self.animationCell * self.animCellWidth, self.animCellHeight*self.animationState, self.animCellWidth, self.animCellHeight))
									
				else:
					qp.drawImage(QPoint(self.drawX, self.drawY), self.src, QRect(self.animationCell * self.animCellWidth, self.animCellHeight*self.animationState, self.animCellWidth, self.animCellHeight))

					
				del qp
			
					
	def updateAnim(self):
		if self.debug == True:
			print("updateanime cell:", self.animationCell)
		self.tick += 1
		if self.tick >= self.animationLength:
			
			self.tick = 0			
			self.AnimTask()
			
		return self.animationCell
			
						

		
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
				print("Error")

				
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
		
	def setMoveAngle(self, degrees):
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
				collision = True
				
				# determine if there's a miss
				if ((left > spriteRight) or (top > spriteBottom) or (right < spriteLeft) or (bottom < spriteTop)):
					collision = False	

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
		
		

		
	def setSpeed(self, speed):
		self.currentSpeed = speed
		self.calcVector()
		
	# moves the sprite to x and y coordinates
	def setPosition(self, xNew, yNew):
		self.x = xNew;
		self.y = yNew;
		
		
	def setCPos(self, xNew, yNew):
		self.x = int(xNew + (self.width/2))
		self.y = int(yNew + (self.height/2))
		

	def calcVector(self):
		self.dx = (int(self.currentSpeed * math.cos(math.radians(self.moveAngle))))
		self.dy = (int(self.currentSpeed * math.sin(math.radians(self.moveAngle))))


	# changes the angle the image is drawn
	def setImgAngle(self, degrees):
		# offset degrees to compensate for monitor weirdness
		degrees = degrees - 90;
		self.imgAngle = degrees * math.pi / 180
		
		# process the image
		if self.imgAngle == 0:
			rotated = False		
		else:
			rotated = True
		