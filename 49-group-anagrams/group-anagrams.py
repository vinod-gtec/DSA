class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        a=[]
        b={}
        for i in strs:
            temp=''.join(sorted(i))
            if temp in b.keys():
                b[temp].append(i)
            else:
                b[temp]=[i]
        for i in b.keys():
            a.append(b[i])
        return a