add_library('sound')
from MainMenu import *
from DobbelManager import *
from Spelvordering import *
import StateManager
import Variables
import csv
import gc
loaded = False
main_menu = False
spelvordering = False
bg_menu = 0
dobbelManager = 0
load_str_i = 1

img_sound = 0
img_no_sound = 0

def setup():
    size(1200, 800)
    global bg_menu
    bg_menu = loadImage('images/bg_menu.jpg')
    bg_menu.resize(width, height)
    thread("load")    
    global img_sound
    img_sound = loadImage('images/sound.png') 
    img_sound.resize(75, 75)
    global img_no_sound
    img_no_sound = loadImage('images/nosound.png') 
    img_no_sound.resize(75, 75)
    
    saveFileHandle = open('saves/save.csv')
    saveData = list(csv.DictReader(saveFileHandle))
    if len(saveData) > 0:
        for s in saveData:
            s['inventaris'] = s['inventaris'].strip('][').split(', ')
            for index, value in enumerate(s['inventaris']):
                s['inventaris'][index] = s['inventaris'][index].strip("'")
            StateManager.players.append(s)
    
def draw():
    background(47, 46, 48)  
    if not loaded:
        image(bg_menu, 0, 0)
        textSize(32)
        global load_str_i
        text("Loading" + '.' * load_str_i, width/2 - 64, height/2)
        load_str_i = load_str_i + 1 if frameCount % 60 == 0 else load_str_i
        if load_str_i >= 4:
            load_str_i = 1
        return
    
    state = StateManager.state
    if state == 'dobbelen':   
        global dobbelManager
        dobbelManager.update()
    elif state == 'spelvordering':
        spelvordering.render()
    else:
        main_menu.main_menu()
    
    global themesong
    muted = StateManager.muted
    if muted and themesong.isPlaying():
        themesong.pause()
        
    if not themesong.isPlaying() and not muted:
        themesong.amp(0.1)
        themesong.play()  
        
    global img_sound
    global img_no_sound    
    img = img_sound if not muted else img_no_sound
    image(img, width - 100, height - 100)

def load():
    global loaded
    
    # Sound
    global themesong 
    themesong = SoundFile(this, "../sound/seaofthieves.mp3")
    rollSound = SoundFile(this, "../sound/diceroll.mp3")
    
    # Load images    
    start_btn = loadImage('images/dobbelstenen.png')
    start_btn.resize(350, 75)
    spel_btn = loadImage('images/spelvordering.png')
    spel_btn.resize(350, 75)
    handl_btn = loadImage('images/handleiding.png')
    handl_btn.resize(350, 75)
    exit_btn = loadImage('images/exitbutton.png')
    exit_btn.resize(350, 75)
    goback_btn = loadImage('images/goback.png')
    goback_btn.resize(75, 50)
    cross_btn = loadImage('images/cross.png')
    cross_btn.resize(25, 25)
    miro_btn = loadImage('images/miro.png')
    miro_btn.resize(100, 75)
    logo = loadImage('images/logo.png')
    logo.resize(width/5, height/4)
    
    global playing
    playing = False
    
    mm_btns = [
      {'btn': start_btn, 'type': 'dobbelen'},
      {'btn': spel_btn, 'type': 'spelvordering'},
      {'btn': handl_btn, 'type': 'handleiding'},
      {'btn': exit_btn, 'type': 'exit'},
    ]
    # Main Menu class
    global main_menu
    global bg_menu
    main_menu = MainMenu(bg_menu, logo, miro_btn, mm_btns)   
    
    # Dobbels
    images = []
    for i in range(6):
        _imgstr = 'images/dobbel/dice' + str(i+1) + '.png'
        images.append(loadImage(_imgstr)) 
     
    storm_sound = SoundFile(this, "../sound/storm.mp3")
    cheer_sound = SoundFile(this, "../sound/cheer.mp3")
    global dobbelManager
    dobbelManager = DobbelManager(images, goback_btn, rollSound, storm_sound, cheer_sound)
    
    # Spelvordering
    
    producten = ['koffie', 'dadels', 'smaragd', 'goud', 'kaas', 'maple', 'olie', 'sinasappel', 'palmolie', 'suiker']
    images = {}
    for p in producten:
        images[p] = loadImage('images/producten/' + p + '.png')
        images[p].resize(50, 50)
    
    godobbelen_btn = loadImage('images/gotodobbelen.png')
    godobbelen_btn.resize(100, 100)
    global spelvordering
    spelvordering = Spelvordering(goback_btn, godobbelen_btn, cross_btn, images)
    loaded = True

def mousePressed():
    if mouseButton == LEFT:    
        if not main_menu:
            return    
        global dobbelManager
        global spelvordering
        state = StateManager
        if Variables.MouseInSpace(width - 100, height - 100, 75, 75):
            state.muted = not state.muted
        if Variables.MouseInSpace(25, height-100, 100, 75):
            link('https://miro.com/app/board/o9J_kkYRyq4=/')
        if state.state == 'dobbelen':
            dobbelManager.input_check()
        elif state.state == 'spelvordering':
            spelvordering.input_check()
        else:    
            main_menu.input_check(mouseX, mouseY) 
            playing = False
def keyPressed():
    if key == CODED or StateManager.state != 'spelvordering':
        return
    global spelvordering
    spelvordering.handleKeys(key)
