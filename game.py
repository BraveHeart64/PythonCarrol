import sys,os, pygame
import time
from Ship import ships



pygame.init()
pygame.image.get_extended()
t = pygame.image.load(os.path.join('Gamesprites','player.png'))
icon = pygame.image.load(os.path.join('Gamesprites','icon.png'))
humanshuttle = pygame.image.load(os.path.join('Gamesprites','Shuttle.png'))
shot = pygame.image.load(os.path.join('Gamesprites','shot.png'))
saucer = pygame.image.load(os.path.join('Gamesprites','Saucer.png'))
tigfighter = pygame.image.load(os.path.join('Gamesprites','fighter.png'))
basicsaucer = pygame.image.load(os.path.join('Gamesprites','row1.png'))
t = width, height = 400,400
gameclock = pygame.time.Clock()
mytime = time.clock()

mywindow = pygame.display.set_caption("Mele Combat")
mywindow = pygame.display.set_icon(icon)
mywindow = pygame.display.set_mode(t)
player = ships(1,humanshuttle,4,360)
player.setPlayerx(400/2)




def LoadShip():
    mywindow.blit(player.image,(player.x,player.y))
    mywindow.blit(tigfighter,(150,100))
    mywindow.blit(basicsaucer,(50,50))
    


def InBounds():
	if player.x >= 360:
		player.x = 360
		
	if player.x <= 1:
		player.x = 2
		
    
	


def Render():
    mywindow.blit(player.image,(player.x,player.y))
    mywindow.blit(tigfighter,(150,100))
    mywindow.blit(basicsaucer,(50,50))
    mytime = time.clock()
    InBounds()





run = 1 
LoadShip()

# need to spin the image without moving the image us the raduis to do this maybe

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               
               player.turnRight(player.x)
               print(player.angle)
          
               rotated_image = pygame.transform.rotate(humanshuttle, player.getRigntAngel())
               player = ships(player.turnRight,rotated_image,player.x,player.y)
               
              
               if mytime > 5:
				   mytime= .000001
                    
               player.x =  player.x + (mytime/60) 
               
               
               
            if event.key == pygame.K_ESCAPE:
				sys.exit()	
				   
            if event.key == pygame.K_LEFT:
				#angle = player.turnLeft()
				
				rotated_image = pygame.transform.rotate(humanshuttle,player.turnLeft(player.x))
				player = ships(player.turnLeft,rotated_image,player.x,player.y)
				player.x = player.x -(mytime/60)
				
	
            if event.key == pygame.K_UP:
				mytime = mytime +.0001
                
        #print (mytime)
        #print(player.angle)

        Render()
        pygame.display.flip()
        mywindow.fill((0,0,0))

		

