class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0

        while n!=0:
            rem = n%2
            if rem == 1:
                count+=1
            
            print(n)
            n=n//2
        
        return count
    


s=Solution()
print(s.hammingWeight(128))