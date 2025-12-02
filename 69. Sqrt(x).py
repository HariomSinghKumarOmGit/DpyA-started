class Solution:
    def mySqrt(self, x: int) -> int:
    
        if x ==0:
            return 0
        l=0
        r=x
        ans=1

        while r>=l:
            mid = (l+r)//2
            midSq = mid*mid
            if midSq > x:
                r = mid-1
            else:
                ans = mid
                l = mid +1
        return ans