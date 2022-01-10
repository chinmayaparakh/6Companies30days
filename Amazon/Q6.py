from collections import deque

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        #code here
        ans = deque()
        out = []
        for i in range(k):
            while ans and arr[i] >= arr[ans[-1]]:
                ans.pop()
            ans.append(i);
        for i in range(k, n):
            out.append(arr[ans[0]])
            while ans and ans[0] <= i-k:
                ans.popleft() 
            while ans and arr[i] >= arr[ans[-1]] :
                ans.pop()
            ans.append(i)
        out.append(arr[ans[0]])
        return out
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends
