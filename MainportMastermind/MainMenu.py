class MainMenu():
    def __init__(self, bg, logo, sbtn, ebtn):
        self.bg_menu = bg
        self.logo = logo
        self.start_btn = sbtn
        self.exit_btn = ebtn
        self.game_started = False
    
    # Renders the main menu
    def main_menu(self):   
        image(self.bg_menu, 0, 0)    
        _w = width/2
        _h = height/2
        image(self.logo, _w - (width/5)/2, (height/4) - (height/3)/2)
        
        # Render start button
        image(self.start_btn, _w - 225, height/2)
        
        # Render exit button
        image(self.exit_btn, _w - 225, height/2 + 150)
    
    def input_check(self, mX, mY):        
        # Check start btn
        x = width/2 - 225
        y = height/2
        
        
        
        if mX >= x and mX <= x + 450:
            if mY >= y and mY <= y + 50:
                self.game_started = True
                
        # Check exit btn
        x = width/2 - 250
        y = height/2 + 150
        
        if mX >= x and mX <= x + 450:
            if mY >= y and mY <= y + 50:
                exit()
                        
