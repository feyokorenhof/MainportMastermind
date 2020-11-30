from MainMenu import *
from Dobbel import *
def setup():
    fullScreen()    
    
    # Load images
    bg_menu = loadImage('images/bg_menu.jpg')
    bg_menu.resize(width, height)
    start_btn = loadImage('images/startbutton.png')
    start_btn.resize(450, 100)
    exit_btn = loadImage('images/exitbutton.png')
    exit_btn.resize(450, 100)
    logo = loadImage('images/logo.png')
    logo.resize(width/5, height/3)
    
    # Main Menu class
    global main_menu
    main_menu = MainMenu(bg_menu, logo, start_btn, exit_btn)
    
    
    # Dobbel
    global dobbelstenen
    dobbelstenen = []
    images = []
    for i in range(6):
        _imgstr = 'images/dobbel/dice' + str(i+1) + '.png'
        images.append(loadImage(_imgstr))
        
    
        
    db1 = Dobbel(6, images)
    db2 = Dobbel(6, images)
    dobbelstenen.append({'dobbel': db1, 'ogen': 6, 'gerold': -1})
    dobbelstenen.append({'dobbel': db2, 'ogen': 6, 'gerold': -1})
    
def draw():
    background(47, 46, 48)  
    if main_menu.game_started:     
        upperText()
        global dobbelstenen
        if len(dobbelstenen) <= 0:
            return
        isRolling = False
        hoogsteDobbel = dobbelstenen[0]['dobbel']
        for i,d in enumerate(dobbelstenen):    
            if d['dobbel'].ogen > hoogsteDobbel.ogen:
                hoogsteDobbel = d['dobbel']
            w = 0
            if i == 0:
                w = 1
            else:
                w = 3
            if d['dobbel'].rolling:
                d['dobbel'].animateDice(w)
                isRolling = True
            else:
                d['dobbel'].drawDice(w)
                isRolling = dobbelstenen[0]['dobbel'].rolling or dobbelstenen[1]['dobbel'].rolling
        rollButtons()
        if isRolling:
            time.sleep(0.5)
        
    else:
        main_menu.main_menu()

        
def mousePressed():
  if mouseButton == LEFT:
      global main_menu
      if main_menu.game_started:
        global dobbelstenen
        for d in dobbelstenen:
            d['dobbel'].rollDice()
      else:            
        main_menu.input_check(mouseX, mouseY) 
        
        

def MouseInSpace(x, y, w, h):
    return ((mouseX > x) and (mouseX < x+w) and (mouseY > y) and (mouseY < y+h))
