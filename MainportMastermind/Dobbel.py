import time
class Dobbel():
    def __init__(self, ogen):
        self.ogen = ogen + 1
        self.rolledDice = int(random(1, self.ogen))   
        self.rolling = False
        self.images = []
        self.animationFrame = 0
        for i in range(self.ogen-1):
            _imgstr = 'images/dobbel/dice' + str(i+1) + '.png'
            print(_imgstr)
            self.images.append(loadImage(_imgstr))
        
    def rollDice(self):
        #Roll calculations:
        self.rolledDice = int(random(1, self.ogen))        
        self.rolling = True
        
    def drawDice(self, w):
        imageMode(CENTER)
        img = self.images[self.rolledDice-1]
        image(img, (width/4)*w, 600, 490, 490)
        
    def animateDice(self, w):
        if self.animationFrame == self.ogen-1 or self.rolling == False:
            self.animationFrame = 0
            self.rolling = False
            return
                
        imageMode(CENTER)
        img = self.images[self.animationFrame]
        image(img, (width/4)*w, 600, 490, 490)
        self.animationFrame += 1
        
        
    
    
def upperText():
    fill(255, 255, 255) #text color (black)
    textSize(45)
    textAlign(CENTER)
    text('Gooi de linker of rechter dobbelsteen', width/2, 175)
    textSize(25)
    text('Dobbel en bepaal wat je deze beurt mag doen', width/2, 275)

def rollButtons(): #the lower two buttons
    fill(0, 0, 0)
    rectMode(CENTER)
    rect(width/4, 950, 355, 155)
    fill(61, 61, 62)
    rect(width/4, 950, 350, 150)
    fill(255, 255, 255)
    textSize(40)
    textAlign(CENTER)
    text('Gooi!', width/4, 950)       
