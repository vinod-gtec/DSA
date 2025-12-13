class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        b=len(nums)
        for i in range(0,b):
            is_sorted = True
            for j in range(0,b-1):
                if(nums[j]<=nums[j+1]):
                    pass
                else:
                    is_sorted = False
                    break
            if is_sorted:
                return True
            temp=nums[0]
            for j in range(0,b-1):
                nums[j]=nums[j+1]
            nums[b-1]=temp
                
        return False


            