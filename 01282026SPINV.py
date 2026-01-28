import pygame

pygame.init()
pygame.display.set_caption("space invaders")
ipad = pygame.display.set_mode((800,800))
duration = pygame.time.Clock()
gameover = False
timer = 0
shoot = False


#player variables
xpos = 400
ypos = 750
moveLeft = False
moveRight = False



class Alien:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
        self.direction = 1
    def draw(self):
        if self.isAlive == True:
            pygame.draw.rect(ipad, (25,25,25), (self.xpos, self.ypos, 40, 40))
    def move(self, time):
        
        if timer%800==0:
            self.ypos += 100
            self.direction *= -1
            return 0
        
        if timer%100==0:
            self.xpos+=50*self.direction
        
        return timer
    def collide(self, BulletX, BulletY):
        if self.isAlive:
            if BulletX > self.xpos:
                if BulletX < self.xpos + 40:
                    if BulletY < self.ypos + 40:
                        if BulletY > self.ypos:
                            print("hit")
                            self.isAlive = False
                            return False
        return True


armada = []
for i in range (4):
    for j in range(9):
        armada.append(Alien(j*80+60, i*70+50))
        
class Bullet:
    def __init__(self, xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = False
        
    def move(self, xpos, ypos):
        if self.isAlive == True:
            self.ypos-=5
        if self.ypos < 0:
            self.isAlive = False
            self.xpos = xpos
            self.ypos = ypos
            
    def draw(self):
        pygame.draw.rect(ipad, (150,150,150), (self.xpos, self.ypos, 3, 20))
        
bullet = Bullet(xpos+28, ypos)


class Wall:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.numHits = 0
    
    def draw(self):
        if self.numHits == 0:
            pygame.draw.rect(ipad, (255,255,20), (self.xpos, self.ypos, 30, 30))
        if self.numHits == 1:
            pygame.draw.rect(ipad, (150,150,10), (self.xpos, self.ypos, 30, 30))
        if self.numHits == 2:
            pygame.draw.rect(ipad, (50,50,0), (self.xpos, self.ypos, 30, 30))
            
    def collide(self, BulletX, BulletY):
        if self.numHits < 3:
            if BulletX > self.xpos:
                if BulletX < self.xpos + 40:
                    if BulletY < self.ypos + 40:
                        if BulletY > self.ypos:
                            print("hit")
                            self.numHits += 1
            
walls = []
for k in range(4):
    for i in range(2):
        for j in range(3):
            walls.append(Wall(j*30+200*k+50, i*30+600))
            
            
class missile:
    def __init__(self):
        self.xpos = (-10,-10)
        self.ypos = (-10,-10)
        self.isAlive = False
        
    def move(self):
        if self.isAlive == True:
            self.ypos+=5
        if self.ypos > 800:
            self.isAlive = False
            self.xpos = (-10,-10)
            self.ypos = (-10,-10)
            
    def draw(self):
        pygame.draw.rect(ipad, (0,45,4), (self.xpos, self.ypos, 3, 20))
        
missiles = []
for i in range(1):
    for j in range(10):
        missiles.append(missile)
                     


while not gameover: #game loop-----------------------------
    duration.tick(60)
    timer += 1
    
    
    #input section-----------------------------------------------------------------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveRight = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moveRight = False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shoot = False
    
    
    #physics section---------------------------------------------------------------------------------------------------------------------------------------------------
    if moveLeft == True:
        vx =- 3
    elif moveRight == True:
        vx =+ 3
    else:
        vx = 0
        
    for i in range (len(armada)):
        timer = armada[i].move(timer)
        
    for i in range (len(missiles)):
        missiles[i].move()
    
    #update player pos  
    xpos += vx
    
    if shoot == True:
        bullet.isAlive = True
    if shoot == False:
        bullet.isAlive = False
        
    if bullet.isAlive == True:
        bullet.move(xpos+28, ypos)
        if bullet.isAlive == True:
            for i in range (len(armada)):
                bullet.isAlive = armada[i].collide(bullet.xpos, bullet.ypos)
                if bullet.isAlive == False:
                    break
                
            #walls    
        if bullet.isAlive == True:      
            for i in range (len(walls)):
                bullet.isAlive = walls[i].collide(bullet.xpos, bullet.ypos)
                if bullet.isAlive == False:
                    break
    else:
        bullet.xpos = xpos+28
        bullet.ypos = ypos
    
    #render section----------------------------------------------------------------------------------------------------------------------------------------
    
    ipad.fill((255,255,255))
    
    pygame.draw.rect(ipad, (200,200,100), (xpos, ypos, 60, 20))
    
    
    
    
    for i in range (len(armada)):
            armada[i].draw()
        
    for i in range (len(walls)):
            walls[i].draw()
            
    for i in range (len(missiles)):
            missiles[i].draw()
        
    bullet.draw()
    
    pygame.display.flip()
    
#end of game loop-----------------------------------------
    
pygame.quit()
