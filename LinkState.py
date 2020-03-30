
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



# print('col:', colcount)
# print('row:',rowcount)

router_arr = [[0 for i in range(colcount)]for j in range(rowcount)]

temp_arr = [0] * colcount

f.seek(0)
# print('temp: ', temp_arr)

for i in range(colcount):
    temp = line.split()
    print(temp)
    for j in range(rowcount):
        print(temp[j], end = ' ') 
        # print(router_arr[i][j], end = ' ')
    print()
    line = f.readline()



# f = open("test1.txt", "r")

# line = f.readline()

# for k in range(colcount):
#     for l in range(rowcount):
#         router_arr[k][j] = 1