class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        #O(n),O(1)
        
        n1,n2,cnt1,cnt2 = None,None,0,0
        
        for i in range(len(nums)):
            # print(n1,cnt1,n2,cnt2)
            if nums[i] == n1:
                cnt1+=1
            elif nums[i] == n2:
                cnt2+=1
            elif cnt1 == 0:
                n1 = nums[i]
                cnt1 = 1
            elif cnt2 == 0:
                cnt2 = 1
                n2 = nums[i]
            else:
                cnt1-=1
                cnt2-=1
        # print(n1,n2)
        ans  = []
        
        if nums.count(n1)>len(nums)//3:
            ans.append(n1)
        if nums.count(n2)>len(nums)//3:
            ans.append(n2)
        return ans if ans else []
        
        
        #O(n),O(n)
#         dic={}
#         lis=[]
#         for i in nums:
#             if i in dic:
#                 dic[i]+=1

#             else:
#                 dic[i]=1
                
#             if dic[i]>len(nums)//3:
#                 lis.append(i)
#         if len(lis)==0 and len(nums)==1:
#             return nums
#         return list(set(lis))
        