
class Solution:

    def amendSentence(self, s):

        # code here
        st=''
        n=len(s)
        j=0
        for i in range(n):
            if s[i].isupper():
                st+=' '
                st+=s[i].lower()
            else:
                st+=s[i]
        if st[0]==' ':
            st=st[1:]
        return st
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.amendSentence(s))
        

# } Driver Code Ends
