class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        cnt,majority = 0,-1
        
        for i in range(len(nums)):
            if cnt  == 0:
                majority = nums[i]
                cnt = 1
            elif nums[i] == majority:
                cnt+=1
            else:
                cnt-=1
        return majority
      
    

                
            
        # dic={}
        # # if len(n)
        # for i in nums:
        #     if i not in dic:
        #         dic[i]=1
        #     else:
        #         dic[i]+=1
        #         if dic[i]>len(nums)//2:
        #             return i
        # return nums[0]
                
        