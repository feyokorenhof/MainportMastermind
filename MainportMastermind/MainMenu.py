import os
import StateManager
import Variables
class MainMenu():
    def __init__(self, bg, logo, buttons):
        self.bg_menu = bg
        self.logo = logo
        self.btns = buttons
        self.dobbeling = False
        self.inspecting = False
        self.mis = Variables.MouseInSpace
    
    # Renders the main menu
    def main_menu(self):   
        image(self.bg_menu, 0, 0)    
        _w = width/2
        _h = height/2
        image(self.logo, _w - (width/5)/2, (height/4) - (height/3)/2)
        
        # Render buttons
        i = 0
        for b in self.btns:
            image(b['btn'], _w - 225, height/2 + (125 * i))
            i += 1
    
    def input_check(self, mX, mY):        
        # Check start btn
        x = width/2 - 225
        y = height/2
        
        i = 0
        for b in self.btns:
            nY = y + (125 * i)
            if self.mis(x, nY, 450, 150):
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
