class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=[]
        s=str(bin(num)[2:])
        for i in s:
            if i=="1":
                count.append("0")
            else:
                count.append("1")
        st="".join(count)
        number = int(st, 2)


                
        return number

        