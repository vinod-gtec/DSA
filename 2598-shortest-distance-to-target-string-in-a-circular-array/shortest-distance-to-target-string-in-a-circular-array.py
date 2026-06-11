class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        a=[]
        if target not in words:
            return -1
        if words[startIndex]==target:
            return 0
        n=len(words)
        for i in range(n-1):
            if words[(startIndex+i+1)%n]==target:
                a.append(i+1)
        counter=0
        for i in range(n-1,-1,-1):
            if words[(startIndex+i)%n]==target:
                a.append(n-i)
        return min(a)
        