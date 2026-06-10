class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_sum=[]
        right_sum=[]
        for i in range(len(nums)):
            temp1=nums[0:i]
            if len(temp1)<=0:
                left_sum.append(0)
            else:
                see=sum(temp1)
                left_sum.append(see)
        for i in range(len(nums)-1,-1,-1):
            temp1=nums[len(nums):i:-1]
            if len(temp1)<=0:
                right_sum.append(0)
            else:
                see=sum(temp1)
                right_sum.append(see)
        right_sum=right_sum[::-1]
        ne=[]
        for i in range(len(nums)):
            ne.append(abs(left_sum[i]-right_sum[i]))
        return ne


        