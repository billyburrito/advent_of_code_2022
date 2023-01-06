from monkey import Monkey
group = []

with open('./input') as fp:
    for line in fp:
        if line != '\n':
            input = line.strip().split()
#            print(input)
            if input[0] == 'Monkey':
                group.append(Monkey(input[1][0]))
            if input[0] == 'Starting':
                items = line.strip().split(':')[1].split(',')
                group[-1].add_things(items)
            if input[0] == 'Operation:':
                group[-1].add_operation(line.strip().split('=')[1])
            if input[0] == 'Test:':
                group[-1].add_divisor(line.strip().split()[3])
            if input[0] == 'If':
                if input[1] == 'true:':
                    group[-1].add_true(input[-1])
                if input[1] == 'false:':
                    group[-1].add_false(input[-1])

for z in range(20):
    for y in range(len(group)):
        while group[y].things:
            output = group[y].throw_next()
            if output:
                group[output[0]].add_thing(output[1])
#    print(group)

inspects = list()
for x in range(len(group)):
    inspects.append(group[x].inspect_count)

inspects.sort(reverse=True)
print("part 1: " + str(inspects[0] * inspects[1]))

