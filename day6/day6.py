count = 0
count2 = 0

with open('./input') as fp:
    for line in fp:
        for i in range(len(line)-4):
            if len(set(line[i:i+4])) == 4:
                break
            count += 1
        for r in range(len(line)-14):
            if len(set(line[r:r+14])) == 14:
                break
            count2 += 1

count += 4 # add the set of chars being looked at
print("Part one: " + str(count))
count2 += 14 # add the set of chars being looked at
print("Part two: " + str(count2))