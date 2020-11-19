class MainMenu():
    def __init__(self):
        self.ui_menu = [
            {'name': 'start', 'button_type': 'click', 'location': {'x': -1, 'y': -1}, 'dim': { 'w': -1, 'h': -1}}
        ]
        
        self.bg_menu = loadImage('images/bg_menu.jpg')
        self.bg_menu.resize(width, height)
        self.start_btn = loadImage('images/startbutton.png')
        self.start_btn.resize(width/2, height/2)
        self.logo = loadImage('images/logo.png')
        self.logo.resize(width/5, height/3)
        
        self.game_started = False
    
    # Renders the main menu
    def main_menu(self):   
        image(self.bg_menu, 0, 0)    
        _margin = 0.02 * height
        _w = width/2
        _h = height/2 - ((len(self.ui_menu) - 1) * (20 + _margin))
        image(self.logo, _w - (width/5)/2, (height/4) - (height/3)/2)
        for index, s in enumerate(self.ui_menu):
            img = 0
            if s['name'] == 'start':
                img = self.start_btn
                
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
    
    def handle_ui_pressed(self, s):
        if s['name'] == 'start':
            self.game_started = True
    
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
                        
