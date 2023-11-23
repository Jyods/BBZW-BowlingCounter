
class Throw():
    def __init__(self, npins1:int, npins2:int=0):
        self.npins1 = npins1
        self.npins2 = npins2

    @property
    def calc_points(self):
        return self.npins1 + self.npins2

throws:list[Throw] = []

def calc_points():
    total_points = 0
    frame = 1
    throw_index = 0

    while frame <= 10 and throw_index < len(throws):
        current_throw = throws[throw_index]
        total_points += current_throw.calc_points

        if current_throw.npins1 == 10:  # Strike
            total_points += calc_strike_bonus(throw_index)
            throw_index += 1
        elif current_throw.calc_points == 10:  # Spare
            total_points += calc_spare_bonus(throw_index)
            throw_index += 2
        else:
            throw_index += 2

        frame += 1

    return total_points

def calc_strike_bonus(throw_index):
    next_throw = throws[throw_index + 1]
    return next_throw.calc_points

def calc_spare_bonus(throw_index):
    next_throw = throws[throw_index + 2]
    return next_throw.npins1

# Example usage:
for ri in range(12):
    pins = []
    for ti in range(2):
        pins.append(int(input(f"Runde {ri+1}, Wurf {ti+1}: Wie viele pins wurden umgeworfen?\n> ")))
    throws.append(Throw(*pins))

#throws.append(Throw(1, 4))
#throws.append(Throw(4, 5))
#throws.append(Throw(6, 4))  # Spare
#throws.append(Throw(5, 5))  # Spare
#throws.append(Throw(10))    # Strike
#throws.append(Throw(0, 1))

total_score = calc_points()
print("Total Score:", total_score)
