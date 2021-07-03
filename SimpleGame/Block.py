from SimpleGame.Sprite import Sprite

class Block(Sprite):
	def __init(self, thisScene, imageFile, xSize, ySize):
		super().__init__(thisScene, imageFile, xSize, ySize)	
		self.scrollAmount = 0
		self.isLeft = False
		self.isRight = False
		self.isAbove = False
		self.isBelow = False
	
	# 	collideswith(Sprite) - checks for collision with another sprite, pushes sprite back because it's a block
	def collidesWith(self, sprite):
		collision = False
		
		if self.isVisible:
			if sprite.isVisible:
				# check borders
				left = int(self.x - (self.width / 2))
				top = int(self.y - (self.height / 2))
				right = int(self.x + (self.width / 2))
				bottom = int(self.y + (self.height / 2))
				spriteLeft = int(sprite.x - (sprite.width / 2))
				spriteTop = int(sprite.y - (sprite.height / 2))
				spriteRight = int(sprite.x + (sprite.width / 2))
				spriteBottom = int(sprite.y + (sprite.height / 2))
				
			
				# assume collision
				collision = True
				

				# calculate amounts
				amountLeft = left - spriteRight
				amountAbove = top - spriteBottom
				amountRight = spriteLeft - right
				amountBelow = spriteTop - bottom
				
				# determine if there's a miss
				if ((left > spriteRight) or (top > spriteBottom) or (right < spriteLeft) or (bottom < spriteTop)):
					collision = False	
				
				
				# amountLeft is highest
				if (amountLeft > amountRight and amountLeft > amountAbove and amountLeft > amountBelow):
					self.isLeft = True
					self.isRight = False
					self.isAbove = False
					self.isBelow = False
				elif (amountRight > amountBelow and amountRight > amountAbove):
					self.isRight = True
					self.isLeft = False
					self.isAbove = False
					self.isBelow = False				
				elif (amountBelow > amountAbove):
					self.isBelow = True
					self.isLeft = False
					self.isAbove = False
					self.isRight = False				
				else:
					self.isAbove = True
					self.isLeft = False
					self.isBelow = False
					self.isRight = False				
				
				
				#move the sprite back
				if collision == True:
					if self.isBelow and (bottom > spriteTop):
						sprite.y = (sprite.y + (bottom - spriteTop))
					elif self.isAbove and (top < spriteBottom):
						sprite.y = (sprite.y - (spriteBottom - top))
						sprite.dy = 0				
					elif self.isLeft and (left < spriteRight):
						sprite.x = (sprite.x - (spriteRight - left))
						sprite.dx = 0				
					elif self.isRight and (right > spriteLeft):
						sprite.x = (sprite.x + (right - spriteLeft))	
						sprite.dx = 0						
						

			
		return collision
		
		
	# returns true if the bottom of one sprite is on top of a block
	def standingOn(self, sprite):	
		left = int(self.x - (self.width / 2))
		top = int(self.y - (self.height / 2))
		right = int(self.x + (self.width / 2))
		spriteLeft = int(sprite.x - (sprite.width / 2))
		spriteRight = int(sprite.x + (sprite.width / 2))
		spriteBottom = int(sprite.y + (sprite.height / 2))
		standing = False		
		
		# we need a NOR
		if not ((left > spriteRight) and (right < spriteLeft)):
			if top == spriteBottom:
				standing = True
			
		return standing		

	
	
