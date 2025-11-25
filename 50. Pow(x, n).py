class Solution:
    def myPw(self, x: float, n: int) -> float:
        # Base
        if n == 0:
            return 1
        if n == 1:
            return x
        # Recersive 
        a = self.myPw(x,n//2)

        if n%2 == 1:
            return a*a*x
        
        else:
            return a*a
    def myPow(self, x: float, n: int) -> float:
        if n>=0:
            return self.myPw(x,n)
        else:
            n*= -1
            return 1/self.myPw(x,n)
        
        
        
        