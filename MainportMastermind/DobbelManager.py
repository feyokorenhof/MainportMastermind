from Dobbel import *
import StateManager
import Variables
class DobbelManager():
    def __init__(self, images, goback_btn, rollSound, storm_sound, cheer_sound):
        self.dobbelstenen = []
        self.back_btn = goback_btn
        self.mis = Variables.MouseInSpace
        self.rollSound = rollSound
        self.rollSound.amp(1.0)  
        self.storm_sound = storm_sound
        self.cheer_sound = cheer_sound
        db1 = Dobbel(6, images, {'x' : width/4 + 50, 'y' : 300}, self)
        db2 = Dobbel(6, images, {'x' : width/2 + 50, 'y' : 300}, self)
        self.dobbelstenen.append({'dobbel': db1, 'ogen': 6, 'gerold': -1})
        self.dobbelstenen.append({'dobbel': db2, 'ogen': 6, 'gerold': -1})
    
    def update(self):
        for d in self.dobbelstenen:    
            d['dobbel'].update()
        self.render()
        
    def render(self):
        # Back button
        image(self.back_btn, 20, 20)
        # Outcome text
        textSize(18)
        text(Variables.outcome, width/2 - len(Variables.outcome) * 4.5, 200)
        # Gooi button
        fill(0, 0, 0)
        rect(width/2, height - 100, 200, 100)
        fill(61, 61, 62)
        rect(width/2, height - 100, 200, 100)
        fill(255, 255, 255)
        textSize(40)
        text('Gooi!', width/2, height - 100)
        
    def processRoll(self):
        sum = 0
        done = False
        for d in self.dobbelstenen:
            done = sum + d['dobbel'].animationFrame == 0
        if done:
            outcome1 = 0
            outcome2 = 0
            outcome_str = ''
            outcome1 = self.dobbelstenen[0]['dobbel'].rolledDice + 1
            outcome2 = self.dobbelstenen[1]['dobbel'].rolledDice + 1
            
            outcome_str = str(outcome1) + '-' + str(outcome2)
            if (outcome1 == 6 or outcome2 == 6) and not StateManager.muted:
                self.cheer_sound.play()
            elif (outcome1 == 1 or outcome2 == 1) and not StateManager.muted:
                self.storm_sound.play()
                
            Variables.outcome = Variables.outcomes[outcome_str]
        else:
            Variables.outcome = 'Rolling..'
                
        
    def input_check(self):
        if self.mis(20, 20, 75, 50):
            StateManager.state = StateManager.states.MAINMENU
        elif self.mis(width/2, height - 100, 200, 100) and not self.rollSound.isPlaying():
            sum = 0
            for d in self.dobbelstenen:
                sum += d['dobbel'].animationFrame
            if sum > 0:
                return
            if not StateManager.muted:
                self.rollSound.play()
            Variables.outcome = 'Rolling..'
            for d in self.dobbelstenen:
                d['dobbel'].rollDice()
       
        
