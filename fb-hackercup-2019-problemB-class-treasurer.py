def findSolution(filename):
    """
    https://www.facebook.com/codingcompetitions/hacker-cup/2019/round-1/problems/B
    https://www.youtube.com/watch?v=HzeK7g8cD0Y
    This function find the minimum possible cost required to guarantee
    that Betty cannot possibly win and become the class treasurer
    
    Args: a file
    
    Input begins with an integer T, the number of elections.
    For each election, there are two lines.
    The first line contains the space-separated integers N and K.
    The second line contains the N characters V1 through VN.

    Returns:
    For the ith election, print a line containing
    "Case #i: " followed by 1 integer, the minimum possible cost
    (in dollars) required to guarantee that Betty cannot become
    the class treasurer, modulo 1,000,000,007.

    """    
    with open(filename,'r') as in_file, open('problemB_output.txt','w') as out_file:
        
        # read T
        T=int(in_file.readline())

        #precompute the value of (2^i) modulo 1,000,000,007 for all values of i in advance
        #1 ≤ N ≤ 1,000,000
        MOD = 10**9+7
        C = [0]*(10**6+1)
        C[0] = 2
        for i in range(1,len(C)):
            C[i] = (C[i-1]*2) % MOD
                
        # iterate through each t in T
        for t in range(T):
            # for each graph, read N nodes and K requirements
            NK=list(map(int,in_file.readline().split()))
            N=NK[0]
            K=NK[1]
            #print("Case #{}: ".format(t+1))
            #print(N,K)
            
            # voting choice list
            V=in_file.readline()
            #V=in_file.readline().split()
            #print("Case #{}: ".format(t+1))
            #print(V)
            
            #the minimum possible cost (in dollars) required
            result=0
            #difference d between # of votes a and b
            d = 0
            
            #greedy algorigthm
            #The cost of paying off any given student x outweighs
            #the costs of paying off any subset of the first x-1 students,
            #as 2^x > ∑{i = 1..(x-1) | 2^i}. Therefore, our top priority
            #should be to avoid changing student N’s vote, our next priority
            #should be to avoid changing student (N-1)’s vote, and so on.
            for i in range(N-1,-1,-1):
                #if V[i] = 'A', we’ll leave student i alone
                if V[i]=='A':
                    d=max(d-1,0)
                else:
                    if d<K:
                        d=d+1
                    else:
                        #pay 2^i dollars to have student i change their vote to Amy
                        result=(result+C[i]) % MOD
                        d=max(d-1,0)
                        
            print("Case #{}: {}\n".format(t+1,result))
            out_file.write("Case #{}: {}\n".format(t+1,result))
            
if __name__ == "__main__":    
    #findSolution("class_treasurer_sample_input.txt")
    findSolution("class_treasurer_input.txt")
    print("Done")
