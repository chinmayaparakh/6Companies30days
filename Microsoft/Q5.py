
class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        st = [] 
        S=[0]*n
        st.append(0)
        S[0] = 1
        for i in range(1, n):
            while( len(st) > 0 and a[st[-1]] <= a[i]):
                st.pop()
            S[i] = i + 1 if len(st) <= 0 else (i - st[-1])
            st.append(i)
        return S
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nikhil Kumar Singh

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
        n = int(input())
        a = list(map(int,input().strip().split()))
        obj = Solution()
        ans = obj.calculateSpan(a, n);
        print(*ans) # print space seperated elements of span array
# } Driver Code Ends
