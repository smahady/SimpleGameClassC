from SimpleGame.Sprite import Sprite

class Background(Sprite):
	def __init__(self, thisScene, imageFile, xSize, ySize, scrollX = 0, scrollY = 0):
		super().__init__(thisScene, imageFile, xSize, ySize)		
		self.scrollAmountX = scrollX
		self.scrollAmountY = scrollY
		self.setBoundAction(Sprite.CONTINUE)

		
	def update(self, offX = 0, offY = 0):

		externX = int(offX * self.scrollAmountX)
		externY = int(offY * self.scrollAmountY)		
		
		
		for ix in range((externX * -1), self.cWidth, self.width):
			for iy in range((externY * -1),self.cHeight, self.height):
				self.setPosition(ix + self.width/2, iy + self.height/2)
				super().update()