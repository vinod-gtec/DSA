class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        a=[]
        for i in digits:
            s=s+str(i)
        val=int(s)+1
        str_val=str(val)
        for i in str_val:
            a.append(int(i))
        return a
        
