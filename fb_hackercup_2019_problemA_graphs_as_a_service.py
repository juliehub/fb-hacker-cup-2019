import sys

def findSolution(filename):
    """
    This function find any valid graph consistent with all of these requirements if possible,
    or to determine that no such graph exists.
    
    Args: a file
    
    Input begins with an integer T,
    the number of graphs that Texas Instruments has commissioned. 
    For each graph, there is first a line containing the space-separated integers N and M. 
    Then, M lines follow (M requirements), the ith of which contains the space-separated integers Xi, Yi, and Zi.

    Returns:
    For the ith graph, print a line containing "Case #i: " 
    followed by either an integer E and then a description of a valid graph if possible,
    or the string "Impossible" if no valid graph exists.

    A graph description contains E lines, where E is the number of edges in your graph.
    The ith line contains the space-separated integers Ai, Bi, and Wi indicating that
    there is an edge between nodes Ai and Bi with weight Wi. 
    Please keep in mind that your graph must satisfy all of the requirements stated above
    (both the fundamental requirements dictated by Texas Instruments, and the M customer ones).
    """    
    with open(filename,'r') as in_file, open('output.txt','a') as out_file:
        
        # read T
        T=int(in_file.readline())
        if T<1 or T>1000:
            return "T is out of range!"

        # iterate through each t in T
        for t in range(T):
            # for each graph, read N nodes and M requirements
            NM=list(map(int,in_file.readline().split()))
            N=NM[0]
            M=NM[1]

            #INT_MAX=sys.maxsize -1
            INT_MAX=1000000
            # initialize distance matrix between 2 nodes Xi and Yi
            dist = [[INT_MAX for i in range(N)] for j in range(N)]
            for i in range(N):
                dist[i][i]=0
            
            X=[0]*M
            Y=[0]*M
            Z=[0]*M
             
            # M lines follow
            # the ith of which states that the shortest distance
            # between two different nodes Xi and Yi must be equal to Zi.
            for i in range(M):
                
                # read ith requirement r
                r=list(map(int,in_file.readline().split()))
                #print(r)
                if r[0]<=N and r[0]>=1 and r[1]<=N and r[1]>=1:
                    X[i]=r[0]-1
                    Y[i]=r[1]-1
                    Z[i]=r[2]
                    dist[X[i]][Y[i]]=Z[i]
                    dist[Y[i]][X[i]]=Z[i]
           
            #print("Case #{}: ".format(t+1))
            #print(dist)
            
            # Floyd-Warshall algorithm
            # finding shortest paths in a weighted graph with positive
            # or negative edge weights (but with no negative cycles).
            # Time Complexity O(n3)
            # For any 2 vertices i and j, one should actually minimize the distances
            # between this pair using the first K nodes, so the shortest path will be:
            # minimum( D[i][k] + D[k][j], D[i][j]).
            for k in range(N):
                for i in range(N):
                    for j in range(N):
                        dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

            # For each requirement i that the shortest distance
            # between nodes X_i and Y_i must be Z_i,
            # we will simply have a direct edge between nodes X_i and Y_i
            # having a weight of Z_i. Each such edge helps to satisfy
            # its corresponding requirement without introducing anything
            # superfluous into the graph, so there’s no reason to omit
            # any of these edges. On the other hand, any edge aside from
            # those offers no additional assistance for satisfying
            # any requirements but may result in new conflicts,
            # so there’s no reason to include any edges aside from those M.
           
            skip=False
            for i in range(M):
                if dist[X[i]][Y[i]]!=Z[i] and dist[X[i]][Y[i]]!=INT_MAX:
                    out_file.write("Case #{}: Impossible\n".format(t+1))
                    skip=True
                    break

            # for any given requirement i, other requirements’ edges
            # may cause the shortest distance between nodes X_i and Y_i
            # to be less than the required Z_i.
            
            if not skip:
                out_file.write("Case #{}: {}\n".format(t+1,M))
                for i in range(M):
                    out_file.write("{} {} {}\n".format(X[i]+1,Y[i]+1,Z[i]))
              
if __name__ == "__main__":    
    #findSolution("graphs_as_a_service_sample_input.txt")
    findSolution("graphs_as_a_service.in")
    print("Done")
    
