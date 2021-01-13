import os
import StateManager
import Variables
class MainMenu():
    def __init__(self, bg, logo, miro_btn, buttons):
        self.bg_menu = bg
        self.logo = logo
        self.miro_btn = miro_btn
        self.btns = buttons
        self.dobbeling = False
        self.inspecting = False
        self.mis = Variables.MouseInSpace
    
    # Renders the main menu
    def main_menu(self):   
        image(self.bg_menu, 0, 0)    
        _w = width/2
        _h = height/3 + 100
        image(self.logo, _w - (width/5)/2, _h - 250)
        
        # Miro button
        image(self.miro_btn, 25, height-100)
        
        # Render buttons
        i = 0
        for b in self.btns:
            image(b['btn'], _w - 175, _h + (100 * i))
            i += 1
    
    def input_check(self, mX, mY):        
        x = width/2 - 175
        y = height/3 + 100
        
        i = 0
        for b in self.btns:
            nY = y + (100 * i)
            if self.mis(x, nY, 350, 75):
                self.handle_input(b['type'])
                break
            i += 1
        
    def handle_input(self, type):
        state = StateManager
        if type == 'dobbelen':
            state.state = state.states.DOBBELEN       
        elif type == 'spelvordering':
            state.state = state.states.SPELVORDERING
        elif type == 'handleiding':
            path = os.path.abspath("./resources/handleiding.pdf")
            os.system("start " + path)
        else:
            StateManager.saveState()                 
