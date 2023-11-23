
class Throw():
    def __init__(self, npins1:int, npins2:int):
        self.npins1 = npins1
        self.npins2 = npins2

    @property
    def calc_points(self):
        return self.npins1 + self.npins2

throws:list[Throw] = []

def calc_points():
    points = 0
    # TODO
    return points