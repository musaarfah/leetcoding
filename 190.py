class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):  
            result <<= 1
            
           
            last_bit = n & 1
            
           
            result |= last_bit
            
          
            n >>= 1
        
        return result 

    
a=Solution()
print(a.reverseBits(11111111111111111111111111111101))