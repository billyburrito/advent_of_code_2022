import copy
col = {}
newcol = {}
for i in range(1,10):
    col[i] = []
ops = False

def move_crate ( count, src, dst):
    for i in range(int(count)):
        col[int(dst)].append(col[int(src)].pop())

def move_crates ( count, src, dst):
        newcol[int(dst)] += (newcol[int(src)][int(count)*(-1):]) # add, dont append
        for x in range(int(count)):
            newcol[int(src)].pop() # remove after we are done

with open('./input') as fp:
    for line in fp:
        if line != '\n':
            if ops:
                order = line.strip().split()
                move_crate(order[1], order[3], order[5])
                move_crates(order[1], order[3], order[5])
            else: 
                # we parse
                if line[1] != ' ':
                    col[1].append(line[1])
                if line[5] != ' ':
                    col[2].append(line[5])
                if line[9] != ' ':
                    col[3].append(line[9])
                if line[13] != ' ':
                    col[4].append(line[13])
                if line[17] != ' ':
                    col[5].append(line[17])
                if line[21] != ' ':
                    col[6].append(line[21])
                if line[25] != ' ':
                    col[7].append(line[25])
                if line[29] != ' ':
                    col[8].append(line[29])
                if line[33] != ' ':
                    col[9].append(line[33])
        else:
            ops = True
            for i in range(1,10):
                col[i].reverse()
                newcol = copy.deepcopy(col) # if we dont deepcopy, we get messy

part1 = ''
for i in range(1,10):
    part1 += col[i][-1]
part2 = ''
for i in range(1,10):
    part2 += newcol[i][-1]

print("part 1: " + part1)
print("part 2: " + part2)
