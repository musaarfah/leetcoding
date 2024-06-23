class Solution:
    def topKFrequent(self, nums, k):
        count_dict={}

        for num in nums:
            if num in count_dict:
                count_dict[num]+=1

            else:
                count_dict[num]=1


        sorted_count_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))


        count_list=[]
        count=1
        for value in sorted_count_dict:
            if count<=k:
                count_list.append(value)
                count+=1
            else:
                break

        return count_list
    
a= Solution()

print(a.topKFrequent([1,1,1,2,2,3],2))