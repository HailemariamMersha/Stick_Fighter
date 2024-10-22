add_library('minim')
import os
import random
#yes
PATH = os.getcwd()
RESOLUTION_X = 1000
RESOLUTION_Y = 600 
kick = "kick"
punch = "punch"
block = "block"

class Fighter:
    def __init__(self, x,y,w,h,health,img, slice_w, slice_h, shift):
        self.shift = shift 
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.w = w
        self.h = h
        self.img = loadImage(PATH + "/Sprites/" + img)
        self.health = health
        self.key_handler = {LEFT:False, RIGHT:False, UP:False, kick:False, punch:False, block:False}
        self.g = 490
        self.health_bar = 100
        self.slice_w = slice_w
        self.slice_h = slice_h
        self.num_slices = 0
        self.slice = 0
        self.dir = RIGHT
        self.walking = True 
        self.kicking = False
        self.punching = False 
        self.blocking = False
        self.attacking = self.punching or self.kicking 
    def display(self):
        self.move()
        fill(255,0,0)
        #rect(self.x, self.y, self.w, self.h)
        fill(0,255,0)
        rect(self.health, 30, self.health_bar, 10)
        if self.dir == RIGHT:
            if self.walking:
                self.num_slices = 6
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h, 194 * 7 + self.slice * self.slice_w, 0, 194 * 7 + (self.slice + 1)* self.slice_w, self.slice_h)
            elif self.punching:
                self.num_slices = 7
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h,  -30 + self.slice * self.slice_w, 0, -30 + (self.slice + 1) * self.slice_w, self.slice_h )
            elif self.kicking == True:
                self.num_slices = 4
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h,190*10 + self.slice * self.slice_w, 0, 190 * 10+(self.slice + 1)* self.slice_w, self.slice_h)
            elif self.blocking == True:
                self.num_slices = 3
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h, 194 * 15 + self.slice * self.slice_w, 0, 194 * 15 + (self.slice + 1)* self.slice_w, self.slice_h)
        elif self.dir == LEFT:
            if self.walking:
                self.num_slices = 6
                image(self.img, self.x - self.shift  , self.y + 50, self.slice_w, self.slice_h, 194 * 7 + (self.slice + 1) * self.slice_w, 0, 194 * 7 + self.slice * self.slice_w, self.slice_h)
            if self.punching:
                self.num_slices = 7
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h,-30 + (self.slice + 1) * self.slice_w, 0, -30 + self.slice * self.slice_w, self.slice_h )    
            elif self.kicking:
                self.num_slices = 4
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h, 190 *10 + (self.slice + 1) * self.slice_w, 0, 190 *10 + self.slice * self.slice_w, self.slice_h)
            elif self.blocking:
                self.num_slices = 3
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h, 194 * 15 + (self.slice + 1) * self.slice_w, 0, 194 * 15 + self.slice * self.slice_w, self.slice_h)
    def kick(self):
        if game.fighter_1.x + self.w >= game.fighter_2.x:
            if game.fighter_1.health_bar > 0 and game.fighter_2.kicking:
                game.fighter_1.health_bar -= 5
            if game.fighter_2.health < RESOLUTION_X - 20 and game.fighter_1.kicking:
                game.fighter_2.health += 5
                game.fighter_2.health_bar -= 5
    def punch(self):
        if game.fighter_1.x + self.w >= game.fighter_2.x:
            if game.fighter_1.health_bar > 0 and game.fighter_2.punching:
                game.fighter_1.health_bar -= 5
            if game.fighter_2.health < RESOLUTION_X - 20 and game.fighter_1.punching:
                game.fighter_2.health += 5
                game.fighter_2.health_bar -= 5
    def block(self):
        if game.fighter_1.x + self.w >= game.fighter_2.x:
            if game.fighter_1.health_bar > 0 and game.fighter_1.attacking:
                game.fighter_1.health_bar += 5
            if game.fighter_2.health < RESOLUTION_X - 20 and game.fighter_1.attacking:
                game.fighter_2.health -= 5
                game.fighter_2.health_bar += 5
                
        
    def move(self):
        #gravity 
        
        if self.y + self.h >= self.g:  
            self.vy = 0 
        else:
            self.vy += 5
            
        if self.key_handler[LEFT] == True:
            self.vx = -7
            if game.fighter_2.x <= self.w + game.fighter_1.x:
                game.fighter_2.vx = 0
            self.dir = LEFT
        elif self.key_handler[RIGHT] == True:
            self.vx = 7
            if game.fighter_1.x + self.w >= game.fighter_2.x:
                game.fighter_1.vx = 0
            self.dir = RIGHT
            
        else:
            self.vx = 0
        if self.key_handler[UP] == True and self.y + self. h == self.g:
            self.vy = -50
    
        #checks edges of the screen 
        if self.x + self.vx < 0:
            self.vx = -self.x
        if self.x + self.w + self.vx > RESOLUTION_X:
            self.vx = RESOLUTION_X - self.w - self.x 
        if frameCount % 10 == 0 and self.vx != 0: 
            self.slice = (self.slice + 1) % self.num_slices
        elif self.vx == 0:
            self.slice = 6
            
            
        self.x += self.vx
        self.y += self.vy 
        
        #attacks 
        if frameCount % 60 == 0:
            if self.key_handler[kick] == True:
                self.kick()
            elif self.key_handler[punch] == True:
                self.punch()
            elif self.key_handler[block] == True:
                self.block()
        elif self.key_handler[block] == True:
            pass
            #blcok
        elif self.key_handler[punch] == True:
            pass
            #punch 
        
            
