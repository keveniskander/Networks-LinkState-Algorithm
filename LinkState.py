
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

def lcp(n, gateway_arr, router_arr):

    for i in range(rowcount):
        # print(i)

        minval = router_arr[i][0]
        if i + 1 not in gateway_arr:

            for j in range(colcount):

                print(router_arr[i][j], end = ' ')

                if router_arr[i][j] > 0:
                    
                    if router_arr[i][j] < minval:
                        
                        minval = router_arr[i][j]
            print('MIN: ', minval)        
                    


        print()
    print('TEST')


lcp(colcount, gateway_arr, router_arr)


    