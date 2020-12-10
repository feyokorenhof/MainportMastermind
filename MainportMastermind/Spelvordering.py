class Spelvordering():
    def __init__(self):
        print('spelvordering yaaas')  
        self.players = { "Jan", "Dirk", "John" }
        self.colors = [{'naam': 'rood', 'kleur': color(255, 0, 0)}, { 'naam': 'groen', 'kleur': color(0, 255, 0)}, { 'naam': 'blauw', 'kleur': color(74, 112, 247)}]
        
    def render(self):
        self.drawPlayers()
        
    def drawPlayers(self):
        fill(12, 12, 12)
        rect(20, 20, 400, 400)
        for index, value in enumerate(self.players):            
            fill(self.colors[index]['kleur'])
            textSize(20)
            textAlign(CORNER)
            text(self.colors[index]['naam'] + ": " + value, 20, 40 + (20 * index))
        
        
        
    def MouseInSpace(self, x, y, w, h):
        return ((mouseX > x) and (mouseX < x+w) and (mouseY > y) and (mouseY < y+h))
