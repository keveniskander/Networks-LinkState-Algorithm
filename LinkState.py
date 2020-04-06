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
		# print(router_arr[i][j], end = ' ')
	# print()
	line = f.readline()



# line = f.readline()
temp = line.split()

gateway_arr = [0]*len(temp)
for k in range(len(temp)):
	gateway_arr[k] = int(temp[k])

# print()
# print(gateway_arr)
# print()




def lcp(n, k, start, gateway_arr, router_arr):
	
	cost_arr = []
	for i in range(n):
		for j in range(1):
			if i != start:
				cost_arr.append([i,1000,1000])
			else:
				cost_arr.append([i,0,1000])

	min_cost = 10000
	min_vertex = 0
	path = ''
	minval = 1000
	visited = []
	unvisited = [i for i in range(n)]
	


	# cost_count = 0

	# print(cost_arr)
   

	count = 0
	i = start

	while len(visited) < n:

		min_cost = 10000
		# print('visited:', visited)
		# print(cost_arr)
		# print('I =', i+1)
		
		for k in range(n):
			if cost_arr[k][1]<=min_cost and cost_arr[k][0] not in visited:
				# print(min_cost)
				min_cost = cost_arr[k][1] 
				# print(min_cost)
				min_vertex = cost_arr[k][0]

		i = min_vertex

		
		# print(cost_arr)



		for j in range(n):

			# print(router_arr[i][j], end = ' ')

			if router_arr[i][j] > 0 and router_arr[i][j] + cost_arr[i][1] < cost_arr[j][1]:

			

			# if the cost_neighbor + cost_current < cost_neighbor then cost_current = cost_neighbor

				
			
				cost_arr[j][1] = router_arr[i][j] + cost_arr[i][1]



				
			   
		visited.append(i)
		unvisited.remove(i)				


		# print()

	# print(visited)

	return cost_arr


cost_arr = lcp(colcount, len(gateway_arr), 0, gateway_arr, router_arr)
# print(cost_arr)
# print(cost_arr[1][1])

for a in range(colcount):
	# print('dsjknbfg')
	cost_arr = lcp(colcount, len(gateway_arr), a, gateway_arr, router_arr)
	
	if cost_arr[a][0]+1 not in gateway_arr:
		
		print(cost_arr)
		
		print("Forwarding Table for", cost_arr[a][0]+1)
		print("{:>10} {:>10} {:>10}".format("To", "Cost", "Next Hop"))
		for b in range(len(gateway_arr)):
			# print(gateway_arr[b])
			print("{:>10} {:>10} {:>10}".format(gateway_arr[b], cost_arr[gateway_arr[b]-1][1], cost_arr[a][2]))