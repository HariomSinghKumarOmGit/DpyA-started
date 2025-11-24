# by while loop 
n = 150

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        while n%2==0 :
            n //= 2
 
        print("hello")
        return n ==1
    
    








    
