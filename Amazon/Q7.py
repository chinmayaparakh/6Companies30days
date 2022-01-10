from collections import OrderedDict

class Solution:
	def FirstNonRepeating(self, A):
	    # Code here
		s=set()
		dct=OrderedDict()
		res=''
		for i in A:
		    if i not in s:
		        s.add(i)
		        dct[i]=None
		        
		        res+=list(dct.keys())[0]
		        
		    else:
		        if i in dct:
		            del dct[i]
		            
		        if len(dct)==0:
		            res+='#'
		        else:
		            res+=list(dct.keys())[0]
	    return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends
