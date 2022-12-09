grid = list()
visible = 0
scenic = 0

with open('./input') as fp:
    for line in fp:
        grid.append([int(i) for i in line.strip()])

xmax = len(grid)-1
ymax = len(grid[0])-1

def maxup(first,second):
    templist = list()
    for x in range(0,first): 
        templist.append(grid[x][second])
    return max(templist)

def maxdown(first,firstmax,second):
    templist = list()
    for x in range(first+1,firstmax+1): 
        templist.append(grid[x][second])
    return max(templist)

def checkNorth(one,two):
    origin = one
    count = 0
    while True:
        one -= 1
        count += 1
        if one == 0 or grid[one][two] >= grid[origin][two]:
            break
    return count

def checkSouth(one,two):
    origin = one
    count = 0
    while True:
        one += 1
        count += 1
        if one == xmax or grid[one][two] >= grid[origin][two]:
            break
    return count

def checkWest(one,two):
    origin = two
    count = 0
    while True:
        two -= 1
        count += 1
        if two == 0 or grid[one][two] >= grid[one][origin]:
            break
    return count

def checkEast(one,two):
    origin = two
    count = 0
    while True:
        two += 1
        count += 1
        if two == ymax or grid[one][two] >= grid[one][origin]:
            break
    return count

for x in range(len(grid)):
    for y in range(len(grid[x])):
        #print(grid[x][y])
        if x == 0 or y == 0 or x == xmax or y == ymax:
            visible += 1
        elif grid[x][y] > max(grid[x][:y]):
            visible += 1
        elif grid[x][y] > max(grid[x][y+1:]):
            visible += 1
        elif grid[x][y] > maxup(x,y): # check 'bottom'
            visible += 1
        elif grid[x][y] > maxdown(x,xmax,y): # check 'bottom'
            visible += 1

        if x == 0 or y == 0 or x == xmax or y == ymax:
            next
        else:
            north = checkNorth(x,y)
            east = checkEast(x,y)
            south = checkSouth(x,y)
            west = checkWest(x,y)

            # print("north is: " + str(north))
            # print("south is: " + str(south))
            # print("west is: " + str(west))
            # print("east is: " + str(east))

            factor = north * east * south * west
            if factor > scenic:
                scenic = factor

print("part 1: " + str(visible))
print("part 2: " + str(scenic))
