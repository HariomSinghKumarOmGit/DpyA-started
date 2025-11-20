class Solution:
    def isAlpha(self, s, i):
        #a-x , 0-1 --> Asclli value are char code of each value
        # for Asclli value we use or
        x = ord(s[i])
        if 97<=x<=122 or 48<=x<=57:
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        n = len(s)

        i,j = 0,n-1

        while i<j:
            if not self.isAlpha(s,i):
                i+=1
                continue
            if not self.isAlpha(s,j):
                j-=1
                continue
            
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
    
    #  this only works fro lowecase we converted all uppercase to lower case