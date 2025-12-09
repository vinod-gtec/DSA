import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        punc=string.punctuation + " "
        #a=s.replace(",","").replace(":","").replace(" ","").replace(".","")

        for char in punc:
            s=s.replace(char,"")
        a=s
        a=a.lower()
        s1=a[::-1]
        if(a==s1):
            return True
        else:
            return False
        