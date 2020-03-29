
f = open("test1.txt", "r")

line = f.readline()

nvertices = int(line.strip())
line = f.readline()
temp = line.split(' ')
print(temp)
colcount = len(temp)


rowcount = -1

while line:
    rowcount +=1
    # print(line)
    line = f.readline()

print('col:', colcount)
print('row:',rowcount)

router_arr = [[0 for i in range(colcount)]for j in range(rowcount)]

for i in range(colcount):
    for j in range(rowcount):
        print(router_arr[i][j])