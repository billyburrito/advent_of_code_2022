from dir import Dir
root = Dir('/', None)
dir = root
part1 = 0
sizeidx = list()

def traverse(data):
    global part1
    global sizeidx
    volume = data.calc_size()
    sizeidx.append(volume)
    if volume <= 100000:
        part1 += volume
    #print(data.name + " " + str(volume))
    for r in data.dirs.keys():
        traverse(data.dirs[r])

with open('./input') as fp:
    for line in fp:
        data = line.strip().split()
        if data[0] == '$': # its a command
            if data[1] == 'cd':
                if data[2] == '..':
                    dir = dir.parent
                elif data[2] == '/':
                    dir = root
                else:
                    dir = dir.dirs[data[2]]
        else:
            if data[0] == 'dir':
                if data[1] in dir.dirs.keys():
                    print("already there")
                else:
                    dir.add_dir(data[1])
            else:
                if data[1] in dir.files.keys():
                    print("already there")
                else:
                    dir.add_file(data[1], data[0])

total = root.calc_size()
#print("total: " + str(total))
#print(root)

traverse(root)
newlist = sorted(sizeidx)

print("part 1: " + str(part1))

for i in newlist:
    if 70000000 - total + i >= 30000000:
        print("part 2: " + str(i))
        break