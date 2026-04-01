class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights)==0:
            return 0
        if len(heights)==1:
            return 1
        count=0
        dup_heights=sorted(heights)
        for i in range(len(heights)):
            if heights[i]==dup_heights[i]:
                pass
            else:
                count=count+1
        return count
        