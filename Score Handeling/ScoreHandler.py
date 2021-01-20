#Get Scores from BeatSavior
def getScore(userID):
    weight = int(input('What is the weight of the map?:\n'))
    acc = float(input('What score did you get?:\n'))
    f = (-0.0000000089146*acc**5)+(0.0000036255812*acc**4)+(-0.0004061889074*acc**3)+(0.003306769423*acc**2)+(1.9970958028178*acc)
    if (0 <= acc <= 135):
        g = (2*acc)-(f)
        h = g/100
    else:
        h = 0
    cp = round(weight*h, 2)
    print(f'You got {cp}CP!')

userID = 0
getScore(userID)