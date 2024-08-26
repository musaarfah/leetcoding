class Solution:
    
# bit manipulation
    # def subset(self,nums):
    #     result=[]

    #     for i in range(2**len(nums)):
    #         subest=[]
    #         for j in range(len(nums)):
    #             if (1<<j) & i:
    #                 subest.append(nums[j])
    #         result.append(subest)

    #     return result
    
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res= [[]]

        for num in nums:
            print(num)
            res += [curr + [num] for curr in res]
            print(res)

        return res
    

a=Solution()
nums=[1,2,3]
print(a.subsets(nums))


        