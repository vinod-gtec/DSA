class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        total=0
        pos=0
        for i in reversed(columnTitle):
            digit=ord(i)-64
            total=total+digit*26**pos
            pos=pos+1
        return total