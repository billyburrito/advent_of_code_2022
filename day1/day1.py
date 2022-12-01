index = 0
elves = list()
top3 = 0

# init the first one
elves.append(0)

with open('input') as fp:
    for line in fp:
        if line.strip():
            elves[index] += int(line)
        else:
            elves.append(0)
            index += 1

print("part 1: "+ str(max(elves)))

for i in range(3):
    maxVal = max(elves)
    top3 += maxVal
    elves.remove(maxVal)

print("part 2: "+ str(top3))

