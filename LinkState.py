
f = open("test1.txt", "r")

line = f.readline()

nvertices = int(line.strip())
# line = f.readline()
# temp = line.split(' ')
# print(temp)


rowcount = -1
colcount = nvertices

for line in f:
    rowcount += 1

print(rowcount)
print(colcount)
# f.seek(1)

f = open("test1.txt", "r")

f.seek(1)

# line = f.readline()
# print(line)
# temp = line.split(' ')
# print(temp)

# print('col:', colcount)
# print('row:',rowcount)

router_arr = [[0 for i in range(colcount)]for j in range(rowcount)]

temp = [rowcount]

for i in range(colcount):
    temp = line.split()
    for j in range(rowcount):
        # router_arr[i][j] = temp[j]
        print(router_arr[i][j], end = ' ')
    print()
    line = f.readline()



# f = open("test1.txt", "r")

# line = f.readline()

# for k in range(colcount):
#     for l in range(rowcount):
#         router_arr[k][j] = 1