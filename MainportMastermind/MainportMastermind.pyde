from MainMenu import *
from MainGame import *
from Dobbel import *
def setup():
    fullScreen()  
    
    # Main Menu class
    global main_menu
    main_menu = MainMenu()
    global main_game
    main_game = MainGame()
    
    # Dobbel
    global dobbelstenen
    dobbelstenen = []
    db1 = Dobbel(6)
    db2 = Dobbel(6)
    dobbelstenen.append({'dobbel': db1, 'ogen': 6, 'gerold': -1})
    dobbelstenen.append({'dobbel': db2, 'ogen': 6, 'gerold': -1})
    
def draw():
    background(255)    
    if main_menu.game_started:     
        upperText()
        global dobbelstenen
        if len(dobbelstenen) <= 0:
            return
        
        hoogsteDobbel = dobbelstenen[0]['dobbel']
        for i,d in enumerate(dobbelstenen):    
            if d['dobbel'].ogen > hoogsteDobbel.ogen:
                hoogsteDobbel = d['dobbel']
            w = 0
            if i == 0:
                w = 1
            else:
                w = 3
            if hoogsteDobbel.rolling:
                d['dobbel'].animateDice(w)
                isRolling = True
            else:
                d['dobbel'].drawDice(w)
                isRolling = False
        rollButtons()
        if isRolling:
            time.sleep(0.5)
        
    else:
        main_menu.main_menu()
    
    if main_game.paused:
        main_menu.pause_menu()

        
def mousePressed():
  if mouseButton == LEFT:
      global main_menu
      if main_menu.game_started:
        global dobbelstenen
        for d in dobbelstenen:
            d['dobbel'].rollDice()
      else:            
        global main_menu
        main_menu.input_check(mouseX, mouseY) 

      

def keyPressed():
    if key == 'p' or key == 'P':
        global main_game
        global main_menu
        if main_menu.game_started:
            main_game.paused = not main_game.paused
        
        

def MouseInSpace(x, y, w, h):
    return ((mouseX > x) and (mouseX < x+w) and (mouseY > y) and (mouseY < y+h))
