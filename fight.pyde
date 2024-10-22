add_library('minim')
import os
#no
import random
player = Minim(this)
PATH = os.getcwd()
RESOLUTION_X = 1000
RESOLUTION_Y = 600 
kick = "kick"
punch = "punch" #delcaring our punch key for the key_handler dictionary 
block = "block"
Games = []

class Fighter:
    def __init__(self, x,y,w,h,health,img, slice_w, slice_h, shift):
        self.kick_sound = player.loadFile(PATH + "/Sound/kick.mp3")
        self.punch_sound = player.loadFile(PATH + "/Sound/punch.mp3")
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
        self.attacking = False 
    def display(self):
        self.move()
        fill(255,0,0)
        #rect(self.x, self.y, self.w, self.h)
        fill(0,255,0)
        rect(self.health, 30, self.health_bar, 10)
        if self.dir == RIGHT:
            if self.walking:
                self.num_slices = 6
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h, 125 * 8 + self.slice * self.slice_w, 0, 125 * 8 + (self.slice + 1)* self.slice_w, self.slice_h)
            elif self.punching:
                self.num_slices = 10
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h,  125*5 + self.slice * self.slice_w, 0, 125*5 + (self.slice + 1) * self.slice_w, self.slice_h )
            elif self.kicking == True:
                self.num_slices = 4
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h,125*16 + self.slice * self.slice_w, 0, 125 * 16 +(self.slice + 1)* self.slice_w, self.slice_h)
            elif self.blocking == True:
                self.num_slices = 6
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h, 125 * 20 + self.slice * self.slice_w, 0, 125 * 20 + (self.slice + 1)* self.slice_w, self.slice_h)
        elif self.dir == LEFT:
            if self.walking:
                self.num_slices = 7
                image(self.img, self.x - self.shift  , self.y + 50, self.slice_w, self.slice_h, 125 * 8 + (self.slice + 1) * self.slice_w, 0,125 * 8 + self.slice * self.slice_w, self.slice_h)
            if self.punching:
                self.num_slices = 10
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h, 125*5 + (self.slice + 1) * self.slice_w, 0,  125*5 + self.slice * self.slice_w, self.slice_h )    
            elif self.kicking:
                self.num_slices = 4
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h, 125 *16 + (self.slice + 1) * self.slice_w, 0, 125 *16 + self.slice * self.slice_w, self.slice_h)
            elif self.blocking:
                self.num_slices = 6
                image(self.img, self.x - self.shift, self.y + 50, self.slice_w, self.slice_h, 125 * 20 + (self.slice + 1) * self.slice_w, 0, 125 * 20 + self.slice * self.slice_w, self.slice_h)
   #checks if the fighters are colliding,if the fighter is blocking the attack from the right direction or is jumping while recieving the attack, then he is protected
     
    def kick(self):
        if Games[-1].fighter_1.x + self.w >= Games[-1].fighter_2.x:
            if Games[-1].fighter_1.health_bar > 0 and Games[-1].fighter_2.kicking and Games[-1].fighter_1.vy == 0 and (not Games[-1].fighter_1.blocking or Games[-1].fighter_1.dir == LEFT) and Games[-1].fighter_2.dir == LEFT:
                Games[-1].fighter_1.health_bar -= 5
            if Games[-1].fighter_2.health < RESOLUTION_X - 20 and Games[-1].fighter_1.kicking and Games[-1].fighter_2.vy == 0 and (not Games[-1].fighter_2.blocking or Games[-1].fighter_2.dir == RIGHT) and Games[-1].fighter_1.dir == RIGHT:
                Games[-1].fighter_2.health += 5
                Games[-1].fighter_2.health_bar -= 5
    def punch(self):
        if Games[-1].fighter_1.x + self.w >= Games[-1].fighter_2.x:
            if Games[-1].fighter_1.health_bar > 0 and Games[-1].fighter_2.punching and Games[-1].fighter_1.vy == 0 and (not Games[-1].fighter_1.blocking or Games[-1].fighter_1.dir == LEFT) and Games[-1].fighter_2.dir == LEFT:
                Games[-1].fighter_1.health_bar -= 2
            if Games[-1].fighter_2.health < RESOLUTION_X - 20 and Games[-1].fighter_1.punching and Games[-1].fighter_2.vy == 0 and (not Games[-1].fighter_2.blocking or Games[-1].fighter_2.dir == RIGHT) and Games[-1].fighter_1.dir == RIGHT:
                Games[-1].fighter_2.health += 2
                Games[-1].fighter_2.health_bar -= 2
    # def block(self):
    #     if Games[-1].fighter_1.x + self.w >= Games[-1].fighter_2.x:
    #         if Games[-1].fighter_1.health_bar > 0 and Games[-1].fighter_2.kicking or 0 < Games[-1].fighter_1.health_bar < 100  and Games[-1].fighter_2.punching:
    #             Games[-1].fighter_1.health_bar += 5
    #         if Games[-1].fighter_2.health < RESOLUTION_X - 20 and Games[-1].fighter_1.kicking or Games[-1].fighter_2.health_bar < RESOLUTION_X - 20  and Games[-1].fighter_1.punching:
    #             Games[-1].fighter_2.health -= 5
    #             Games[-1].fighter_2.health_bar += 5
                
        
    def move(self):
        #gravity 
        
        if self.y + self.h >= self.g:  
            self.vy = 0 
        else:
            self.vy += 5
            
        if self.key_handler[LEFT] == True:
            self.vx = -7
            if Games[-1].fighter_2.x <= self.w + Games[-1].fighter_1.x:
                Games[-1].fighter_2.vx = 0
            self.dir = LEFT
        elif self.key_handler[RIGHT] == True:
            self.vx = 7
            if Games[-1].fighter_1.x + self.w >= Games[-1].fighter_2.x:
                Games[-1].fighter_1.vx = 0
            self.dir = RIGHT
            
        else:
            self.vx = 0
        if self.key_handler[UP] == True and self.y + self. h == self.g:
            self.vy = -45
    
    
        #checks edges of the screen 
        if self.x + self.vx < 0:
            self.vx = -self.x
        if self.x + self.w + self.vx > RESOLUTION_X:
            self.vx = RESOLUTION_X - self.w - self.x 
        if frameCount % 10 == 0 and self.vx != 0: 
            self.slice = (self.slice + 1) % self.num_slices
        elif self.vx == 0:
            self.slice = 0
            
            
        self.x += self.vx
        self.y += self.vy 
        
        #attacks 
        if frameCount % 60 == 0:
            if Games[-1].fighter_2.punching or Games[-1].fighter_2.kicking:
                Games[-1].fighter_1.punching = False
                Games[-1].fighter_1.kicking = False 
                Games[-1].fighter_1.walking = True 
                #Games[-1].fighter_1.blocking = True 
                if Games[-1].fighter_2.key_handler[kick] == True:
                    Games[-1].fighter_2.kick()
                    if Games[-1].Collide:
                        Games[-1].fighter_2.kick_sound.rewind()
                        Games[-1].fighter_2.kick_sound.play()
                elif Games[-1].fighter_2.key_handler[punch] == True:
                    Games[-1].fighter_2.punch()
                    if Games[-1].Collide:
                        Games[-1].fighter_2.punch_sound.rewind()
                        Games[-1].fighter_2.punch_sound.play()
            if Games[-1].fighter_1.punching or Games[-1].fighter_1.kicking:
                Games[-1].fighter_2.punching = False
                Games[-1].fighter_2.kicking = False
                Games[-1].fighter_2.walking = True 
                #Games[-1].fighter_2.blocking = True 
                
                if Games[-1].fighter_1.key_handler[kick] == True:
                    Games[-1].fighter_1.kick()
                    if Games[-1].Collide:
                        Games[-1].fighter_1.kick_sound.rewind()
                        Games[-1].fighter_1.kick_sound.play()
                elif Games[-1].fighter_1.key_handler[punch] == True:
                    Games[-1].fighter_1.punch()
                    if Games[-1].Collide:
                        Games[-1].fighter_1.punch_sound.rewind()
                        Games[-1].fighter_1.punch_sound.play()
        # if self.key_handler[block] == True:
        #         self.block()
        # elif Games[-1].fighter_1.punching or Games[-1].fighter_1.kicking or Games[-1].fighter_2.punching or Games[-1].fighter_2.kicking:
        #     self.walking = True 
    
