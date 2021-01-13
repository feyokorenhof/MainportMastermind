from Dobbel import *
import StateManager
import Variables
class DobbelManager():
    def __init__(self, images, goback_btn, govordering_btn, rollSound, storm_sound, cheer_sound):
        self.dobbelstenen = []
        self.back_btn = goback_btn
        self.vordering_btn = govordering_btn
        self.mis = Variables.MouseInSpace
        self.rollSound = rollSound
        self.rollSound.amp(1.0)  
        self.storm_sound = storm_sound
        self.cheer_sound = cheer_sound
        db1 = Dobbel(6, images, {'x' : width/4 + 50, 'y' : 300}, self)
        db2 = Dobbel(6, images, {'x' : width/2 + 50, 'y' : 300}, self)
        self.dobbelstenen.append({'dobbel': db1, 'ogen': 6, 'gerold': -1})
        self.dobbelstenen.append({'dobbel': db2, 'ogen': 6, 'gerold': -1})
        self.is_kans = False
        self.kans_dobbel = Dobbel(6, images, {'x' : width/2 - 100, 'y': 300}, self)
        self.previous = 0
        self.worp_txt = 'Gooi!'
    
    def update(self):
        if not self.is_kans:
            for d in self.dobbelstenen:    
                d['dobbel'].update()
        else:
            self.kans_dobbel.update()
        self.render()
        
    def render(self):
        # Back button
        image(self.back_btn, 20, 20)
        # Go to vordering btn
        image(self.vordering_btn, width - 125, 20)
        # Outcome text
        outcome = Variables.outcome
        if outcome in Variables.outcomes_kans:
            textSize(10)
        else:
            textSize(18)
        _x = width/2 - len(outcome) * 4.5 if not '\n' in outcome else width/2 - len(outcome) * 2.25
        text(outcome, _x, 200)
        # Gooi button
        fill(61, 61, 62)
        rect(width/2-100, height - 200, 200, 100)
        fill(255, 255, 255)
        textSize(40)
        text(self.worp_txt, width/2-50, height - 130)
        
    def processRoll(self):
        if not self.is_kans:
            sum = 0
            done = self.dobbelstenen[0]['dobbel'].rolling == False and self.dobbelstenen[1]['dobbel'].rolling == False
            if done:
                outcome1 = 0
                outcome2 = 0
                outcome_str = ''
                outcome1 = self.dobbelstenen[0]['dobbel'].rolledDice + 1
                outcome2 = self.dobbelstenen[1]['dobbel'].rolledDice + 1
                
                outcome_str = str(outcome1) + '-' + str(outcome2)
                if ( (outcome1 == 6 and outcome2 != 6) or (outcome1 != 6 and outcome2 == 6) ):
                    self.worp_txt = 'Verder'
                    for d in self.dobbelstenen:
                        d['dobbel'].animationFrame = 0
                    if not StateManager.muted:
                        self.cheer_sound.play()
                elif (outcome1 == 1 or outcome2 == 1) and not StateManager.muted:
                    self.storm_sound.play()
                    
                Variables.outcome = Variables.outcomes[outcome_str]
            else:
                Variables.outcome = 'Rolling..'
        else:
            if not self.kans_dobbel.rolling:
                outcome = self.kans_dobbel.rolledDice + 1                
                
                if self.previous == 2:
                    Variables.outcome = "U heeft " + str(outcome) + " gegooit, u mag hier 1 bij optellen of aftrekken!"
                    self.worp_txt = 'Verder'
                    self.previous = 0
                    self.kans_dobbel.animationFrame = 0
                    return
                elif self.previous == 4:
                    Variables.outcome = "U heeft " + str(outcome) + " gegooit, dit wordt verdubbeld! Zet " + str(outcome*2) + " stappen!"
                    self.worp_txt = 'Verder'
                    self.kans_dobbel.animationFrame = 0
                    self.previous = 0
                    return
                    
                if outcome == 1 or outcome == 6:
                    Variables.outcome = Variables.outcomes_kans[str(outcome)]
                    self.previous = 0
                elif outcome == 2 or outcome == 4:
                    self.previous = outcome
                    outcome_str = str(outcome)
                    result = Variables.outcomes_kans[outcome_str]
                    l = len(result)
                    if l >= 50:
                        result = result[0:l//2] + '\n' + result[l//2:l]
                    Variables.outcome = result
                    self.is_kans = True
                else:                                                                   
                    outcome_str = str(outcome)
                    result = Variables.outcomes_kans[outcome_str]
                    l = len(result)
                    if l >= 50:
                        result = result[0:l//2] + '\n' + result[l//2:l]
                    Variables.outcome = result
                    self.kans_dobbel.animationFrame = 0
                    self.worp_txt = 'Verder'
                    self.previous = 0
                
                
        
    def input_check(self):
        if self.mis(20, 20, 75, 50):
            StateManager.state = StateManager.states.MAINMENU
        elif self.mis(width - 125, 20, 100, 100):
            StateManager.state = StateManager.states.SPELVORDERING
        elif self.mis(width/2-100, height - 200, 200, 100) and not self.rollSound.isPlaying():
            if self.worp_txt == 'Verder':
                self.is_kans = not self.is_kans
                Variables.outcome = 'Werp de dobbelsteen!'
                self.worp_txt = 'Gooi!'
            else:
                if not self.is_kans:
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
                else:
                    self.kans_dobbel.rollDice()
       
        
