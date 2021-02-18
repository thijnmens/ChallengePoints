# ChallengePoints

Challenge Ranking System for Beat Saber

# How do we calculate the wight of a map?

these are the criteria we set for a map

-   Amount of notes
-   Notes on natural side
-   Avg angle Change
-   Avg swing distance

i'll explain all of them in depth later, but before that there is some basic knowledge you should have before reading any of this
So the map is devided into chunks and those chunks give point values which later get added up into a final point level, which is the weight of the map. each chunk is 2 beats long, the program runs twice, 1 time starting from beat 0 and 1 time starting from beat 1 to avoid severe angle changes between the first chunks not being counted for in the final cp value.

## Amount of notes

This one is selfexplainatory, its the amount of notes in a chunk.

#### 1 note = 1 point

## Notes on the natural side

If you watched or played any beat saber you know that blue is on the right and red is on the left, but some maps like to switch this a round sometimes, which should lead to an increase of score.

#### 1 point for each note that isnt on the correct side

## Avg angle change

This one is a bit more difficult, so bare with me here, so basically what it does is it draws 2 lines through each note, then when the lines hit (if they hit, more on this later) it takes 2 angles, left angle and the right angle, then the smallest of these 2 angles is the amount of points one gets, then we also need another value, the distancemod, this is the amount of beats between the 2 notes devided by 10 so the number is smaller then 1.

#### The amount of points is the (angle/45+1)\*distancemod

## Avg swing distance

This one is also a selfexplenatory one, it takes the avg distance between the notes.

#### The amount of points is the distance between the notes
