import StateManager
import Variables
class Spelvordering():
    def __init__(self, goback_btn, godobbelen_btn, cross_btn, images):
        self.players = StateManager.players
        self.colors = [
            {'naam': 'rood', 'kleur': color(255, 0, 0)}, 
            { 'naam': 'yellow', 'kleur': color(0, 255, 255)},
            { 'naam': 'groen', 'kleur': color(0, 255, 0)}, 
            { 'naam': 'blauw', 'kleur': color(74, 112, 247)}, 
            { 'naam': 'purple', 'kleur': color(255,0,255)}
        ]
        self.starthavens = [
            'Rotterdam',
            'Qatar',
            'Shanghai',
            'Singapore',
            'Kaapstad',
            'Dakar',
            'Rio de Janeiro',
            'Caracas',
            'Los Angeles',
            'Quebec'
        ]
        self.back_btn = goback_btn
        self.dobbel_btn = godobbelen_btn
        self.cross_btn = cross_btn
        self.images = images
        self.mis = Variables.MouseInSpace
        self.txtBoxFocus = False
        self.txt = ''
        self.adding = True
        self.selected = ''
        self.selectedProduct = ''
        self.selectedHaven = ''
        self.havens = Variables.havens
        for p in self.players:
            del self.havens[self.havens.index(p['haven'])]
        
        stroke(255, 255, 255)
        
    def render(self):
        # Txtbox
        self.drawTxtBox()
        
        # Picker
        if self.txtBoxFocus:
            self.drawPicker()
        
        # Players
        if self.players != {}:
            self.drawPlayers()
        
        # Add producten
        self.drawProducten()
        
        
        # Go to dobbelen btn
        image(self.dobbel_btn, width - 125, 20)
        # Back Button
        image(self.back_btn, 20, 20)
        
    def input_check(self):
        if self.mis(20, 20, 75, 50):
            StateManager.state = StateManager.states.MAINMENU
            self.txtBoxFocus = False
            self.selected = ''
        elif self.mis(width-125, 20, 100, 100):
            StateManager.state = StateManager.states.DOBBELEN
            self.txtBoxFocus = False
            self.selected = ''
        elif self.mis(width/2 - 400, height - 700, 800, 50):
            self.txtBoxFocus = True
            self.selected = ''
        elif self.mis(20, height-700, 180, 25 * len(self.havens)):
            self.txtBoxFocus = True
            self.havenSelected()
        elif self.playerSelected():
            self.txtBoxFocus = False
        elif self.productSelected():
            self.txtBoxFocus = False
        else:
            self.txtBoxFocus = False
            self.selectedProduct = ''
    
    def playerSelected(self):
        x = width/2 - 400
        y = height - 650 
        for index, value in enumerate(self.players):
            pY = (y + 20) + (100 * index)
            if self.mis(x, pY-25, 800, 100):
                self.selected = value['naam']
                self.inventoryItemSelected()
                self.deletePlayer(x, pY)
                
    def productSelected(self):
        if self.selected == '':
            return
        x = width/2 - 400
        y = height - 150
        for index, value in enumerate(self.images.keys(), start=1):
            pX = x + (index * 67)
            pY = y + 25
            if self.mis(pX, pY, 50, 50):
                self.selectedProduct = value
                currentPlayer = list(filter(lambda player: player['naam'] == self.selected, self.players))[0]
                if len(currentPlayer['inventaris']) >= 14:
                    return
                currentPlayer['inventaris'].append(self.selectedProduct)
                
                
    def inventoryItemSelected(self):
        if self.selected == '':
            return
        currentPlayer = list(filter(lambda player: player['naam'] == self.selected, self.players))[0]
        x = width/2 - 400 
        y = height - 650 + 20 + self.players.index(currentPlayer) * 100
        inventory = currentPlayer['inventaris']
        for index, value in enumerate(inventory, start=1):
            iX = x + (index * 50)
            if self.mis(iX, y, 35, 35):
                del currentPlayer['inventaris'][index-1]
                
    def havenSelected(self):
        if not self.txtBoxFocus:
            return
        y = height - 680
        for index, value in enumerate(self.havens):
            _x = 25
            _y = y + index * 25
            if self.mis(_x, _y-25, 180, 25):
                self.selectedHaven = value
                
    def deletePlayer(self, x, pY):
        _x, _y = x+768, pY-12
        if self.mis(_x, _y, 25, 25):
            playerToRemove = list(filter(lambda player: player['naam'] == self.selected, self.players))[0]
            # Add haven back to available havens
            self.havens.append(playerToRemove['haven'])
            del self.players[self.players.index(playerToRemove)]
            self.selected = ''
    
    def drawPlayers(self):
        x = width/2 - 400
        y = height - 650         
        textSize(20)
        for index, value in enumerate(self.players):            
            textAlign(CORNER)
            pY = (y + 20) + (100 * index)
            if self.selected == value['naam']: fill(50, 50, 50)
            else:
                noFill()
                stroke(255)
            rect(x, pY - 20, 800, 100)
            fill(self.colors[index]['kleur'])
            text(value['naam'], x+5, pY)
            text(value['haven'], x+5, pY + 75)
            
            # Delete player button
            if self.selected == value['naam']: 
                image(self.cross_btn, x+768, pY-12)
            
            if len(value['inventaris']) <= 0: 
                continue
            for index, product in enumerate(value['inventaris'], start=1):
                pX = x + (index * 50)
                if product != '':
                    image(self.images[product], pX, pY, 35, 35)
                
    def drawTxtBox(self):
        x = width/2 - 400
        y = height - 700
        fill(12, 12, 12)
        rect(x, y, 800, 600)
        if self.txtBoxFocus:
            fill(50, 50, 50)
        else:
            fill(25, 25, 25)
        rect(x, y, 800, 50)
        fill(255, 255, 255)
        text(self.txt, x + 20, y + 40)
        
    def drawPicker(self):
        x = 20
        y = height - 700
        fill(12,12,12)
        rect(x, y, 180, 25 * len(self.havens))
        self.drawHavens()
   
    def drawProducten(self):
        x = width/2 - 400
        y = height - 150
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
        
    def drawHavens(self):
        if not self.txtBoxFocus: return
        y = height - 680
        for index, value in enumerate(self.havens):
            _x = 25
            _y = y + index * 25
            fill(255, 255, 255)
            if self.selectedHaven == value:
                noFill()
                stroke(100, 230, 100)
                rect(_x-5, _y - 20, 180, 25)
                stroke(255)
            text(value, _x, _y)
            
    
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
                elif self.selectedHaven == '':
                    self.txt = 'Selecteer eerst een haven!'
                    return
                else:
                    self.players.append({'naam': self.txt, 'inventaris': [], 'haven': self.selectedHaven})
                    self.txt = ''
                    
                    # Remove haven from list
                    del self.havens[self.havens.index(self.selectedHaven)]
                    self.selectedHaven = ''
                    if len(self.players) != len(self.colors): self.txtBoxFocus = True
                    else: self.txtBoxFocus = False
            elif key == BACKSPACE:
                if len(self.txt) > 0:
                    if self.txt == 'Deze naam is al in gebruik!' or self.txt == 'Selecteer eerst een haven!':
                        self.txt = ''
                    else:
                        self.txt = self.txt[0:len(self.txt)-1]
            else:
                self.txt += key       
        