class Game:
    def __init__(self):
        self.fighter_1 = Fighter(200,310,80,180, 20, "3.png", 194, 138,10)
        self.fighter_2 = Fighter(700,310,80,180, RESOLUTION_X - 120,"2.png", 194, 138, 100)
        self.background_img = loadImage(PATH + "/Sprites/" + "background_imgg.png")
        self.fighter_2.dir = LEFT 
    def display(self):
        image(self.background_img, 0, 0) 
        fill(255,0,0)
        rect(RESOLUTION_X - 120,30, 100,10)
        fill(255,0,0)
        rect(20,30,100,10)
        self.fighter_2.display()
        self.fighter_1.display()
def keyPressed():
    if keyCode == LEFT:
        game.fighter_1.key_handler[LEFT] = True
    elif keyCode == RIGHT:
        game.fighter_1.key_handler[RIGHT] = True
    elif keyCode == UP:
        game.fighter_1.key_handler[UP] = True
    if key == ",":
        game.fighter_1.key_handler[punch] = True
        game.fighter_1.punching = True
        game.fighter_1.walking = False
        
    if key == '.':
        game.fighter_1.key_handler[kick] = True
        game.fighter_1.kicking = True
        game.fighter_1.walking = False
    if key == '/':
        game.fighter_1.key_handler[block] = True
        game.fighter_1.blocking = True
        game.fighter_1.walking = False
    if key == 'a':
        game.fighter_2.key_handler[LEFT] = True
    elif key == 'd':
        game.fighter_2.key_handler[RIGHT] = True
    elif key == ' ':
        game.fighter_2.key_handler[UP] = True
    if key == 'w':
        game.fighter_2.key_handler[punch] = True
        game.fighter_2.punching = True
        game.fighter_2.walking = False
    if key == 's':
        game.fighter_2.key_handler[block] = True
        game.fighter_2.blocking = True
        game.fighter_2.walking = False
    if key == 'e':
        game.fighter_2.key_handler[kick] = True
        game.fighter_2.kicking = True
        game.fighter_2.walking = False 
def keyReleased():
    if keyCode == LEFT:
        game.fighter_1.key_handler[LEFT] = False
    if keyCode == RIGHT:
        game.fighter_1.key_handler[RIGHT] = False  
    if keyCode == UP:
        game.fighter_1.key_handler[UP] = False 
    if key == ",":
        game.fighter_1.key_handler[punch] = False
        game.fighter_1.punching = False
        game.fighter_1.walking = True
    if key == '.':
        game.fighter_1.key_handler[kick] = False
        game.fighter_1.kicking = False
        game.fighter_1.walking = True
    if key == '/':
        game.fighter_1.key_handler[block] = False 
        game.fighter_1.blocking = False
        game.fighter_1.walking = True
    if key == 'a':
        game.fighter_2.key_handler[LEFT] = False
    if key == 'd':
        game.fighter_2.key_handler[RIGHT] = False  
    if key == ' ':
        game.fighter_2.key_handler[UP] = False 
    if key == 'w':
        game.fighter_2.key_handler[punch] = False
        game.fighter_2.punching = False
        game.fighter_2.walking = True
    if key == 's':
        game.fighter_2.key_handler[block] = False
        game.fighter_2.blocking = False 
        game.fighter_2.walking = True
    if key == 'e':
        game.fighter_2.key_handler[kick] = False
        game.fighter_2.kicking = False
        game.fighter_2.walking = True 
game = Game()
        
        
def setup():
    size(RESOLUTION_X,RESOLUTION_Y)
def draw():
    background(255,255,255)
    game.display()
    textSize(15)
    fill(0)
    text("Player1",20,18)
    text("Player2", RESOLUTION_X - 90,18)
