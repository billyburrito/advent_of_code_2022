originx = 500
originy = 500
ropelen = 10 # our indexes start at 0 so we are good
rope = {}
for num in range(ropelen):
    rope[num] = [originx, originy]

grid = list()
size = 1000

def checkRight(chain, limit):
    if (rope[chain][0] - rope[chain+1][0]) > limit: # move right
        rope[chain+1][0] += 1
        if limit:
            checkUp(chain,0)
            checkDown(chain,0)

def checkLeft(chain, limit):
    if (rope[chain+1][0] - rope[chain][0]) > limit: # move left
        rope[chain+1][0] -= 1
        if limit:
            checkUp(chain,0)
            checkDown(chain,0)

def checkUp(chain, limit):
    if (rope[chain][1] - rope[chain+1][1]) > limit: # move up
        rope[chain+1][1] += 1
        if limit:
            checkLeft(chain,0)
            checkRight(chain,0)

def checkDown(chain, limit):
    if (rope[chain+1][1] - rope[chain][1]) > limit: # move down
        rope[chain+1][1] -= 1
        if limit:
            checkLeft(chain,0)
            checkRight(chain,0)

def checkTail():
    for z in range(ropelen-1):
        checkRight(z,1)
        checkLeft(z,1)
        checkUp(z,1)
        checkDown(z,1)
    grid[rope[ropelen-1][0]][rope[ropelen-1][1]] = 1

for a in range(size):
    grid.append([0 for b in range(size)])

with open('./input') as fp:
    for line in fp:
        input = line.strip().split()
        #print(input)
        for z in range(int(input[1])):
            if input[0] == 'U':     #x axis
                rope[0][0] += 1
            elif input[0] == 'D':
                rope[0][0] -= 1
            elif input[0] == 'L':   #y axis
                rope[0][1] -= 1
            elif input[0] == 'R':
                rope[0][1] += 1
            checkTail()

print("answer 1: " + str(sum([i.count(1) for i in grid])))
