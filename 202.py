class Solution:
    def isolateDigits(self,n):
        digits=[]

        while n>0:
            digits.append(n%10) ; n=n//10
        digits.reverse()

        sum=0
        
        for i in range(len(digits)):
            sum+=digits[i]**2

        return sum

        

        


    def isHappy(self, n: int) :
        i=0

        while i<10:
            n=self.isolateDigits(n)
            i+=1

        if n==1:
            return True
        else:
            return False

        

a=Solution()
print(a.isHappy(19))
