
f = open("test1.txt", "r")

line = f.readline()

nvertices = int(line.strip())
line = f.readline()
temp = line.split(' ')
colcount = len(temp)

print('col:', colcount)

rowcount = 0

while line:
    rowcount +=1

    line = f.readline()

print('row:',rowcount)