class Game:
    def __init__(self):
        self.fighter_1 = Fighter(200,310,50,180, 20, "C1.png", 125, 125,12)
        self.fighter_2 = Fighter(700,310,50,180, RESOLUTION_X - 120,"CB.png", 125, 125, 12)
        self.background_img = loadImage(PATH + "/Sprites/" + "background_imgg.png")
        self.fighter_2.dir = LEFT 
        self.bg_sound = player.loadFile(PATH + "/Sound/back.mp3")
        self.bg_sound.loop()
        self.fighter_2_wins = False
        self.fighter_1_wins = False
        self.draw_ = False
        self.Collide = False
    def game_over(self):
        if Games[-1].fighter_1.health_bar == 0 and Games[-1].fighter_2.health_bar != 0:
            self.fighter_2_wins = True
        if Games[-1].fighter_1.health_bar != 0 and Games[-1].fighter_2.health_bar == 0:
            self.fighter_1_wins = True
        if Games[-1].fighter_1.health_bar == 0 and Games[-1].fighter_2.health_bar == 0:
            self.draw_ = True 
    def display(self):
        if  Games[-1].fighter_1.x + Games[-1].fighter_2.w >= Games[-1].fighter_2.x:
            self.Collide = True 
        else:
            self.Collide = False
        self.game_over()
        image(self.background_img, 0, 0) 
        fill(255,0,0)
        rect(RESOLUTION_X - 120,30, 100,10)
        fill(255,0,0)
        rect(20,30,100,10)
        if Games[-1].fighter_2_wins:
            self.fighter_2.display()
            fill(0,0,255)
            rect(300,100, 500,100)
            textSize(15)
            fill(0)
            textSize(30)
            text("Ouch! Fighter 2 wins",430,150)
            text("Click to Restart", 430, 185)
        elif Games[-1].fighter_1_wins:
            self.fighter_1.display()
            fill(255,0,0)
            rect(300,100, 500,100)
            textSize(15)
            fill(0)
            textSize(30)
            text("Oops! Fighter 1 wins",430,150)
            text("Click to Restart", 430, 185)
        elif Games[-1].draw_:
            fill(0,0,0)
            rect(300,100, 500,100)
            fill(0,255,0)
            text("That was a close one!",430,150)
            text("Let's do it again", 430, 170)
            
        else:
            self.fighter_2.display()
            self.fighter_1.display()
    
def keyPressed():
    if keyCode == LEFT:
        Games[-1].fighter_1.key_handler[LEFT] = True
    elif keyCode == RIGHT:
        Games[-1].fighter_1.key_handler[RIGHT] = True
    elif keyCode == UP:
        Games[-1].fighter_1.key_handler[UP] = True
    if key == ",":
        Games[-1].fighter_1.key_handler[punch] = True
        Games[-1].fighter_1.punching = True
        Games[-1].fighter_1.walking = False
        
    if key == '.':
        Games[-1].fighter_1.key_handler[kick] = True
        Games[-1].fighter_1.kicking = True
        Games[-1].fighter_1.walking = False
    if key == '/':
        Games[-1].fighter_1.key_handler[block] = True
        Games[-1].fighter_1.blocking = True
        Games[-1].fighter_1.walking = False
    if key == 'a':
        Games[-1].fighter_2.key_handler[LEFT] = True
    elif key == 'd':
        Games[-1].fighter_2.key_handler[RIGHT] = True
    elif key == ' ':
        Games[-1].fighter_2.key_handler[UP] = True
    if key == 'w':
        Games[-1].fighter_2.key_handler[punch] = True
        Games[-1].fighter_2.punching = True
        Games[-1].fighter_2.walking = False
    if key == 's':
        Games[-1].fighter_2.key_handler[block] = True
        Games[-1].fighter_2.blocking = True
        Games[-1].fighter_2.walking = False
    if key == 'e':
        Games[-1].fighter_2.key_handler[kick] = True
        Games[-1].fighter_2.kicking = True
        Games[-1].fighter_2.walking = False 
def keyReleased():
    if keyCode == LEFT:
        Games[-1].fighter_1.key_handler[LEFT] = False
    if keyCode == RIGHT:
        Games[-1].fighter_1.key_handler[RIGHT] = False  
    if keyCode == UP:
        Games[-1].fighter_1.key_handler[UP] = False 
    if key == ",":
        Games[-1].fighter_1.key_handler[punch] = False
        Games[-1].fighter_1.punching = False
        Games[-1].fighter_1.walking = True
    if key == '.':
        Games[-1].fighter_1.key_handler[kick] = False
        Games[-1].fighter_1.kicking = False
        Games[-1].fighter_1.walking = True
    if key == '/':
        Games[-1].fighter_1.key_handler[block] = False 
        Games[-1].fighter_1.blocking = False
        Games[-1].fighter_1.walking = True
    if key == 'a':
        Games[-1].fighter_2.key_handler[LEFT] = False
    if key == 'd':
        Games[-1].fighter_2.key_handler[RIGHT] = False  
    if key == ' ':
        Games[-1].fighter_2.key_handler[UP] = False 
    if key == 'w':
        Games[-1].fighter_2.key_handler[punch] = False
        Games[-1].fighter_2.punching = False
        Games[-1].fighter_2.walking = True
    if key == 's':
        Games[-1].fighter_2.key_handler[block] = False
        Games[-1].fighter_2.blocking = False 
        Games[-1].fighter_2.walking = True
    if key == 'e':
        Games[-1].fighter_2.key_handler[kick] = False
        Games[-1].fighter_2.kicking = False
        Games[-1].fighter_2.walking = True 
Games.append(Game())
def mouseClicked():
    if Games[-1].fighter_1_wins or Games[-1].fighter_2_wins or Games[-1].draw_:
        Games.append(Game())
        
        
def setup():
    size(RESOLUTION_X,RESOLUTION_Y)
def draw():
    background(255,255,255)
    Games[-1].display()
    textSize(15)
    fill(255,0,0)
    text("Player1",20,18)
    fill(0,0,255)
    text("Player2", RESOLUTION_X - 90,18)
    
#change 
