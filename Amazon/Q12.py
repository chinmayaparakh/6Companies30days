//My output is same a expected putput but still GFG compiler is showing WA.

MAX=50
class Solution:
    def colName (self, n):
        # your code here
        s = ["\0"] * MAX
        i = 0
        t=''
        while n > 0:
            r = n % 26
            if r == 0:
                s[i] = 'Z'
                i+=1
                n=(n//26)-1
            else:
                s[i] = chr((r - 1) + ord('A'))
            i+=1
            n=n//26
            s[i] = '\0'
            t=s[::-1]
        return "".join(t)
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends
