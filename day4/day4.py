count = 0
overlap = 0

with open('./input') as fp:
    for line in fp:
        group1, group2 = line.strip().split(',')
        value1 = group1.split('-')
        value2 = group2.split('-')

        if (int(value1[0]) <= int(value2[0]) and int(value1[1]) >= int(value2[1])) or (int(value2[0]) <= int(value1[0]) and int(value2[1]) >= int(value1[1])):
            count += 1
        if range(max(int(value1[0]), int(value2[0])), min(int(value1[1]), int(value2[1]))+1):
            overlap += 1

print ("Part one: " + str(count))
print ("Part two: " + str(overlap))