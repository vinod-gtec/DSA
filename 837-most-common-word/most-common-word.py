class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        a=paragraph.lower()
        b={}
        thi=[]
        for ch in "!?',;.":
            a = a.replace(ch, " ")
        para=a.split()
        for i in para:
            if i not in banned:
                thi.append(i)
        for i in thi:
            if i not in b:
                b[i]=1
            else:
                b[i]+=1
        return max(b,key=b.get)
        