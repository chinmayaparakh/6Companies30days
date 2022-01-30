
class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        M = 1000000007
        N %= M
        if R == 0:
            return 1
        if R == 1:
            return N
        tmp = self.power(N, R // 2)
        res = (tmp * tmp) % M
        if R % 2 != 0:
            res = (res * N) % M
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
