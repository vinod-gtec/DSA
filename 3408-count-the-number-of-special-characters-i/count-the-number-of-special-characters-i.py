class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        vaal=set()
        for i in word:
            temp1=i.upper()
            temp2=i.lower()
            if temp1 in vaal or temp2 in vaal:
                continue

            if temp1 in word and temp2 in word:
                vaal.add(temp1)
                vaal.add(temp2)
        return len(vaal)/2