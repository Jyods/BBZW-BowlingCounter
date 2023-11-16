from enum import Enum

class Art(Enum):
    Normal = 1
    Strike = 2
    Spare = 3
    Foul = 4

class Wurf:
    def __init__(self, wurfart: Art, pins: int = 0):
        self.wurfart = wurfart
        match self.wurfart:
            case Art.Normal:
                self.pins = pins
            case Art.Strike:
                self.pins = 10
            case Art.Spare:
                self.pins = 10 - pins
            case Art.Foul:
                self.pins = 0
        self.pins = pins

class Spielzug:
    def __init__(self, wurf1:Wurf|None, wurf2:Wurf|None):
        self.wurf1 = wurf1
        self.wurf2 = wurf2

    def geworfen(self, wurf:Wurf):
        if self.wurf1 == None:
            self.wurf1 = wurf
            if wurf.wurfart == Art.Strike:
                self.wurf2 = Wurf(Art.Foul)
        elif self.wurf2 == None:
            self.wurf2 = wurf
        else:
            raise Exception("Spielzug ist schon vollständig")

class Player:
    def __init__(self, name:str, points=0):
        self.name = name
        self.points = points

    