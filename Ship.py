# this class will load the ships and prepare to be used to dance on the screen
class ships():
    def __init__(self, power, image,x,y):
        self.x = x
        self.y = y
        self.image = image
        self.power = power
        self.speed = 1
       

    def setPlayerx(self, x):

        self.x = x
