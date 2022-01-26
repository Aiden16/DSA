class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        
        #not modifying array
        #use floyd algo
        slow,fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow==slow2:
                return slow2
        #let us modify the array
        
        for i in range(len(nums)):
            ind = abs(nums[i])
            
            # print(ind)
            if nums[ind]<0:
                # print(nums,nums[i],nums[nums[i]])
                return abs(nums[i])
            # if nums[i]<0:
            #     nums[-nums[i]] = -nums[-nums[i]]
            else:
                # print('--',ind,nums[nums[ind]],-nums[nums[ind]])
                nums[ind] = -nums[ind]
            # print(nums)