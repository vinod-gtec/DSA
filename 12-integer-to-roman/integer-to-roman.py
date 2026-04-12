class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        n=len(str(num))
        count=n
        dict1={
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            50:"L",
            40:"XL",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }
        r=""
        for i in [1000,900,500,400,100,90,50,40,10,9,5,4,1]:
            while(i<=num):
                r+=dict1[i]
                num=num-i
        return r
