# CP372_A3

##DESCRIPTION:

In this assignment I have implemented a core functionality of the Link State routing algorithm for
an autonomous system. The input to the algorithm is a weighted directed graph with n vertices
( labeled with 1, 2, 3,..., n ) that represents topology of a particular autonomous system. Each
vertice represents a router or a gateway router in the network. The gateway routers are
specified in the input as well. The output should print the forwarding table for each router other
than the gateway routers. Each entry in a forwarding table shows the next hop node along the
shortest path route from that node (source) to a gateway router (destination).

##EXAMPLE INPUT:

6
0 1 10 -1 -1 2
10 0 1 -1 -1 -1
1 10 0 -1 -1 -1
-1 -1 2 0 1 10
-1 -1 -1 10 0 1
-1 -1 -1 1 10 0
2 5
