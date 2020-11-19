class MainGame():
    def __init__(self):
        self.bg = loadImage('images/bg.png')
        self.bg.resize(width, height)
        self.game_started = False
        self.paused = False
    
    def draw_static(self):
        image(self.bg, 0, 0)
