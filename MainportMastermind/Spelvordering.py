import StateManager
import Variables
class Spelvordering():
    def __init__(self, goback_btn, images):
        print('spelvordering yaaas')  
        self.players = StateManager.players
        self.colors = [{'naam': 'rood', 'kleur': color(255, 0, 0)}, { 'naam': 'groen', 'kleur': color(0, 255, 0)}, { 'naam': 'blauw', 'kleur': color(74, 112, 247)}, { 'naam': 'wit', 'kleur': color(255, 255, 255)}]
        self.back_btn = goback_btn
        self.images = images
        self.mis = Variables.MouseInSpace
        self.txtBoxFocus = False
        self.txt = ''
        self.adding = True
        self.selected = ''
        self.selectedProduct = ''
        
    def render(self):
        # Txtbox
        self.drawTxtBox()
        # Players
        if self.players != {}:
            self.drawPlayers()
        
        # Add producten
        self.drawProducten()
        
        # Back Button
        image(self.back_btn, 20, 20)
    
    def input_check(self):
        if self.mis(20, 20, 75, 50):
            StateManager.state = StateManager.states.MAINMENU
            self.txtBoxFocus = False
            self.selected = ''
        elif self.mis(20, 120, 400, 50):
            self.txtBoxFocus = True
            self.selected = ''
        elif self.playerSelected():
            self.txtBoxFocus = False
        elif self.productSelected():
            self.txtBoxFocus = False
        else:
            self.txtBoxFocus = False
    
    def playerSelected(self):
        x = 20
        y = 170
        for index, value in enumerate(self.players):
            pY = (y + 20) + (100 * index)
            if self.mis(x, pY-25, 400, 100):
                self.selected = value['naam']
                
    def productSelected(self):
        if self.selected == '':
            return
        x = width/2 - 400
        y = height - 200
        for index, value in enumerate(self.images.keys(), start=1):
            pX = x + (index * 67)
            pY = y + 25
            if self.mis(pX, pY, 50, 50):
                self.selectedProduct = value
                currentPlayer = list(filter(lambda player: player['naam'] == self.selected, self.players))[0]
                currentPlayer['inventaris'].append(self.selectedProduct)
                print(StateManager.players)
    
    def drawPlayers(self):
        x = 20
        y = 170            
        for index, value in enumerate(self.players):            
            textSize(20)
            textAlign(CORNER)
            pY = (y + 20) + (100 * index)
            if self.selected == value['naam']:
                fill(50, 50, 50)
                rect(x, pY - 25, 400, 100)
            fill(self.colors[index]['kleur'])
            text(value['naam'], x, pY)
            if len(value['inventaris']) <= 0:
                continue
            for index, value in enumerate(value['inventaris'], start=1):
                pX = x + (index * 50)
                image(self.images[value], pX, pY)
                
    def drawTxtBox(self):
        x = 20
        y = 120
        fill(12, 12, 12)
        rect(x, y, 400, 400)
        if self.txtBoxFocus:
            fill(50, 50, 50)
        else:
            fill(25, 25, 25)
        rect(x, y, 400, 50)
        fill(255, 255, 255)
        text(self.txt, x + 20, y + 40)
   
    def drawProducten(self):
        x = width/2 - 400
        y = height - 200
        fill(12, 12, 12)
        rect(x, y, 800, 100)    
        key_list = list(self.images.keys())
        val_list = list(self.images.values())
        for index, value in enumerate(self.images.values(), start=1):
            pX = x + (index * 67)
            pY = y + 25
            
            # print key with val 100
            position = val_list.index(value)
            if self.selectedProduct == key_list[position]:
                fill(50, 50, 50)
                rect(pX, pY, 50, 50)
            image(value, pX, pY)   
        
    def handleKeys(self, key):
        if len(self.players) == len(self.colors):
            self.txt = 'Maximaal aantal spelers bereikt'
            return
        if self.txtBoxFocus:
            if key == ENTER and self.txt != '':
                existing = list(filter(lambda player: player['naam'] == self.txt, self.players))
                if len(existing) > 0:
                    self.txt = 'Deze naam is al in gebruik!'
                    return
                self.players.append({'naam': self.txt, 'inventaris': []})
                self.txt = ''
            elif key == BACKSPACE:
                if len(self.txt) > 0:
                    if self.txt == 'Deze naam is al in gebruik!':
                        self.txt = ''
                    else:
                        self.txt = self.txt[0:len(self.txt)-1]
            else:
                self.txt += key       
        
