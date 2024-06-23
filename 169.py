class Solution:
    def majorityElement(self, nums) -> int:
        n=len(nums)//2

        hmap={}

        for element in nums:
            if element in hmap:
                hmap[element]+=1

            else:
                hmap[element]=1

        for element in hmap:
            if hmap[element]>n:
                return element
            
            
        