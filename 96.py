class Solution:
    def factorial(self, n: int) -> int:
        if n==1:
            return 1
        else:
         return n*self.factorial(n-1)
    
    def numTrees(self, n: int) -> int:
       if n==1:
          return 1
       elif n==2:
          return 2
       else:
            x=self.factorial(n)

            return x-1
