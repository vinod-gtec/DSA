class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        set1=set(arr)
        a=[]
        for i in set1:
            temp=arr.count(i)
            if temp in a:
                return False
            else:
                a.append(temp)
        return True

        