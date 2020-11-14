import sys,os, pygame
import time
from Ship import ships


pygame.init()
pygame.image.get_extended()
player = pygame.image.load(os.path.join('Gamesprites','player.png'))
icon = pygame.image.load(os.path.join('Gamesprites','icon.png'))
humanshuttle = pygame.image.load(os.path.join('Gamesprites','Shuttle.png'))
shot = pygame.image.load(os.path.join('Gamesprites','shot.png'))
saucer = pygame.image.load(os.path.join('Gamesprites','Saucer.png'))
tigfighter = pygame.image.load(os.path.join('Gamesprites','fighter.png'))
basicsaucer = pygame.image.load(os.path.join('Gamesprites','row1.png'))
t = width, height = 400,400

gameclock = pygame.time.Clock()
mytime = time.clock()

mywindow = pygame.display.set_caption("space invaderes")
mywindow = pygame.display.set_icon(icon)
mywindow = pygame.display.set_mode(t)



player = ships(1,humanshuttle,4,360)
player.setPlayerx(400/2)


def LoadShip():
    mywindow.blit(player.image,(player.x,player.y))
    mywindow.blit(tigfighter,(150,100))
    mywindow.blit(basicsaucer,(50,50))
  

def Render():
    mywindow.blit(player.image,(player.x,player.y))
    mywindow.blit(tigfighter,(150,100))
    mywindow.blit(basicsaucer,(50,50))
    if player.x >= 360:
        player.x = 360
    if player.x <= 1:
        player.x = 2
    mytime = time.clock()


run = 1 
LoadShip()



while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mytime = mytime +.0001
                if mytime > 5:
                    mytime= .000001
                player.x =  player.x + (mytime/60) 
            elif event.key == pygame.K_LEFT:
                mytime = mytime +.0001
                if mytime > 5:
                    mytime= .000001
                player.x = player.x -(mytime/60) 
                
        print (mytime)
        

        Render()
        pygame.display.flip()
        mywindow.fill((0,0,0))

		

