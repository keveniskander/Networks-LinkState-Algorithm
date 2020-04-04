
f = open("test1.txt", "r")

line = f.readline()

nvertices = int(line.strip())


rowcount = -1
colcount = nvertices

for line in f:
    rowcount += 1

# print(rowcount)
# print(colcount)



router_arr = [[0 for i in range(colcount)]for j in range(rowcount)]

temp_arr = [0] * colcount

f.seek(0)
# print('temp: ', temp_arr)

# i want to use seek here but it's not working. need to fix that

f = open("test1.txt", "r")

f.readline()

line = f.readline()


for i in range(colcount):
    temp = line.split()
    # print(temp)

    for j in range(rowcount):
        # print(temp[j], end = ' ') 
        router_arr[i][j] = int(temp[j])
        print(router_arr[i][j], end = ' ')
    print()
    line = f.readline()



# line = f.readline()
temp = line.split()

gateway_arr = [0]*len(temp)
for k in range(len(temp)):
    gateway_arr[k] = int(temp[k])

print()
print(gateway_arr)
print()




def lcp(n, k, gateway_arr, router_arr):
    
    cost_arr = [[[0,0] for i in range(n)]for j in range(n)]
    path = ''

    cost_count = 0

    for i in range(n):
        for j in range(n):
            print(cost_arr[i][j], end = ' ')

        print()

    for i in range(n):
        # print(i)


        minval = 1
        if i + 1 not in gateway_arr:

            for j in range(n):

                print(router_arr[i][j], end = ' ')

                if router_arr[i][j] > 0:

                    cost_arr[i][j] = [i+1, router_arr[i][j]]
                    
                    if router_arr[i][j] < minval:
                        
                        minval = router_arr[i][j]
                        
                
            print('MIN: ', minval)

            path+=str(i+1)

                 
                    


        print()

    print('path: ', path)
    for i in range(n):
        for j in range(n):
            print(cost_arr[i][j], end = '')
        print() 

# def getMin(colcount, router_array):

#     current = 1

#     for i in range(colcount):
        
#         if router_arr[i]




lcp(colcount, len(gateway_arr), gateway_arr, router_arr)