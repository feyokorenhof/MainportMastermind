class Mainport():
    def __init__(self):
        self.ui_menu = [
            {'name': 'start', 'button_type': 'click', 'location': {'x': -1, 'y': -1}, 'dim': { 'w': -1, 'h': -1}}
        ]
    
    # Renders the main menu
    def main_menu(self):   
        global logo 
        global bg_menu
        image(bg_menu, 0, 0)    
        _margin = 0.02 * height
        _w = width/2
        _h = height/2 - ((len(self.ui_menu) - 1) * (20 + _margin))
        image(logo, _w - (width/5)/2, (height/4) - (height/3)/2)
        for index, s in enumerate(self.ui_menu):
            img = 0
            if s['name'] == 'start':
                global start_btn
                img = start_btn
                
            x = _w
            y = _h +(index * (50 + _margin))
            txt = s['name']
            text('blablabla', x, y)
            if img != 0:
                #image(img, x - (width/2)/2, y - (height/2)/2)
                rect(x, y, img.width, img.height)
                s['dim'] = {'w': img.width, 'h': img.height}
            fill(255, 255, 255)
            s['location'] = {'x': x, 'y': y}
            
            
    def pause_menu(self):
        _w = width/2
        _h = height/2
        x = _w - 125
        y = _h
        txt = 'Resume'
        rect(x, y - 10, 250, 50)
        fill(0,0,0)
        textSize(32)
        text(txt, x + 20, y + 25)
        fill(255, 255, 255)
        
    
    # Renders background and potentially other static gfx
    
    def draw_static(self):
        global bg
        image(bg, 0, 0)
    # 
    def handle_ui_pressed(self, s):
        if s['name'] == 'start':
            global game_started
            game_started = True
    
    def input_check(self, mX, mY):
        # Check if users hovers one of the buttons.
        for s in self.ui_menu:
            x = s['location']['x']
            y = s['location']['y']
            w = s['dim']['w']
            h = s['dim']['h']
            if mX >= x and mX <= x + w:
                if mY >= y and mY <= y + h:
                    self.handle_ui_pressed(s)
                        
            
        pass
 
        

def setup():
    fullScreen()
    global bg
    global bg_menu
    global logo
    global start_btn
    global game_started
    global paused
    global main_game
    bg = loadImage('images/bg.png')
    bg_menu = loadImage('images/bg_menu.jpg')
    logo = loadImage('images/logo.png')
    start_btn = loadImage('images/startbutton.png')
    game_started = False
    paused = False
    
    # Resizing images
    
    bg.resize(width, height)
    bg_menu.resize(width, height)
    logo.resize(width/5, height/3)
    start_btn.resize(width/2, height/2)
    
    # Main game class
    main_game = Mainport()
    
def draw():
    background(255)
    
    
    imageMode(CORNER)
    
    if game_started:        
        main_game.draw_static()
    else:
        main_game.main_menu()
    
    if paused:
        main_game.pause_menu()

        
def mousePressed():
  if mouseButton == LEFT:
    global main_game
    main_game.input_check(mouseX, mouseY)

def keyPressed():
    if key == 'p' or key == 'P':
        if game_started == True:
            global paused
            paused = not paused
        
        

        
