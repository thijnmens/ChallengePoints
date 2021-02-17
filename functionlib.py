

def modtoraw(score, mods):
    ######################################
    # List of mods                       #
    # NF, NO, NB, SS, IF, BE, DA, FS, GN #
    ######################################
    amount = len(mods)
    a = 0
    mod = 1
    while a < amount:
        if mods[a] == 'NF':
            mod = mod - 0.5
        elif mods[a] == 'NO':
            mod = mod - 0.95
        elif mods[a] == 'NB':
            mod = mod - 0.90
        elif mods[a] == 'SS':
            mod = mod - 0.70
        elif mods[a] == 'IF':
            mod = mod + 0.16
        elif mods[a] == 'BE':
            mod = mod + 0.10
        elif mods[a] == 'DA':
            mod = mod + 0.07
        elif mods[a] == 'FS':
            mod = mod + 0.08
        elif mods[a] == 'GN':
            mod = mod + 0.11
        a = a + 1
    score = score * mod
    round(score, 0)
    return score

def scoretoacc(notes, score):
    notes = notes - 14
    a = notes*920
    b = a+4830
    acc = round((score/b)*100, 4)
    return acc

def getScore(userID, acc, weight):
    f = (-0.0000000089146*acc**5)+(0.0000036255812*acc**4)+(-0.0004061889074*acc**3)+(0.003306769423*acc**2)+(1.9970958028178*acc)
    if (0 <= acc <= 135):
        g = (2*acc)-(f)
        h = g/100
    else:
        h = 0
    cp = round(weight*h, 2)
    return cp