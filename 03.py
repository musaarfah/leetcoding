class Solution:
#  Solution one basic (not acceptible)  
   
    # def hasRepeatigChar(self,string):
    #     dict={}
    #     for char in string:
    #         if char in dict:
    #             dict[char]+=1
    #         else:
    #             dict[char]=1
        
        
    #     for element in dict:

    #         if dict[element]>1:
    #             return True
            
    #     return False

    
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if len(s)>1:
    #         if self.hasRepeatigChar(s):
    #             print(s[:-1])
    #             self.lengthOfLongestSubstring(s[:-1])
    #         else:
    #            return len(s)
    #     else:    
    #        return 1



# Solution 2 (178 cases passed ' ' issue)
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if not s:
    #         return 0

    #     traversed=[]
    #     lengths=[]

    #     count=0
    #     lengths.append(0)
    #     for i in range(len(s)):
    #         char=s[i]
    #         if char==' ':
    #             count+=1
            
    #         elif char not in traversed:
    #             traversed.append(char)
    #             count+=1

    #         else:
    #             lengths.append(count)
    #             count=1
    #     lengths.append(count)

    #     return max(lengths)
    


# final solution with hash

    def lengthOfLongestSubstring(self,s: str) -> int:
        max_length = 0
        start = 0
        dict = {}

        for i in range(len(s)):
            
            char = s[i]
            
            if char in dict and dict[char] >= start:
                start = dict[char] + 1
            
            dict[char] = i
            max_length = max(max_length, i - start + 1)
        return max_length
    
   

    
        

a1=Solution()
print(a1.lengthOfLongestSubstring('abc'))

