add_library('sound')
from MainMenu import *
from Dobbel import *
from Spelvordering import *
loaded = False
main_menu = False
spelvordering = False
def setup():
    fullScreen()
    thread("load")      
    
def load():
    global loaded
    global themesong 
    themesong = SoundFile(this, "../sound/seaofthieves.mp3")
    
    
    global rollSound
    rollSound = SoundFile(this, "../sound/diceroll.mp3")
    rollSound.amp(1.0)  
    
    # Load images
    bg_menu = loadImage('images/bg_menu.jpg')
    bg_menu.resize(width, height)
    start_btn = loadImage('images/dobbelstenen.png')
    start_btn.resize(450, 100)
    spel_btn = loadImage('images/spelvordering.png')
    spel_btn.resize(450, 100)
    handl_btn = loadImage('images/handleiding.png')
    handl_btn.resize(450, 100)
    exit_btn = loadImage('images/exitbutton.png')
    exit_btn.resize(450, 100)
    logo = loadImage('images/logo.png')
    logo.resize(width/5, height/3)
    
    global playing
    playing = False
    
    mm_btns = [
               {'btn': start_btn, 'type': 'start'},
               {'btn': spel_btn, 'type': 'spelvordering'},
               {'btn': handl_btn, 'type': 'handleiding'},
               {'btn': exit_btn, 'type': 'exit'},
               ]
    # Main Menu class
    global main_menu
    main_menu = MainMenu(bg_menu, logo, mm_btns)
    
    
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
    loaded = True
    
    # Spelvordering
    global spelvordering
    spelvordering = Spelvordering()
    
    
def draw():
    background(47, 46, 48)  
    if not loaded:
        return
    if main_menu.dobbeling:   
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
    elif main_menu.inspecting:
        spelvordering.render()
    else:
        main_menu.main_menu()

    global themesong
    if not themesong.isPlaying():
        themesong.amp(0.1)
        themesong.play()  

        
def mousePressed():
    if mouseButton == LEFT:
        if main_menu == False:
            return
        if main_menu.dobbeling:
            global dobbelstenen
            global rollSound
            for d in dobbelstenen:
                if not d['dobbel'].rolling:
                    d['dobbel'].rollDice()
            if not rollSound.isPlaying():
                rollSound.play()
        # elif main_menu.inspecting:
        #     main_menu.dobbeling = True
        #     main_menu.inspecting = False
        else:            
            main_menu.input_check(mouseX, mouseY) 
            playing = False
