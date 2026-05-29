class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=[]
        for i in nums:
            if i<10:
                temp.append(i)
            else:
                curr_temp=str(i)
                temp_sum=0
                for i in curr_temp:
                    temp_sum=temp_sum+int(i)
                temp.append(temp_sum)
        return min(temp)
