
class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        dct=dict()
        arr.sort()
        for i in arr:
            if i in dct:
                dct[i]+=1
            else:
                dct[i]=1
        vmx=max(dct.values())
        for i in arr:
            if dct[i]==vmx:
                lst=[i,vmx]
                return lst 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends
