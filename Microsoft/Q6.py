
class Solution:
    
    #Function to find list of all words possible by pressing given numbers.
    def posword(i,cur,ans,N,lst,a):
        if i==N:
            ans.append("".join(cur))
            return
        for ch in lst[a[i]]:
            cur.append(ch)
            Solution.posword(i+1,cur,ans,N,lst,a)
            cur.pop()
    
    def possibleWords(self,a,N):
        #Your code here
        lst={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        ans=[]
        Solution.posword(0,[],ans,N,lst,a)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        res = ob.possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
