class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        """
        a={}
        for i in nums:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        c=[]
        b=math.ceil(len(nums)/3)
        for key,value in a.items():
            if value>b:
                c.append(key)
        return c
        