# by while loop 
n = 150

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n<=0:
#             return False
#         while n%2==0 :
#             n //= 2
 
#         print("hello")
#         return n ==1
    


#   RECOURSION =========> 

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # base case
        if (n<=0):
            return False
        if n==1:
            return True
        if n%2!=0:
            return False
        # recursive case
        return self.isPowerOfTwo(n//2)









    
