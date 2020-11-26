# this class will load the ships and prepare to be used to dance on the screen



class ships():
			
	def __init__(self, power, image,x,y):
		self.x = x
		self.y = y
		self.image = image
		self.power = power
		#self.speed = 1
		self.angle = 0
		self.scale = 0
        
       
	def setPlayerx(self, x):
		self.x = x
        
	def loadImage(self, image):
		self.image = image
		
	def addPlayerX(self, x):
		self.x+=x
		
		
	def turnRight(self,an):
		self.angle -=an
		self.angle = an
		return an


	def getRigntAngel(self):
		return int(self.angle)
		
		


	def turnLeft(self , an):
		self.angle += an
		self.angle = an
		print(self.angle)
		return self.angle 