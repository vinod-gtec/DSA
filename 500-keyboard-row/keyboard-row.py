class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=[]
        checker=["qwertyuiop","asdfghjkl","zxcvbnm"]
        for i in words:
            word=i
            i=i.lower()
            n=len(i)
            j=0
            if i[j] in checker[0]:
                temp=checker[0]
            elif i[j] in checker[1]:
                temp=checker[1]
            else:
                temp=checker[2]
            while(j<n):
                if i[j] not in temp:
                    break
                j=j+1
                if j==n:
                    a.append(word)
        return a
                