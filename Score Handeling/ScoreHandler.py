import os, requests, math

header = {
    "User-Agent": "ChallengePoints (https://github.com/thijnmens/ChallengePoints)"
}

#Get Scores from BeatSavior
def getScore(userID):
    weight = int(input('What is the weight of the map?:\n'))
    acc = float(input('What score did you get?:\n'))
    cpm = (50/(0.5+(math.e**(-1*(0.08*(acc-65.4))))))/100
    cp = round(weight*cpm, 2)
    print(f'You got {cp}CP!')

userID = 0
getScore(userID)