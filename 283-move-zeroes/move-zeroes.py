class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        i=0
        arr_len=len(nums)
        if len(nums)==1:
            return nums
        i=0
        arr_len=len(nums)
        while 0 in nums:
            nums.remove(0)
        print(nums)
        a=arr_len-len(nums)
        for i in range(0,a):
            nums.append(0)
        print(nums)
        print(nums)
        a=arr_len-len(nums)
        for i in range(0,a):
            nums.append(0)
        print(nums)