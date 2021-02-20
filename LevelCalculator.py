import json
from functionlib import *
input('Please make sure the file you want to evaluate is in the same folder as this file and is called "song.dat"\n press enter to continue')

#Split song into chunks
createChunks(getNotes('song.dat'))
#Read json outputs of the chunk split into variables
with open('dict0.json') as json_file:
    dict0 = json.load(json_file)
with open('dict1.json') as json_file:
    dict1 = json.load(json_file)
#While loops to cycle through the dicts and collect all the LineIndex' and LineLayers (Point A and B) and collect the Notes/Chunk
a = 0
lines1 = []
NC = 0
while a < len(dict0):
    NC = NC + (len(f'dict0[chunk{a}]')*0.25)
    if dict0[f'chunk{a}'] != [] and len(dict0[f'chunk{a}']) >= 3:
        b = str(dict0[f'chunk{a}']).split('\'')
        c = len(dict0[f'chunk{a}'])
        d = 0
        while True:
            try:
                e = str(dict0[f'chunk{a}'][d]).split(',')
                lines1.append(f'{a}~{e[1]}~{e[2]}')
                d = d + 1
            except IndexError:
                d = 0
                break
    a = a + 1
a = 0
lines2 = []
while a < len(dict1):
    NC = NC + (len(f'dict1[chunk{a}]')*0.25)
    if dict1[f'chunk{a}'] != [] and len(dict1[f'chunk{a}']) >= 3:
        b = str(dict1[f'chunk{a}']).split('\'')
        c = len(dict1[f'chunk{a}'])
        d = 0
        while True:
            try:
                e = str(dict1[f'chunk{a}'][d]).split(',')
                lines2.append(f'{a}~{e[1]}~{e[2]}')
                d = d + 1
            except IndexError:
                d = 0
                break
    a = a + 1
print(f'Amount of notes: {NC}')
#Create dict with triangles
a = 0
b = 0
triangles1 = []
while a < len(lines1):
    try:
        g = str(lines1[a]).split('~')
        h = str(lines1[a+1]).split('~')
        if g[0] == h[0]:
            c = f'{g[1]}~{g[2]}'
            d = f'{h[1]}~{h[2]}'
            f = g[0]
            triangles1.append(f'{f}~{c}~{d}')
    except IndexError:
        break
    a = a + 1
    b = b + 2
a = 0
b = 0
triangles2 = []
while a < len(lines2):
    try:
        g = str(lines2[a]).split('~')
        h = str(lines2[a+1]).split('~')
        if g[0] == h[0]:
            c = f'{g[1]}~{g[2]}'
            d = f'{h[1]}~{h[2]}'
            f = g[0]
            triangles2.append(f'{f}~{c}~{d}')
    except IndexError:
        break
    a = a + 1
    b = b + 2
#From the triangle dicts get the lenght between the 2 points and add the Avg Swing Distance points to the point dict
a = 0
ASD = 0
while a < len(triangles1):
    try:
        b = str(triangles1[a]).split('~')
        c = int(str(b[1]).split(':')[1])
        d = int(str(b[2]).split(':')[1])
        e = int(str(b[3]).split(':')[1])
        f = int(str(b[4]).split(':')[1])
        ASD = ASD + getLenght(c, e, d, f)
    except IndexError:
        break
    a = a + 1
a = 0
while a < len(triangles2):
    try:
        b = str(triangles2[a]).split('~')
        c = int(str(b[1]).split(':')[1])
        d = int(str(b[2]).split(':')[1])
        e = int(str(b[3]).split(':')[1])
        f = int(str(b[4]).split(':')[1])
        ASD = ASD + getLenght(c, e, d, f)
    except IndexError:
        break
    a = a + 1
ASD = round(ASD, 2)
print(f'Avg Swing Distance: {ASD}')
print(f'Total: {round(ASD+NC, 2)}')
