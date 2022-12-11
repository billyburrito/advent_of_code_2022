register = 1
cycle = 1
interval = []
total = 0
output = ''
linemax = 0

for x in range(20, 221, 40):
    interval.append(x)

def checkCycle():
    global cycle
    global total 
    global register
    global output
    global linemax

    if register + 1 >= linemax and register - 1 <= linemax:
        output += '#'
    else:
        output += '.'
    if cycle in interval:
        total += cycle * register

    cycle += 1
    linemax += 1

    if linemax == 40:
        linemax -= 40


with open('./input') as fp:
    for line in fp:
        input = line.strip().split()
        if input[0] == 'noop':
            checkCycle()
        elif input[0] == 'addx':
            checkCycle()
            checkCycle()
            register += int(input[1])

print("part 1: " + str(total))
print("part2:")
print(output[0:39]+"\n"+output[40:79]+"\n"+output[80:119]+"\n"+output[120:159]+"\n"+output[160:199]+"\n"+output[200:])
