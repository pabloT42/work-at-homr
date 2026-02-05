import pygame
import random
pygame.init()
pygame.display.set_caption("platformer with inheritance")
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
clock = pygame.time.Clock()
gameover = False
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
GREEN = (0, 200, 0)



class Player:
    
    def __init__(self, x, y): #constructor
        self.x = x
        self.y = y
        self.w = 40
        self.h = 60
        self.vy = 0
        self.on_ground = False

    def handle_input(self, keys): #keyboard input
        if keys[pygame.K_RIGHT]:
            self.x += 5
        elif keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vy = -12
            self.on_ground = False

    def apply_gravity(self): #make player fall
        self.vy += GRAVITY
        self.y += self.vy

    def check_collision(self, platforms): 
        self.on_ground = False #assume we're in the air, change if not
        for plat in platforms: #check all the platforms in the list
            if self.is_colliding(plat): #if we ARE colliding, reset feet to top of platform...
                if self.y + self.h <= plat.y + self.vy:
                    self.y = plat.y - self.h
                    self.vy = 0
                    self.on_ground = True

    def is_colliding(self, plat): #bounding box collision
        if self.x + self.w > plat.x and self.x < plat.x + plat.w and self.y + self.h > plat.y and self.y < plat.y + plat.h:
            return True
        else:
            return False
        

    def update(self, platforms): #funtion that calls a bunch of other functions (keeps game loop more simple)
        self.apply_gravity()
        self.check_collision(platforms)

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, (self.x, self.y, self.w, self.h))



#parent class
class platform():
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos= ypos
        
    def draw(self):
        pygame.draw.rect(screen, (100, 50, 100), (self.xpos, self.ypos, 80, 30))
        
    def move(self):
        pass
    
#child class #1
class MovingBlock(platform):
    def __init__(self, xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.startX = self.xpos
        self.startY = self.ypos
        self.direction = 1
        
    def draw(self):
        pygame.draw.rect(screen, (200,50,100), (self.xpos, self.ypos, 80, 30))
        
    def move(self):
        if self.direction == 1:
            if self.xpos < self.startX:
                self.direction*=-1
            else:
                self.xpos-=.1
        else:
            if self.xpos > self.startX+200:
                self.direction*=-1
            else:
                self.xpos+=.1
                
class IceBlock(platform):
    def __init__(self, xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.startX = self.xpos
        self.startY = self.ypos
        
    def draw(self):
        pygame.draw.rect(screen, (112,202,209), (self.xpos, self.ypos, 80, 30))
    
class Trampoline(platform):
    def __init__(self, xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.startX = self.xpos
        self.startY = self.ypos
        
    def draw(self):
        pygame.draw.rect(screen, (123,123,125), (self.xpos, self.ypos, 80, 30))
        
class BreakBlock(platform):
    def __init__(self, xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.startX = self.xpos
        self.startY = self.ypos
        
    def draw(self):
        pygame.draw.rect(screen, (188,74,60), (self.xpos, self.ypos, 80, 30))
    
        
    
                
                
# maaaaaaaaain0

#insatiate some objects


plats = []
for i in range(5):
    plats.append(platform(random.randrange(50, 700), random.randrange(50,700)))
for i in range(4):
    plats.append(IceBlock(random.randrange(50,500), random.randrange(50,500)))
for i in range(3):
    plats.append(MovingBlock(random.randrange(50,500), random.randrange(50,500)))
for i in range(2):
    plats.append(Trampoline(random.randrange(50,500), random.randrange(50,500)))
for i in range(1):
    plats.append(BreakBlock(random.randrange(50,500), random.randrange(50,500)))
    
player = Player(100,100)

while(1): #lame goop
    for i in range(len(plats)):
        plats[i].move()
    
    #render sectiooon
    screen.fill((0,0,0))
    for i in range(len(plats)):
        plats[i].draw()
   
    
    pygame.display.flip()
    
pygame.quit()
