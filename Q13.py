class Solution:
    def decodedString(self, Str):
        # code here
        integerstack = []
        stringstack = []
        temp = ""
        result = ""
        i = 0
        while i < len(Str):
            count = 0
            if (Str[i] >= '0' and Str[i] <='9'):
                while (Str[i] >= '0' and Str[i] <= '9'):
                    count = count * 10 + ord(Str[i]) - ord('0')
                    i += 1
                i -= 1
                integerstack.append(count)
            elif (Str[i] == ']'):
                temp = ""
                count = 0
     
                if (len(integerstack) != 0):
                    count = integerstack[-1]
                    integerstack.pop()
     
                while (len(stringstack) != 0 and stringstack[-1] !='[' ):
                    temp = stringstack[-1] + temp
                    stringstack.pop()
     
                if (len(stringstack) != 0 and stringstack[-1] == '['):
                    stringstack.pop()
     
                for j in range(count):
                    result = result + temp
     
                for j in range(len(result)):
                    stringstack.append(result[j])
     
                result = ""
     
            elif (Str[i] == '['):
                if (Str[i-1] >= '0' and Str[i-1] <= '9'):
                    stringstack.append(Str[i])
     
                else:
                    stringstack.append(Str[i])
                    integerstack.append(1)
     
            else:
                stringstack.append(Str[i])
             
            i += 1
     
        while len(stringstack) != 0:
            result = stringstack[-1] + result
            stringstack.pop()
     
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends
