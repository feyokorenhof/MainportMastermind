import time
import StateManager
import Variables
class Dobbel():
    def __init__(self, ogen, images, position, parent):
        self.ogen = ogen + 1
        self.rolledDice = 0
        self.rolling = False
        self.images = images
        self.animationFrame = 0
        self.mis = Variables.MouseInSpace
        self.position = position
        self.parent = parent
        self.b_w = 200
        self.b_h = 100
        self.d_w = 200
        self.d_h = 200
        self.b_x = self.position['x'] + self.d_w/2 - self.b_w/2
        self.b_y = self.position['y'] + 500
        
    def rollDice(self):
        #Roll calculations:
        self.rolledDice = int(random(0, self.ogen-1))     
        self.rolling = True
        
    def drawDice(self):
        img = self.images[self.rolledDice]
        fill(255)
        rect(self.position['x']-1, self.position['y']-1, self.d_w+1, self.d_h+1)
        image(img, self.position['x'], self.position['y'], self.d_w, self.d_h)
        self.animationFrame = 0
        self.render()
        
    def animateDice(self, ):
        if self.rolling == False:
            return                
        img = self.images[self.animationFrame]
        fill(255)
        rect(self.position['x']-1, self.position['y']-1, self.d_w+1, self.d_h+1)
        image(img, self.position['x'], self.position['y'], self.d_w, self.d_h)
        
        if self.animationFrame == self.rolledDice or self.rolling == False:
            self.animationFrame = 0
            self.rolling = False 
            self.parent.processRoll()    
            return 
        if frameCount % 15 == 0:  
            self.animationFrame += 1   
        
    def render(self):
        # Gooi button          
        pass
        
    def update(self):
        if self.rolling:
            self.animateDice()
        else:
            self.drawDice()            
    
def upperText():
    fill(255, 255, 255) #text color (black)
    textSize(45)
    textAlign(CENTER)
    text('Gooi de linker of rechter dobbelsteen', width/2, 175)
    textSize(25)
    text('Dobbel en bepaal wat je deze beurt mag doen', width/2, 275)          
