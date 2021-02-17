from functionlib import *

print('--------------')

score = int(input('Score: '))
mods = input('modifiers: ').split(', ')
notes = int(input('notes: '))
weight = int(input('weight: '))

pog = modtoraw(score, mods)
acc = scoretoacc(notes, pog)
cp = getScore(0, acc, weight)

print('--------------')
print(f'acc = {acc}')
print(f'cp = {cp}')