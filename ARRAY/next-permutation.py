class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind1=None
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind1 = i
                break
        if ind1==None:
            nums.reverse()
            return nums
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>nums[ind1]:
                nums[ind1],nums[i] = nums[i],nums[ind1]
                break
        p1=ind1+1
        p2=len(nums)-1
        while p1<=p2:
            nums[p1],nums[p2] = nums[p2],nums[p1]
            p1+=1
            p2-=1
