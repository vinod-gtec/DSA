class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        a=list(word)
        vaal=set()
        count=0
        for i in a:
            temp1=i.upper()
            temp2=i.lower()
            if temp1 in vaal or temp2 in vaal:
                continue

            if temp1 in a and temp2 in a:
                count=count+1
                vaal.add(temp1)
                vaal.add(temp2)
        return len(vaal)/2