import Counter

pins:list[int] = []

for ri in range(12):

    for ti in range(2):
        num = None
        while num == None:
            inp = input(f"Runde {ri+1}, Wurf {ti+1}: Wie viele pins wurden umgeworfen?\n> ")
            if inp.isnumeric() and int(inp) <= 10:
                num = int(inp)
            else:
                print("Invalid input! Try again.")
        pins.append(num)
    
    print(pins)
    print(f"Score: {Counter.bowling_score(pins)}")
    