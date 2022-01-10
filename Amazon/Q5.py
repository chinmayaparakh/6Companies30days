class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        contact.sort()
        t=''
        ans=[]
        for i in s:
            prev=''
            t+=i
            lst=[]
            for j in contact:
                if prev==j:
                    continue
                if t in j:
                    lst.append(j)
                prev=j
            if len(lst)==0:
                lst.append(0)
            ans.append(lst)
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
# } Driver Code Ends
