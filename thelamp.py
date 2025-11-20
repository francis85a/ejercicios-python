class Lamp:
    def __init__(self, color):
        self.color = color
        self.on = False
    
    def toggle_switch(self):
        self.on = not self.on
    
    def state(self):
        if self.on:
            return "The lamp is on."
        else:
            return "The lamp is off."