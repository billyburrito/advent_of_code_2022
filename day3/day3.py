import string
from collections import Counter
# build values
value={}
seed = 1
sack = 0
trike = 0
three = {}
badge = 0

for i in range(ord('a'), ord('z')+1):
    value[chr(i)] = seed
    seed += 1

for i in range(ord('A'), ord('Z')+1):
    value[chr(i)] = seed
    seed += 1


with open('./input') as fp:
    for string in fp:
        first, second = string[:len(string)//2], string[len(string)//2:]
        dfirst = Counter(first)
        dsecond = Counter(second)
        common = dfirst & dsecond
        char = (list(common.keys())[0])
        sack += value[char]
        # part 2
        three[trike] = string
        if trike == 2 :
            trike = 0
            badge0 = Counter(three[0])
            badge1 = Counter(three[1])
            badge2 = Counter(three[2])
            thebadge = badge0 & badge1 & badge2
            officialbadge = list(thebadge.keys())[0]
            badge += value[officialbadge]
        else:
            trike += 1
        



print("Part one: " + str(sack))
print("Part two: " + str(badge))