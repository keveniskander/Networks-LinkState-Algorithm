
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




def lcp(n, k, start, gateway_arr, router_arr):
    
    cost_arr = []
    for i in range(n):
        for j in range(1):
            if i != start:
                cost_arr.append([i,1000])
            else:
                cost_arr.append([i, 0])

    min_cost = 10000
    min_vertex = 0
    neighbor = 0
    path = ''
    minval = 1000
    visited = []
    unvisited = [i for i in range(n)]
    


    # cost_count = 0

    print(cost_arr)
   

    count = 0
    i = start

    while len(visited) < n:

        min_cost = 10000
        print('visited:', visited)
        
        for k in range(n):
            if cost_arr[k][1]<min_cost and cost_arr[k][0] not in visited:
                print(min_cost)
                min_cost = cost_arr[k][1] 
                print(min_cost)
                min_vertex = cost_arr[k][0]

        i = min_vertex

        print('I =', i+1)
        print(cost_arr)



        for j in range(n):

            # print(router_arr[i][j], end = ' ')

            neighbor = j+1

			

            if router_arr[i][j] > 0 and router_arr[i][j] + cost_arr[i][1] < cost_arr[neighbor-1][1]:

            

            # if the cost_neighbor + cost_current < cost_neighbor then cost_current = cost_neighbor

                # print('FUCK')
            
                cost_arr[j][1] = router_arr[i][j] + cost_arr[i][1]



                
               
        visited.append(i)
        unvisited.remove(i)
        
        # for i in range(len(visited)):
        #     print(visited[i]+1, end = '')
        # print()

        # count +=1

                 
                    


        print()

    print(cost_arr)

    # for i in range(n):
    #     for j in range(1):
    #         print(cost_arr[i][j], end = ' ')

    # print()

    # print('minval: ', minval_arr)
    # print('visited: ', visited)

    # print('path: ', path)
    # for i in range(n):
    #     for j in range(n):
    #         print(cost_arr[i][j], end = '')
    #     print() 

    path_arr = list(map(int, path))
    # print(path_arr)

    cost = 0
    nh = 0

    # for a in range(n-k):

    #     print("Forwarding Table for ", path_arr[a])
    #     print("{:>10} {:>10} {:>10}".format("To", "Cost", "Next Hop"))

    #     for b in range(len(gateway_arr)):
            
    #         print(router_arr[path_arr[a]][gateway_arr[b]])
    #         if router_arr[path_arr[a]-1][gateway_arr[b]-1] != -1:
    #             print(path_arr[a]-1)
    #             cost = router_arr[path_arr[a]-1][gateway_arr[b]-1]
    #             nh = gateway_arr[b]
    #             print(router_arr[path_arr[a]-1][gateway_arr[b]-1])
    #             nh = path_arr[-1]

    #         else: 
    #             nh = 0
    #             cost = 0

    #         print("{:>10} {:>10} {:>10}".format(gateway_arr[b], cost, nh))
        
    #     print()


lcp(colcount, len(gateway_arr), 0, gateway_arr, router_arr)